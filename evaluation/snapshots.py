import json
from pathlib import Path
from typing import Dict, List, Type, TypeAlias

from src.crewai_poetry_crew.utilities.models import (
    MuseModel,
    GardenerModel,
    PoetModel,
    PsychologistModel,
    ArchitectModel,
    EditorModel,
    # Uncomment / add these if you have them:
    # CriticModel,
    # PublisherModel,
    Snapshot,
)


# Union of all artefacts that can appear in the run log
RunArtefact: TypeAlias = (
    MuseModel
    | GardenerModel
    | PoetModel
    | PsychologistModel
    | ArchitectModel
    | EditorModel
    # | CriticModel
    # | PublisherModel
)


# Map the "type" field in JSON to the corresponding Pydantic model
TYPE_MAPPING: Dict[str, Type[RunArtefact]] = {
    "muse_model": MuseModel,
    "gardener_model": GardenerModel,
    "poet_model": PoetModel,
    "psychologist_model": PsychologistModel,
    "architect_model": ArchitectModel,
    "editor_model": EditorModel,
    # "critic_model": CriticModel,
    # "publisher_model": PublisherModel,
}


def _parse_artefact(obj: dict) -> RunArtefact:
    """
    Parse a single JSON object from the run log into the appropriate
    Pydantic model, based on its `type` field.
    """
    artefact_type = obj.get("type")
    model_cls = TYPE_MAPPING.get(artefact_type)

    if model_cls is None:
        raise ValueError(f"Unknown artefact type: {artefact_type!r}")

    # Pydantic v2: model_validate
    # If you're on v1, swap to: return model_cls.parse_obj(obj)
    return model_cls.model_validate(obj)  # type: ignore[attr-defined]


def load_artefacts_from_json(path: str | Path) -> List[RunArtefact]:
    """
    Load a run log JSON file (the one your crew writes) and convert it into
    a list of typed artefacts (MuseModel, PoetModel, ArchitectModel, etc.).
    """
    path = Path(path)
    data = json.loads(path.read_text())

    if not isinstance(data, list):
        raise ValueError("Run log JSON must be a list of artefacts")

    return [_parse_artefact(obj) for obj in data]


def build_snapshots(artefacts: List[RunArtefact]) -> Dict[int, Snapshot]:
    """
    Group artefacts by poem version into Snapshot objects.

    Rules:
        - PoetModel: use poet.poem.version
        - ArchitectModel: use architect.poem.version
        - EditorModel: use editor.poem.version
        - PsychologistModel: use psychologist.psychologist_notes.poem_version

    Other artefacts (Muse, Gardener, etc.) are ignored for snapshot grouping.
    """

    snapshots: Dict[int, Snapshot] = {}

    def get_snapshot(version: int) -> Snapshot:
        if version not in snapshots:
            snapshots[version] = Snapshot(version=version)
        return snapshots[version]

    for artefact in artefacts:
        # Poet
        if isinstance(artefact, PoetModel):
            version = artefact.poem.version
            snap = get_snapshot(version)
            snap.poet = artefact

            # Optional: capture persona from the poet if you store it there
            if getattr(artefact, "persona", None) and not snap.persona:
                snap.persona = artefact.persona  # type: ignore[attr-defined]

        # Psychologist
        elif isinstance(artefact, PsychologistModel):
            version = artefact.psychologist_notes.poem_version
            snap = get_snapshot(version)
            snap.psychologist = artefact

        # Architect
        elif isinstance(artefact, ArchitectModel):
            version = artefact.poem.version
            snap = get_snapshot(version)
            snap.architect = artefact

        # Editor
        elif isinstance(artefact, EditorModel):
            version = artefact.poem.version
            snap = get_snapshot(version)
            snap.editor = artefact

        # Muse / Gardener / etc. are ignored for Snapshot; they live upstream

    return snapshots


def build_snapshots_from_json(path: str | Path) -> Dict[int, Snapshot]:
    """
    Convenience entry point: load a run log JSON file and build snapshots.
    """
    artefacts = load_artefacts_from_json(path)
    return build_snapshots(artefacts)

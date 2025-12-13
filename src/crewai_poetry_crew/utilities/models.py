from typing import List, Literal, TypeAlias, Optional
from pydantic import BaseModel, Field


# 1. Concepts
class Concept(BaseModel):
    type: str = Field("concept", description="Model type discriminator.")
    id: int
    text: str = Field(
        ...,
        description="One emotionally distinct concept universe."
    )

# 2. Seeds
class Seed(BaseModel):
    type: str = Field("seed", description="Model type discriminator.")
    id: int
    from_concept_id: int
    text: str = Field(
        ...,
        description="Distilled emotional seed from a concept."
    )

# 3. Poems
class Poem(BaseModel):
    type: str = Field("poem", description="Model type discriminator.")
    title: str = Field(
        ...,
        description="Single-line title of the poem."
    )
    text: str = Field(
        ...,
        description="Raw multi-line poem text with indentation preserved."
    )
    version: int = Field(
        0,
        description="Integer version number of the poem."
    )

# 4. Architect Notes
class ArchitectNotes(BaseModel):
    type: str = Field("architect_notes", description="Model type discriminator.")
    bullets: List[str] = Field(
        ...,
        description="Summary bullets of architectural changes."
    )

# 5. Editor Notes
class EditorNotes(BaseModel):
    type: str = Field("editor_notes", description="Model type discriminator.")
    bullets: List[str] = Field(
        ...,
        description="Summary bullets of editorial suggestions."
    )

# 6. Review (Critic)
class Review(BaseModel):
    type: str = Field("review", description="Model type discriminator.")
    title: str
    body: str = Field(
        ...,
        description="Full critic review text."
    )

# ... existing imports ...

# 7. Psychologist Report Sub-Components
class TraumaLoop(BaseModel):
    label: str
    description: str
    evidence_lines: List[str]

class AttachmentDynamics(BaseModel):
    style: str = Field(..., description="e.g., avoidant, ambivalent, disorganized, secure")
    description: str
    evidence_lines: List[str]

class Dissociation(BaseModel):
    present: bool
    description: str
    evidence_lines: List[str]

class TimeDynamics(BaseModel):
    patterns: List[str]
    description: str
    evidence_lines: List[str]

class ContainmentStrategy(BaseModel):
    strategies: List[str]
    description: str
    evidence_lines: List[str]

class DefenseMechanism(BaseModel):
    label: str
    description: str
    evidence_lines: List[str]

class PsychologistNotes(BaseModel):
    type: str = Field("psychologist_notes", description="Model type discriminator.")
    poem_version: int
    notes: str
    leverage_for_poet: List[str]
    leverage_for_architect: List[str]
    leverage_for_editor: List[str]

# Collection aliases
Concepts: TypeAlias = List[Concept]
Seeds: TypeAlias = List[Seed]

# Agent return type models
class MuseModel(BaseModel):
    type: str = Field("muse_model", description="Model type discriminator.")
    concepts: Concepts

class GardenerModel(BaseModel):
    type: str = Field("gardener_model", description="Model type discriminator.")
    seeds: Seeds

class PoetModel(BaseModel):
    type: str = Field("poet_model")
    poem: Poem

class PsychologistModel(BaseModel):
    type: str = Field("psychologist_model", description="Model type discriminator.")
    psychologist_notes: PsychologistNotes
    poem: Poem

class ArchitectModel(BaseModel):
    type: str = Field("architect_model", description="Model type discriminator.")
    architect_notes: ArchitectNotes
    psychologist_notes: PsychologistNotes
    poem: Poem

class EditorModel(BaseModel):
    type: str = Field("editor_model", description="Model type discriminator.")
    editor_notes: EditorNotes
    architect_notes: ArchitectNotes
    psychologist_notes: PsychologistNotes
    poem: Poem


class SentinelModel(BaseModel):
    type: str = Field("sentinel_model", description="Model type discriminator.")
    forbidden_new_words: List[str]

class EvaluatorModel(BaseModel):
    """
    Neutral evaluation of two poem versions (poem_a and poem_b)
    for a given persona-poet.
    """
    type: Literal["evaluator_model"] = Field(
        "evaluator_model",
        description="Discriminator for the evaluator model type.",
    )
    persona: str = Field(
        ...,
        description="Name of the persona-poet whose identity is used for evaluation (e.g. 'Richard Siken').",
    )
    version_a: int = Field(
        ...,
        description="Version number of poem_a (the lower version number).",
    )
    version_b: int = Field(
        ...,
        description="Version number of poem_b (the higher version number).",
    )

    persona_alignment_a: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Persona alignment score for poem_a, in [0.0, 1.0].",
    )
    persona_alignment_b: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Persona alignment score for poem_b, in [0.0, 1.0].",
    )
    persona_alignment_difference: float = Field(
        ...,
        description="Difference persona_alignment_b - persona_alignment_a.",
    )

    global_escalation_a: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree of emotional pressure escalation in poem_a, in [0.0, 1.0].",
    )
    global_escalation_b: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree of emotional pressure escalation in poem_b, in [0.0, 1.0].",
    )

    pressure_instability_a: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree of instability / self-contradiction in poem_a, in [0.0, 1.0].",
    )
    pressure_instability_b: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree of instability / self-contradiction in poem_b, in [0.0, 1.0].",
    )

    motif_evolution_a: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree to which motifs recur and evolve in poem_a, in [0.0, 1.0].",
    )
    motif_evolution_b: float = Field(
        ...,
        ge=0.0,
        le=1.0,
        description="Degree to which motifs recur and evolve in poem_b, in [0.0, 1.0].",
    )

    reader_score_a: int = Field(
        ...,
        ge=0,
        le=100,
        description="0–100 estimate of how a serious poetry reader would rate poem_a.",
    )
    reader_score_b: int = Field(
        ...,
        ge=0,
        le=100,
        description="0–100 estimate of how a serious poetry reader would rate poem_b.",
    )

    persona_score_a: int = Field(
        ...,
        ge=0,
        le=100,
        description="0–100 estimate of how the persona-poet would rate poem_a.",
    )
    persona_score_b: int = Field(
        ...,
        ge=0,
        le=100,
        description="0–100 estimate of how the persona-poet would rate poem_b.",
    )

    summary: str = Field(
        ...,
        description="2–5 sentence neutral comparison of key differences between poem_a and poem_b.",
    )
    risks_or_regressions: str = Field(
        ...,
        description="1–3 sentences describing any weaknesses, risks, or regressions observed in either poem.",
    )

class CriticModel(BaseModel):
    type: str = Field("critic_model", description="Model type discriminator.")
    review: Review

class PublisherModel(BaseModel):
    type: str = Field("publisher_model", description="Model type discriminator.")
    file_path: str

### Snapshot for Metrics and Reporting ###

class Snapshot(BaseModel):
    """
    Aggregates all artefacts associated with a single poem version.
    This is built offline from the JSON run log by grouping actor
    outputs that share the same poem version id.
    """

    version: int = Field(
        ...,
        description="Poem version identifier shared by all artefacts in this snapshot."
    )

    # Optional per-version metadata (set by your eval layer, not the crew).
    persona: Optional[str] = Field(
        None,
        description="Persona label for this run/version (e.g. 'siken'), if known."
    )

    # Actor artefacts for this version.
    poet: Optional[PoetModel] = Field(
        None,
        description="PoetModel output for this version, if any."
    )
    psychologist: Optional[PsychologistModel] = Field(
        None,
        description="PsychologistModel analysing this version, if any."
    )
    architect: Optional[ArchitectModel] = Field(
        None,
        description="ArchitectModel transforming this version, if any."
    )
    editor: Optional[EditorModel] = Field(
        None,
        description="EditorModel commenting on this version, if any."
    )

    @property
    def poem(self) -> Optional[Poem]:
        """
        Convenience accessor for the poem associated with this version.

        Preference order (most downstream first):
            1. Editor's poem (if present)
            2. Architect's poem
            3. Poet's poem

        Returns None if no poem is attached in this snapshot.
        """
        if self.editor is not None:
            return self.editor.poem
        if self.architect is not None:
            return self.architect.poem
        if self.poet is not None:
            return self.poet.poem
        return None

import yaml
import os
from pathlib import Path
from pydantic import BaseModel
from typing import List
import pprint

class Persona(BaseModel):
    id: str
    name: str
    description: str
    poet: str
    architect: str
    editor: str

DEFAULT_FILENAME = Path(__file__).parent / "config" / "personas.yaml"

def read_personas(filename: Path = DEFAULT_FILENAME) -> List[Persona]:
    """
    Reads the personas.yaml file and returns a list of Persona objects.

    Args:
        filename (Path): Path to the personas.yaml file. Defaults to "src/crewai_poetry_crew/config/personas.yaml".

    Returns:
        List[Persona]: A list of Persona objects.
    """
    if not filename.exists():
        raise FileNotFoundError(f"The file {filename} does not exist.")

    with open(filename, 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
    # Assuming the YAML is a dict with persona keys, convert to list of Persona
    personas = []
    for persona_id, persona_data in data.items():
        persona_dict = {'id': persona_id, **persona_data}
        persona = Persona(**persona_dict)
        personas.append(persona)
    return personas

def get_persona(name: str, filename: Path = DEFAULT_FILENAME) -> Persona:
    """
    Reads the personas.yaml file and returns the Persona with the specified name.

    Args:
        filename (Path): Path to the personas.yaml file.
        name (str): The name (id) of the persona to retrieve.

    Returns:
        Persona: The requested Persona object.

    Raises:
        ValueError: If the persona with the given name is not found.
    """
    personas = read_personas(filename)
    for persona in personas:
        if persona.id == name:
            return persona
    raise ValueError(f"Persona with name '{name}' not found.")
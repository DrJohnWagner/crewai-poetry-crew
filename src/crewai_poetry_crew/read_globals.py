from typing import Any, Dict
from pydantic import BaseModel, Field
from pathlib import Path
from typing import Union
import yaml  # PyYAML


class GlobalsBlock(BaseModel):
    """
    Inner model for the `globals` section of globals.yaml.
    """

    comments: str = Field(
        ...,
        alias="COMMENTS",
        description="Comments section.",
    )

    global_meta_guardrails: str = Field(
        ...,
        alias="GLOBAL_META_GUARDRAILS",
        description="Global meta / safety guardrails applied to all agents.",
    )

    universal_section_format: str = Field(
        ...,
        alias="UNIVERSAL_SECTION_FORMAT",
        description="Global universal section format applied to all agents.",
    )

    tool_usage_instructions: str = Field(
        ...,
        alias="TOOL_USAGE_INSTRUCTIONS",
        description="Shared instructions for how agents must format and use tools.",
    )

    poet_antipattern_instruction: str = Field(
        ...,
        alias="POET_ANTIPATTERN_INSTRUCTION",
        description="Global anti-pattern rules for poet personas.",
    )

    class Config:
        # allow both Pythonic names and YAML-style aliases
        allow_population_by_field_name = True
        extra = "ignore"  # or "allow" if you expect more keys


class GlobalConfig(BaseModel):
    """
    Pydantic model representing the contents of globals.yaml.

    The YAML structure is:

        globals:
            COMMENTS: |
                ...
            GLOBAL_META_GUARDRAILS: |
                ...
            UNIVERSAL_SECTION_FORMAT: |
                ...
            TOOL_USAGE_INSTRUCTIONS: |
                ...
            POET_ANTIPATTERN_INSTRUCTION: |
                ...

    Access via `config.globals_.comments`, `config.globals_.global_meta_guardrails`, etc.
    """

    globals_: GlobalsBlock = Field(
        ...,
        alias="globals",
        description="Top-level globals block from globals.yaml.",
    )

    class Config:
        allow_population_by_field_name = True
        extra = "ignore"  # ignore any unexpected top-level keys


def read_globals(path: Union[str, Path]) -> GlobalConfig:
    """
    Read the globals.yaml file and convert it into a GlobalConfig instance.
    """
    path = Path(path)

    with path.open("r", encoding="utf-8") as f:
        raw_data = yaml.safe_load(f) or {}

    return GlobalConfig(**raw_data)


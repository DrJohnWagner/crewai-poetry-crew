#!/usr/bin/env python
import os
import sys
from unittest import result
import warnings
from pathlib import Path
from datetime import datetime
# from contextlib import redirect_stdout, redirect_stderr
from crewai_poetry_crew.crew import CrewAIPoetryCrew
from .redirect import redirect_stdout, redirect_stderr
from .read_personas import get_persona
from .read_globals import read_globals
from .create_logger import create_logger
from .create_logger import create_log_file

from prompts import PROMPT

logger = create_logger("crewai")

globals = read_globals(Path("src/crewai_poetry_crew/config/globals.yaml"))
globals = globals.globals_

persona = get_persona(name="Richard-Siken")
# persona = get_persona(name="Rainer-Maria-Rilke")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


INPUTS = {
    'GLOBAL_META_GUARDRAILS': globals.global_meta_guardrails,
    'UNIVERSAL_SECTION_FORMAT': globals.universal_section_format,
    'TOOL_USAGE_INSTRUCTIONS': globals.tool_usage_instructions,
    'POET_ANTIPATTERN_INSTRUCTION': globals.poet_antipattern_instruction,
    "REVIEW_LENGTH": "300-500",
    "CONCEPTS": "3",
    "EDITS": "3-5",
    "POET": persona.poet,
    "ARCHITECT": persona.architect,
    "EDITOR": persona.editor,
    "PROMPT": PROMPT
}

def run():
    """
    Run the crew.
    """
    inputs = INPUTS | {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }

    try:
        filename = create_log_file(name="crewai", suffix=".out")
        with open(filename, 'w') as f:
            with redirect_stdout(f), redirect_stderr(f):
                result = CrewAIPoetryCrew().crew().kickoff(inputs=inputs)
                logger.info(f"Crew execution completed: {result}")
                print(f"\nCrew Output:\n{result.raw}\n", file=sys.stderr)
                print(f"\nToken Usage:\n{result.token_usage}\n", file=sys.stderr)
    except Exception as e:
        logger.error(f"Crew execution failed: {e}")
        raise Exception(f"An error occurred while running the crew: {e}")

def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = INPUTS | {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }
    try:
        CrewAIPoetryCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        CrewAIPoetryCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = INPUTS | {
        'topic': 'AI LLMs',
        'current_year': str(datetime.now().year)
    }

    try:
        CrewAIPoetryCrew().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = INPUTS | {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": ""
    }

    try:
        result = CrewAIPoetryCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

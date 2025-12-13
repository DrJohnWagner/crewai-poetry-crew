#!/usr/bin/env python
import os
import sys
import json
import warnings
from pathlib import Path
from datetime import datetime

from crewai_poetry_crew.crew import CrewAIPoetryCrew
from .redirect import redirect_stdout, redirect_stderr
from crewai_poetry_crew.utilities.read_personas import get_persona
from crewai_poetry_crew.utilities.globals import GLOBAL_INPUTS
from crewai_poetry_crew.utilities.create_logger import create_logger
from crewai_poetry_crew.utilities.create_logger import create_log_file

logger = create_logger("crewai")

PROMPT = "Your name is a knot I can't untie in my chest."

PROMPT = """
Two former lovers, who had a torrid affair years ago but then
broke it off suddenly, go for a drive through the snow-covered
mountains where they used to go to be intimate. Things happen.
They are both emotionally wrecked afterward.
"""
PROMPT = """
Write 5 short sentences from inside an ordinary, everyday situation
(kitchen, street, car, office, waiting room, errand).

Something external is making the situation uncomfortable,
but you must NOT name or describe pressure, tension, stress,
force, threat, or emotion in any way.

Show this only through concrete actions, objects, repetition,
mis-timing, or small behavioral distortions.

Use plain, conversational language.
Avoid metaphor, symbolism, and explanation.
Dry or awkward humor is allowed only if it does not relieve anything.

Stop without resolving or concluding.
"""
# persona = get_persona(name="Richard-Siken")
persona = get_persona(name="Siken-Barnett")
# persona = get_persona(name="Rainer-Maria-Rilke")

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# ---------------------------------------------------------------------------
# Base INPUTS
# ---------------------------------------------------------------------------

INPUTS = {
    "REVIEW_LENGTH": "300-500",
    "CONCEPTS": "5",
    "CONCEPT_SENTENCES": "4-6",
    "SEED_SENTENCES": "3-5",
    "POET_NAME": persona.name,
    "POET_DESCRIPTION": persona.description,
    "POET_AGENT": persona.poet_agent,
    "POET_TASK": persona.poet_task,
    "PSYCHOLOGIST_AGENT": persona.psychologist_agent,
    "PSYCHOLOGIST_TASK": persona.psychologist_task,
    "ARCHITECT_AGENT": persona.architect_agent,
    "ARCHITECT_TASK": persona.architect_task,
    "EDITOR_AGENT": persona.editor_agent,
    "EDITOR_TASK": persona.editor_task,
    "PROMPT": PROMPT,
}

# Merge in the agent model JSON examples
INPUTS |= GLOBAL_INPUTS

def run():
    """
    Run the crew.
    """
    inputs = INPUTS | {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }

    try:
        filename = create_log_file(name="crewai", suffix=".out")
        with open(filename, "w") as f:
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
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }
    try:
        CrewAIPoetryCrew().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
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
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year),
    }

    try:
        CrewAIPoetryCrew().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json as _json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = _json.loads(sys.argv[1])
    except _json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    inputs = INPUTS | {
        "crewai_trigger_payload": trigger_payload,
        "topic": "",
        "current_year": "",
    }

    try:
        result = CrewAIPoetryCrew().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")

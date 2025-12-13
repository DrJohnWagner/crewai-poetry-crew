from crewai import Task, Agent
from typing import Callable, Any, List

from crewai_poetry_crew.utilities.globals import EXPECTED_OUTPUT
from crewai_poetry_crew.utilities.models import PsychologistModel
from crewai_poetry_crew.utilities.save_to_file import save_to_file
from crewai_poetry_crew.utilities.load_template import load_task_template

def PsychologistTask(
    agent: Agent,
    task_name: str,
    context: List[Task],
    callback: Callable[[Any], None],
    verbose: bool = False,
    save_description: bool = False
) -> Task:
    # This loads from Psychologist.yaml and injects {{PSYCHOLOGIST}} from the persona
    template = load_task_template("Psychologist", task_name)
    
    if save_description:
        save_to_file(template["description"], f"descriptions/{task_name}.txt")
        
    return Task(
        task_name=task_name,
        description=template["description"],
        expected_output=EXPECTED_OUTPUT("PsychologistModel"),
        agent=agent,
        context=context,
        output_pydantic=PsychologistModel,
        callback=callback,
        verbose=verbose,
    )
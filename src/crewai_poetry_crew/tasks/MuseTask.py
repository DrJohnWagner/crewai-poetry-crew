from crewai import Task, Agent
from typing import Callable, Any, List

from crewai_poetry_crew.utilities.globals import EXPECTED_OUTPUT
from crewai_poetry_crew.utilities.globals import STRUCTURED_OUTPUT_INSTRUCTION
from crewai_poetry_crew.utilities.globals import CONCEPTS
from crewai_poetry_crew.utilities.models import MuseModel
from crewai_poetry_crew.utilities.save_to_file import save_to_file
from crewai_poetry_crew.utilities.load_template import load_task_template

def MuseTask(
    task_name: str,
    agent: Agent,
    callback: Callable[[Any], None],
    agent_name: str = None,
    context: List[Task] | None = None,
    verbose: bool = False,
    save_description: bool = False,
) -> Task:
    agent_name = agent_name or "Muse"
    template = load_task_template(agent_name, task_name)
    if save_description:
        save_to_file(template["description"], f"descriptions/{task_name}.txt")
    return Task(
        task_name=task_name,
        description=template["description"],
        expected_output=EXPECTED_OUTPUT("MuseModel"),
        agent=agent,
        context=context or [],
        output_pydantic=MuseModel,
        callback=callback,
        verbose=verbose,
    )

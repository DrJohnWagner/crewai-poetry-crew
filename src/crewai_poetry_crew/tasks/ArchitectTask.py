from crewai import Task, Agent
from typing import Callable, Any, List

from crewai_poetry_crew.utilities.globals import EXPECTED_OUTPUT, EXTRACT_POEM_FROM_INPUT, STRUCTURED_OUTPUT_INSTRUCTION
from crewai_poetry_crew.utilities.load_template import load_task_template
from crewai_poetry_crew.utilities.models import ArchitectModel
from crewai_poetry_crew.utilities.save_to_file import save_to_file

def ArchitectTask(
    task_name: str,
    agent: Agent,
    callback: Callable[[Any], None],
    agent_name: str = None,
    context: List[Task] | None = None,
    verbose: bool = False,
    save_description: bool = False,
) -> Task:
    agent_name = agent_name or "Architect"
    template = load_task_template(agent_name, task_name)
    if save_description:
        save_to_file(template["description"], f"descriptions/{task_name}.txt")
    return Task(
        task_name=task_name,
        description=template["description"],
        expected_output=EXPECTED_OUTPUT("ArchitectModel"),
        agent=agent,
        context=context or [],
        output_pydantic=ArchitectModel,
        callback=callback,
        verbose=verbose,
    )

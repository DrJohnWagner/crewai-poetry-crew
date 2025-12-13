from enum import Enum
from crewai import Task, Agent
from typing import Callable, Any, List

from crewai_poetry_crew.utilities.globals import EXPECTED_OUTPUT
from crewai_poetry_crew.utilities.load_template import load_task_template
from crewai_poetry_crew.utilities.models import PoetModel
from crewai_poetry_crew.utilities.save_to_file import save_to_file

def PoetTask(
    task_name: str,
    agent: Agent,
    callback: Callable[[Any], None],
    agent_name: str = None,
    context: List[Task] | None = None,
    verbose: bool = False,
    save_description: bool = False,
) -> Task:
    agent_name = agent_name or "Poet"
    template = load_task_template(agent_name, task_name)
    if save_description:
        save_to_file(template["description"], f"descriptions/{task_name}.txt")
    return Task(
        task_name=task_name,
        description=template["description"],
        expected_output=EXPECTED_OUTPUT("PoetModel"),
        agent=agent,
        context=context or [],
        output_pydantic=PoetModel,
        callback=callback,
        verbose=verbose,
    )

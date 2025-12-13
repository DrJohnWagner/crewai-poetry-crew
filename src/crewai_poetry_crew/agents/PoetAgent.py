from crewai import LLM, Agent

from crewai_poetry_crew.utilities.load_template import load_agent_template
from crewai_poetry_crew.utilities.save_to_file import save_to_file


def PoetAgent(
    llm: LLM,
    name: str = None,
    role: str = None,
    tools: list | None = None,
    memory: bool = False,
    verbose: bool = False,
    allow_delegation: bool = False,
    save_backstory: bool = False,
    ) -> Agent:
    name = name or "Poet"
    template = load_agent_template(name)
    if save_backstory:
        save_to_file(template["backstory"], f"descriptions/{name}.txt")
    return Agent(
        llm=llm,
        name=name,
        role=role or template["role"],
        tools=tools or [],
        memory=memory,
        goal=template["goal"],
        backstory=template["backstory"],
        verbose=verbose,
        allow_delegation=allow_delegation,
    )

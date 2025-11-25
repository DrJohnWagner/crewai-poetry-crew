import os
from typing import List
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from .tools import ClicheDetectionTool, MarkdownWriterTool
from .tools.ClicheDetectionTool import ClicheDetectionTool
from .tools.MarkdownWriterTool import MarkdownWriterTool
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
# src/my_crew/crew.py

load_dotenv()

# llm = LLM(
#     model="gemini/gemini-2.0-flash",
#     verbose=True,
#     temperature=0.2,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0.2,
    verbose=True

)

# Initialize the tool
cliche_detection_tool = ClicheDetectionTool()
markdown_writer_tool = MarkdownWriterTool()

@CrewBase
class CrewAIPoetryCrew():
    """CrewAIPoetryCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
    
    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def muse(self) -> Agent:
        return Agent(
            config=self.agents_config['muse'], # type: ignore[index]
            llm=llm,
            verbose=False
        )

    @agent
    def summariser(self) -> Agent:
        return Agent(
            config=self.agents_config['summariser'], # type: ignore[index]
            llm=llm,
            verbose=False
        )

    @agent
    def poet(self) -> Agent:
        return Agent(
            config=self.agents_config['poet'], # type: ignore[index]
            llm=llm,
            verbose=True
        )

    @agent
    def architect(self) -> Agent:
        return Agent(
            config=self.agents_config['architect'], # type: ignore[index]
            llm=llm,
            verbose=True
        )

    @agent
    def editor(self) -> Agent:
        return Agent(
            config=self.agents_config['editor'], # type: ignore[index]
            llm=llm,
            verbose=True
        )

    @agent
    def critic(self) -> Agent:
        return Agent(
            config=self.agents_config['critic'], # type: ignore[index]
            llm=llm,
            verbose=False
        )

    @agent
    def publisher(self) -> Agent:
        return Agent(
            config=self.agents_config['publisher'], # type: ignore[index]
            tools=[MarkdownWriterTool()],
            llm=llm,
            verbose=False
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def task_inspire(self) -> Task:
        return Task(
            config=self.tasks_config['task_inspire'], # type: ignore[index]
        )

    @task
    def task_summarise(self) -> Task:
        return Task(
            config=self.tasks_config['task_summarise'], # type: ignore[index]
        )

    @task
    def task_write(self) -> Task:
        return Task(
            config=self.tasks_config['task_write'], # type: ignore[index]
        )

    @task
    def task_architect_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_architect_one'], # type: ignore[index]
        )

    @task
    def task_edit_one(self) -> Task:
        return Task(
            config=self.tasks_config['task_edit_one'], # type: ignore[index]
        )

    @task
    def task_revise(self) -> Task:
        return Task(
            config=self.tasks_config['task_revise'], # type: ignore[index]
        )

    @task
    def task_architect_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_architect_two'], # type: ignore[index]
        )

    @task
    def task_edit_two(self) -> Task:
        return Task(
            config=self.tasks_config['task_edit_two'], # type: ignore[index]
        )

    @task
    def task_finalise(self) -> Task:
        return Task(
            config=self.tasks_config['task_finalise'], # type: ignore[index]
        )

    @task
    def task_review(self) -> Task:
        return Task(
            config=self.tasks_config['task_review'], # type: ignore[index]
        )

    @task
    def task_publish(self) -> Task:
        return Task(
            config=self.tasks_config['task_publish'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewAIPoetryCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

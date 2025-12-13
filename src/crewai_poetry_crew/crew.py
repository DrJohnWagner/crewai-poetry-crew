import json
import logging
from typing import List
from dotenv import load_dotenv
from pydantic import BaseModel

# from langchain_openai import ChatOpenAI
from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import before_kickoff
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from crewai_poetry_crew.agents.MuseAgent import MuseAgent
from crewai_poetry_crew.agents.GardenerAgent import GardenerAgent
from crewai_poetry_crew.agents.PoetAgent import PoetAgent
from crewai_poetry_crew.agents.PsychologistAgent import PsychologistAgent
from crewai_poetry_crew.agents.ArchitectAgent import ArchitectAgent
from crewai_poetry_crew.agents.EditorAgent import EditorAgent
from crewai_poetry_crew.agents.SentinelAgent import SentinelAgent
from crewai_poetry_crew.agents.EvaluatorAgent import EvaluatorAgent
from crewai_poetry_crew.agents.CriticAgent import CriticAgent
from crewai_poetry_crew.agents.PublisherAgent import PublisherAgent
from crewai_poetry_crew.tasks.MuseTask import MuseTask
from crewai_poetry_crew.tasks.GardenerTask import GardenerTask
from crewai_poetry_crew.tasks.PoetTask import PoetTask
from crewai_poetry_crew.tasks.PsychologistTask import PsychologistTask
from crewai_poetry_crew.tasks.ArchitectTask import ArchitectTask
from crewai_poetry_crew.tasks.EditorTask import EditorTask
from crewai_poetry_crew.tasks.SentinelTask import SentinelTask
from crewai_poetry_crew.tasks.EvaluatorTask import EvaluatorTask
from crewai_poetry_crew.tasks.CriticTask import CriticTask
from crewai_poetry_crew.tasks.PublisherTask import PublisherTask

from crewai_poetry_crew.tools.PrintPoemAndReviewTool import PrintPoemAndReviewTool

# from crewai_poetry_crew.utilities.models import MuseModel, GardenerModel
# from crewai_poetry_crew.utilities.models import PoetModel, ArchitectModel, EditorModel
# from crewai_poetry_crew.utilities.models import CriticModel, PublisherModel
from crewai_poetry_crew.utilities.create_logger import create_log_file

EVALUATE = True
INCLUDE_CRITIC_AND_PUBLISHER = False

logger = logging.getLogger("crewai")

load_dotenv()

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators
# src/my_crew/crew.py

# llm = LLM(
#     model="gemini/gemini-2.0-flash",
#     verbose=True,
#     temperature=0.2,
#     google_api_key=os.getenv("GOOGLE_API_KEY")
# )

llm = LLM(model="gpt-5-nano")
# llm = LLM(model="gpt-5-nano", temperature=0.20)
# llm_muse = LLM(model="gpt-5-nano", temperature=0.55)
llm_poet = LLM(model="gpt-5")
@CrewBase
class CrewAIPoetryCrew():
    """CrewAIPoetryCrew crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    models: List[BaseModel]
    filename: str

    @before_kickoff
    def init_logging_and_state(self, inputs):
        self.filename = create_log_file("crewai", ".json")
        self.models = []
        return inputs

    def write_output_as_json(self, output):
        try:
            model = getattr(output, "pydantic", None)
            if model is None:
                raw = getattr(output, "raw", "")[:120]
                logger.warning(f"[TASK WARNING] No pydantic model; raw[:120]={raw}")
            else:
                model_json = model.model_dump_json(indent=4, ensure_ascii=False)
                logger.info(f"[TASK DONE JSON] {model_json}")
                #
                self.models.append(model)
                with open(self.filename, "w") as f:
                    models = [model.model_dump() for model in self.models]
                    json.dump(models, f, indent=4)
                    logger.info(
                        f"[TASK DONE FILE] {self.filename} written with {len(models)} models"
                    )
        except Exception as e:
            logger.error(f"Error in task listener: {e}")

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    @agent
    def muse(self) -> Agent:
        return MuseAgent(llm=llm, verbose=False, save_backstory=True)

    @agent
    def gardener(self) -> Agent:
        return GardenerAgent(llm=llm, verbose=False, save_backstory=True)

    @agent
    def poet(self) -> Agent:
        return PoetAgent(llm=llm_poet, verbose=False, save_backstory=True)

    @agent
    def psychologist(self) -> Agent:
        return PsychologistAgent(llm=llm, verbose=False, save_backstory=True)

    @agent
    def architect(self) -> Agent:
        return ArchitectAgent(llm=llm, verbose=False, save_backstory=True)

    @agent
    def editor(self) -> Agent:
        return EditorAgent(llm=llm, verbose=False, save_backstory=True)

    @agent
    def sentinel(self) -> Agent:
        return SentinelAgent(llm=llm, verbose=False, save_backstory=True)

    if EVALUATE:

        @agent
        def evaluator(self) -> Agent:
            return EvaluatorAgent(llm=llm, verbose=False, save_backstory=True)

    if INCLUDE_CRITIC_AND_PUBLISHER:

        @agent
        def critic(self) -> Agent:
            return CriticAgent(llm=llm, verbose=False, save_backstory=True)

        @agent
        def publisher(self) -> Agent:
            return PublisherAgent(
                llm=llm,
                tools=[PrintPoemAndReviewTool()],
                verbose=False,
                save_backstory=True,
            )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def create_concepts(self) -> Task:
        return MuseTask(
            task_name="create-concepts",
            agent=self.muse(),
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def sow_seeds(self) -> Task:
        return GardenerTask(
            agent=self.gardener(),
            task_name="sow-seeds",
            context=[self.create_concepts()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def write_poem(self) -> Task:
        return PoetTask(
            agent=self.poet(),
            task_name="write-poem",
            context=[self.sow_seeds()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def psychoanalyse_poem_not(self) -> Task:
        return PsychologistTask(
            agent=self.psychologist(),
            task_name="psychoanalyse-poem-not",
            context=[self.write_poem()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def architect_poem_not(self) -> Task:
        return ArchitectTask(
            agent=self.architect(),
            task_name="architect-poem-not",
            context=[self.psychoanalyse_poem_not()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def edit_poem_not(self) -> Task:
        return EditorTask(
            agent=self.editor(),
            task_name="edit-poem-not",
            context=[self.architect_poem_not()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def screen_poem_not(self) -> Task:
        return SentinelTask(
            agent=self.sentinel(),
            task_name="screen-poem-not",
            context=[self.edit_poem_not()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def revise_poem_not(self) -> Task:
        return PoetTask(
            agent=self.poet(),
            task_name="revise-poem-not",
            context=[self.edit_poem_not()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    if EVALUATE:

        @task
        def evaluate_poem_not(self) -> Task:
            return EvaluatorTask(
                agent=self.evaluator(),
                task_name="evaluate-poem-not",
                context=[self.write_poem(), self.revise_poem_not()],
                callback=self.write_output_as_json,
                save_description=True,
            )

    @task
    def psychoanalyse_poem_one(self) -> Task:
        return PsychologistTask(
            agent=self.psychologist(),
            task_name="psychoanalyse-poem-one",
            context=[self.revise_poem_not()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def architect_poem_one(self) -> Task:
        return ArchitectTask(
            agent=self.architect(),
            task_name="architect-poem-one",
            context=[self.psychoanalyse_poem_one()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def edit_poem_one(self) -> Task:
        return EditorTask(
            agent=self.editor(),
            task_name="edit-poem-one",
            context=[self.architect_poem_one()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def screen_poem_one(self) -> Task:
        return SentinelTask(
            agent=self.sentinel(),
            task_name="screen-poem-one",
            context=[self.edit_poem_one()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def revise_poem_one(self) -> Task:
        return PoetTask(
            agent=self.poet(),
            task_name="revise-poem-one",
            context=[self.edit_poem_one()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    if EVALUATE:

        @task
        def evaluate_poem_one(self) -> Task:
            return EvaluatorTask(
                agent=self.evaluator(),
                task_name="evaluate-poem-one",
                context=[self.revise_poem_not(), self.revise_poem_one()],
                callback=self.write_output_as_json,
                save_description=True,
            )

    @task
    def psychoanalyse_poem_two(self) -> Task:
        return PsychologistTask(
            agent=self.psychologist(),
            task_name="psychoanalyse-poem-two",
            context=[self.revise_poem_one()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def architect_poem_two(self) -> Task:
        return ArchitectTask(
            agent=self.architect(),
            task_name="architect-poem-two",
            context=[self.psychoanalyse_poem_two()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def edit_poem_two(self) -> Task:
        return EditorTask(
            agent=self.editor(),
            task_name="edit-poem-two",
            context=[self.architect_poem_two()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def screen_poem_two(self) -> Task:
        return SentinelTask(
            agent=self.sentinel(),
            task_name="screen-poem-two",
            context=[self.edit_poem_two()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def revise_poem_two(self) -> Task:
        return PoetTask(
            agent=self.poet(),
            task_name="revise-poem-two",
            context=[self.edit_poem_two()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    if EVALUATE:

        @task
        def evaluate_poem_two(self) -> Task:
            return EvaluatorTask(
                agent=self.evaluator(),
                task_name="evaluate-poem-two",
                context=[self.revise_poem_one(), self.revise_poem_two()],
                callback=self.write_output_as_json,
                save_description=True,
            )

    @task
    def psychoanalyse_poem_three(self) -> Task:
        return PsychologistTask(
            agent=self.psychologist(),
            task_name="psychoanalyse-poem-three",
            context=[self.revise_poem_two()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def architect_poem_three(self) -> Task:
        return ArchitectTask(
            agent=self.architect(),
            task_name="architect-poem-three",
            context=[self.psychoanalyse_poem_three()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def edit_poem_three(self) -> Task:
        return EditorTask(
            agent=self.editor(),
            task_name="edit-poem-three",
            context=[self.architect_poem_three()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def screen_poem_three(self) -> Task:
        return SentinelTask(
            agent=self.sentinel(),
            task_name="screen-poem-three",
            context=[self.edit_poem_three()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    @task
    def finalise_poem(self) -> Task:
        return PoetTask(
            agent=self.poet(),
            task_name="finalise-poem",
            context=[self.edit_poem_three()],
            callback=self.write_output_as_json,
            save_description=True,
        )

    if EVALUATE:

        @task
        def evaluate_poem_three(self) -> Task:
            return EvaluatorTask(
                agent=self.evaluator(),
                task_name="evaluate-poem-three",
                context=[self.revise_poem_two(), self.finalise_poem()],
                callback=self.write_output_as_json,
                save_description=True,
            )

        @task
        def evaluate_poem(self) -> Task:
            return EvaluatorTask(
                agent=self.evaluator(),
                task_name="evaluate-poem",
                context=[self.write_poem(), self.finalise_poem()],
                callback=self.write_output_as_json,
                save_description=True,
            )

    if INCLUDE_CRITIC_AND_PUBLISHER:

        @task
        def review_poem(self) -> Task:
            return CriticTask(
                agent=self.critic(),
                task_name="review-poem",
                context=[self.finalise_poem()],
                callback=self.write_output_as_json,
            )

        @task
        def publish_poem(self) -> Task:
            return PublisherTask(
                agent=self.publisher(),
                task_name="publish-poem-and-review",
                context=[self.finalise_poem(), self.review_poem()],
                callback=self.write_output_as_json,
            )

    @crew
    def crew(self) -> Crew:
        """Creates the CrewAIPoetryCrew crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            # tools=self.tools,
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )

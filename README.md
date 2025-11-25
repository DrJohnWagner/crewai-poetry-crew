# CrewaiPoetryCrew Crew

Welcome to the CrewaiPoetryCrew Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/crewai_poetry_crew/config/agents.yaml` to define your agents
- Modify `src/crewai_poetry_crew/config/tasks.yaml` to define your tasks
- Modify `src/crewai_poetry_crew/crew.py` to add your own logic, tools and specific args
- Modify `src/crewai_poetry_crew/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the crewai-poetry-crew Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Pompts

### **The Prompt: The Unopened Message**

**Part 1: The Core Idea**

Write a poem addressed to a message you will never send, and to the person who will never receive it.

This message could be:
*   A text typed out and then deleted.
*   A letter written and then burned or hidden in a book.
*   An email saved in the "Drafts" folder for years.
*   Words whispered to a photograph.
*   A confession spoken to an empty chair.

**Part 2: The Sensory & Emotional Scaffolding (Guiding Questions)**

To help the poet build the world of the poem, ask them to consider:

*   **The Medium:** *Where* does this unsent message live? Is it on a cracked phone screen, a piece of stationery that smells of dust, the steam on a bathroom mirror? How does the physical (or digital) nature of the medium influence the tone?
*   **The Content:** What is the *one true thing* the message needs to say? Is it an apology, a confession of love, a secret, a curse, a question you're finally brave enough to ask? Don't write the whole message—hint at its core weight.
*   **The Silence:** Why *can't* it be sent? Is the person gone, unreachable, dangerous, or would sending it break a fragile peace? The power of the poem lives in this silence. Explore the weight of what is held back.
*   **The Body:** Where in your body do you feel the weight of this unsent message? (e.g., a knot in the throat, a hollow in the chest, a tremor in the hands). Connect the abstract emotion to a physical sensation.
*   **A Metaphor:** Compare the unsent message to an object. Is it "a stone in my pocket," "a seed with no soil," "a lighthouse beam pointing at a shore that sank into the sea"?

**Part 3: The Optional Formal Constraint (To push creativity)**

*   **Option A (Structure):** Write the poem in two stanzas. The first stanza describes the *message and the medium*. The second stanza describes the *silence and the consequence*.
*   **Option B (Sound):** Use the sound of a word related to your message (e.g., "static," "echo," "stillness," "crackle") to influence the poem's rhythm and use of alliteration/assonance.
*   **Option C (Free Form):** Ignore constraints and let the poem find its own necessary shape.

---

### **Why This Prompt is So Effective:**

*   **High Stakes, Low Risk:** It immediately taps into universal human experiences of regret, longing, unresolved conflict, and unexpressed love. Every student will have *something* to draw from, even if they fictionalize it.
*   **Inherent Tension:** The core idea is built on the conflict between the urge to communicate and the necessity of silence. This is the engine of poetry.
*   **Rich Imagery:** It naturally leads to powerful, concrete images (the draft folder, the burning letter, the empty chair) that ground the abstract emotions.
*   **Focus on the Addressee:** The poem has a built-in "you," creating an intimate, confessional tone that can be very powerful.
*   **Open to Interpretation:** The "message" can be to a lost parent, a former lover, a childhood self, a political figure, or even a pet. It is infinitely adaptable.

### **Example Lines to Seed Ideas:**

> "Your name is a knot I can't untie in my chest."
>
> "I have composed the message to you on the inside of my eyelids."
>
> "This text is a paper boat I will never set on the river of your attention."
>
> "The draft folder is a museum of my courage, and every exhibit is closed."

This prompt invites vulnerability and honesty while providing enough structure to prevent the writer from feeling lost in the vastness of the emotion. It should lead to a class of strikingly different, deeply personal, and powerful poems.

## Understanding Your Crew

The crewai-poetry-crew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the CrewaiPoetryCrew Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.

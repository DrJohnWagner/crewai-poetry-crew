## 3. System Overview

> “I can tell already you think I’m the dragon, that would be so like me, but I’m not.  
> I’m not the dragon. I’m not the princess either.”  
> — Richard Siken, *Litany in Which Certain Things Are Crossed Out*

The seven-agent pipeline is not a workflow.  
It is a **computational organism** designed to express, deform, and re-stabilize poetic identity across recursive rounds. This section presents the system *as a system*: its architecture, its internal dynamics, its control parameters, and the conceptual logic that allows it to behave like a multi-agent ecology rather than a linear sequence of prompts.

The opening epigraph is not decorative.  
It captures the core logic of system design: **identity is defined not only by what is expressed, but by what is excluded**. A system remains stable when each component *refuses* the roles that belong to others. The Poet is not the Architect; the Architect is not the Editor; the Editor is not the Critic; no agent becomes the dragon or the princess. Their constraints remain intact. Their refusals keep the ecosystem coherent.

Section 3 therefore explains:

- the system’s architecture as a conceptual object,  
- why it must be multi-agent,  
- how recursive rounds function as the core unit of poetic computation,  
- how distributed genotype becomes distributed behavior,  
- how personas serve as configurable identities, and  
- how the ecology produces the conditions for emergence.

Section 4 will elaborate the behavior of each agent.  
Here we describe the system as a whole.

---

### 3.1 The Seven-Agent Pipeline as a Computational Ecology

The system contains seven agents:

1. **Muse**  
2. **Summariser**  
3. **Poet**  
4. **Architect**  
5. **Editor**  
6. **Critic**  
7. **Publisher**

Each agent is a **stable genotype**: a persistent identity with its own constraints, refusal logic, and domain of responsibility. What changes across rounds is not their identity but their **phenotype**—the specific behavior expressed under the pressures applied by other agents.

The pipeline is built to enforce *structured interference* between agents.  
The agents do not negotiate. They do not collaborate.  
But they are wired so that:

- the output of one becomes the pressure input of the next,  
- constraints accumulate but do not homogenize,  
- and each stage introduces transformations the previous stage could not produce on its own.

The system is therefore an ecology of **competing invariants**, not consensus formation.  
Each agent speaks from a different interior law; the system works because their laws collide.

---

### 3.2 Why a Multi-Agent System Is Architecturally Necessary

A single-agent poem generator—even a large, powerful one—cannot sustain recursive deformation across multiple drafts without:

- drift into non-persona behavior,  
- loss of architectural coherence,  
- internal contradiction resolution,  
- prompt overwriting,  
- or increasing brittleness under pressure.

In human poets, internal contradiction is a source of power.  
In LLMs, it is a source of collapse—unless we distribute it.

The pipeline distributes interior functions across agents so that:

- the **Muse** produces conceptual heat without structural responsibility,  
- the **Summariser** condenses and stabilizes thematic vectors,  
- the **Poet** generates emotional physics,  
- the **Architect** reshapes breath and spatial fracture,  
- the **Editor** escalates pressure,  
- the **Critic** evaluates global coherence and drift,  
- the **Publisher** consolidates and frames the emergent work.

This makes the system capable of handling the kind of multi-round, multi-pressure behavior that human poets perform internally but LLMs cannot sustain in a single invocation.

The multi-agent architecture is therefore not decorative.  
It is a **computational requirement** for simulating recursive poetic identity.

---

### 3.2.1 Personas as Configurable Agent-Level Genotypes

Personas in this system are not literary decorations; they are **configurable genotypes** that define the interior laws governing each agent’s behavior. From a design standpoint, personas are deliberately engineered to be:

- **modular** — each persona is a self-contained identity package,  
- **extensible** — new personas can be added without architectural changes,  
- **swappable** — an agent can adopt a different persona simply by loading a different genotype,  
- **combinable** — multiple personas can be compared or hybridized across runs,  
- **transparent** — every constraint is explicit and inspectable.

Although these personas are maintained externally, their conceptual role is architectural: each persona is a **constraint membrane** that defines what an agent must do, what it can do, and what it will not do under any circumstances.

#### Personas Must Be System-Prompt Genotypes  
A persona cannot be embedded in a task instruction.  
Task prompts shape *phenotype*—the specific behavior expressed in context.  
Personas define *genotype*—the identity that governs all possible behaviors.

For this reason, personas appear **only** in system prompts, where they specify the three components of a genotypic identity:

1. **Interior physics**  
   The emotional or conceptual laws the agent must obey.

2. **Refusal logic**  
   Boundaries the agent never crosses.

3. **Identity invariants**  
   Persistent features that remain stable across rounds, drift, temperature changes, and recursive pressure.

These features define the *persistent self* of each agent.

#### Phenotypes Are Currently Persona-Independent  
In the present design, **phenotypes are not tied to any specific persona-genotype**.  
They are intentionally engineered as **generic task behaviors**—domain-general transformations that each agent performs *regardless* of which persona is loaded.

This design choice ensures:

- **clean separation of concerns** (identity vs. action),  
- **persona-agnostic system behavior**,  
- **consistent architectural scaffolding**, and  
- **controlled comparisons** across different literary or experimental identities.

In effect, **phenotypes provide the scaffolding**,  
and **personas provide the interior physics that animate that scaffolding differently**.

The result is a system where:

- the architecture stays fixed,  
- the tasks are stable,  
- and only identity changes—  
allowing for controlled, scientifically interpretable comparisons across personas.

---

### 3.2.2 Implementation Note: Why CrewAI

Although this paper emphasizes conceptual architecture rather than software tooling, the system’s behavior depends on a framework capable of orchestrating **persistent, identity-bound agents** across recursive rounds. We use **CrewAI** because it provides a stable and transparent mechanism for maintaining system-prompt genotypes, dispatching task-prompt phenotypes, and passing artifacts cleanly between agents. CrewAI does not determine the content or style of the poems; it determines the *ordering*, *isolation*, and *interaction pattern* of the agents. Its role is architectural: ensuring that each agent acts with its own stable identity, that outputs become pressure-inputs for subsequent agents, and that recursive rounds proceed without prompt leakage or role collapse. In short, CrewAI provides the scaffolding required for the multi-agent ecology described in this section.

---

### 3.3 Recursive Rounds as the Fundamental Unit of Computation

The system operates in **two rounds** in the case study and can support additional rounds if desired. Each round contains:

1. **Generation** (Poet)  
2. **Structural deformation** (Architect)  
3. **Pressure escalation** (Editor)  
4. **Evaluation** (Critic)  
5. **Consolidation** (Publisher)

A round is not a pass.  
It is a **cycle of deformation**, in which the poem is not improved linearly but stressed, bent, fractured, and re-articulated. Each round:

- preserves genotype-level constraints,  
- expresses new phenotypic behavior,  
- accumulates structural decisions,  
- and creates the conditions for the next deformation.

The system behaves less like a pipeline and more like a **feedback loop**.  
Identity is not fixed; it is maintained under pressure.

---

### 3.4 Constraint Flow and the Preservation of Tension

The system is designed so that no agent can completely overwrite another.  
This is essential. If any stage had the power to “fix” the output of the previous stage, the system would collapse into generic behavior.

Instead, each agent contributes *directional force*:

- The **Poet** introduces emotional velocity and recursion.  
- The **Architect** introduces spatial instability and fracture.  
- The **Editor** introduces heat, escalation, and refusal.  
- The **Critic** introduces global coherence constraints.

These forces accumulate without resolving one another.  
The computational analogy is not “refinement” but **vector addition under tension**.

The system remains coherent because the Summariser and Publisher provide periodic normalization: one at the beginning of each round, one at the end.

This is the “litany of things not crossed out.”  
The poem moves forward because many pressures remain active, unresolved, and alive.

---

### 3.5 Drift, Stability, and the Role of Controlled Instability

As established in Section 2.3, instability is not merely tolerated—it is sometimes instrumented. Temperature, round count, and agent wiring allow the system to:

- modulate drift,  
- stress-test identity invariants,  
- explore deformation pathways,  
- and examine how computational identity behaves under duress.

Without the capacity to enter and exit instability, the multi-agent ecology would generate only safe, predictable poems.  
Pressure must be engineered.

---

### 3.6 From System Overview to Agent Analysis

Section 3 has now established the pipeline as:

- a multi-agent ecology,  
- a system of distributed genotype,  
- a recursive deformation engine,  
- and a computational organism capable of emergent poetic behavior.

Section 4 will examine each agent in detail—its genotype, its task phenotype, its refusal logic, its structural or emotional responsibilities, and its role in shaping the emergent poem.  
This is where the system’s conceptual architecture becomes an operational blueprint.

---
# Multi-Agent Poetic Generation: A Case Study in Emergent Recursive Behavior  
*Draft — 2025*  

---

## Table of Contents
1. **Motivation**  
2. **Persona Selection and Rationale**  
    - 2.1 Why Richard Siken?  
    - 2.2 Why not alternative personas (e.g., Frost)?  
    - 2.3 Genotype vs Phenotype in poetic modeling  
3. **System Overview (“Litany of Things Not Crossed Out”)**  
## 4. Architectural and Behavioral Analysis of the Seven-Agent System
    - 4.1 Overview of the Seven-Agent System  
    - 4.2 The Poet  
    - 4.3 The Architect  
    - 4.4 The Editor  
    - 4.5 Division of Labor and Conflict Dynamics  
5. **The Run (Case Evidence)**  
    - 5.1 The three seeds (options presented to the Poet)  
    - 5.2 Consciously choosing Seed #3  
    - 5.3 The contamination of Seed #2  
    - 5.4 Round 1: Poet → Architect → Editor → Poet  
        - 5.4.1 Poet’s first draft (V0)  
        - 5.4.2 Architect’s Round 1 revision (V1)  
        - 5.4.3 Editor’s Round 1 suggestions  
        - 5.4.4 Poet’s Round 1 revision (V2)  
    - 5.5 Round 2: Poet → Architect → Editor → Poet  
        - 5.5.1 Architect’s Round 2 stabilization (V3)  
        - 5.5.2 Editor’s Round 2 suggestions  
        - 5.5.3 Poet’s final round revision (V4)  
    - 5.6 Structural and Stylistic Evolution Across Rounds  
        - 5.6.1 Emergence of recursive echo architecture  
        - 5.6.2 Breath-pattern intensification  
        - 5.6.3 Indentation and spatial stabilization  
        - 5.6.4 Contamination dynamics (Seed #2 bleed-through)  
        - 5.6.5 Emergence of the “horizon.” boundary-collapse  
6. **Results (“Saying Your Names”)**  
7. **Discussion (“1001 Things to Discuss”)**
8. **Future Work**
9. **Conclusion**  
**Appendix A: Poet Artefacts**  
    - A.1 Full Poem Versions  
        - V0: Poet Initial Draft (Complete)  
        - V1: Architect Round 1 Revision (Complete)  
        - V2: Poet Recursive Expansion (Complete)  
        - V3: Architect Round 2 Stabilization (Complete)  
        - V4: Poet Final Recursive Intensification (Complete)  
    - A.2 Version Comparisons (Diffs)  
        - A.2.1 Diff: V0 → V1  
        - A.2.2 Diff: V1 → V2  
        - A.2.3 Diff: V2 → V3  
        - A.2.4 Diff: V3 → V4  
    - A.3 Poet Notes and Decisions  
    - A.4 Seeds Passed to the Poet  
**Appendix B: Architect Artefacts**  
    - B.1 Architect Notes (Round 1)  
    - B.2 Architect Revision Output (Round 1)  
    - B.3 Architect Notes (Round 2)  
    - B.4 Architect Revision Output (Round 2)  
    - B.5 Formatting & Indentation Repairs  
**Apendix C: Editor Artefacts**  
    - C.1 Editor Notes (Round 1)  
    - C.2 Poet Response to Editor (Round 1)  
    - C.3 Editor Notes (Round 2)  
    - C.4 Poet Response to Editor (Round 2)  
**Appendix D: System Logs**  
    - D.1 Logger log excerpts  
    - D.2 Stdout log excerpts  
    - D.3 Log Commentary  
**Appendix E: Agent Prompts, Tasks, & Global Constraints**  
    - E.1 System-Wide Instructions and Constraints  
        - E.1.1 No-Meta Rules  
        - E.1.2 Global Guardrails  
        - E.1.3 Universal Section Format  
        - E.1.4 Tool Usage Rules  
    - E.2 Agent and Task Descriptions & Prompts (Pipeline Order)  
        - E.2.1 Muse  
        - E.2.2 Summariser  
        - E.2.3 Poet  
        - E.2.4 Architect  
        - E.2.5 Editor  
        - E.2.6 Critic  
        - E.2.7 Publisher  
    - E.3 Pipeline-Level Implementation Notes (Minimal Stub)
**Appendix F: Breath, Rhythm, and Spatial Architecture**  
    - F.1 Overview and Motivation  
    - F.2 Breath as Structural Constraint  
        - F.2.1 Breath Units  
        - F.2.2 Breath-Based Lineation  
        - F.2.3 Breath Collapse  
    - F.3 Indentation as Semantic Function  
        - F.3.1 Indentation as Meaning  
        - F.3.2 Indentation as Recursion Marker  
        - F.3.3 Indentation as Temporal Stagger  
        - F.3.4 Indentation as Emotional Fracture  
        - F.3.5 Indentation as Structural Closure Agent  
    - F.4 Recursion Mechanics in Poetic Form  
        - F.4.1 Recursive Echo Layers  
        - F.4.2 Recursive Symmetry  
        - F.4.3 Recursive Misalignment  
    - F.5 Line-Breaking and Its Cognitive Effects  
        - F.5.1 Line-Break Types  
        - F.5.2 End-Stops, Caesurae, and Terminal Points  
        - F.5.3 Emotional Weight and Line-Length  
        - F.5.4 Breath-Based Pacing  
        - F.5.5 Line-Break as Semantic Boundary  
        - F.5.6 Line-Break Sequencing as Meaning-Making  
    - F.6 The Architect’s Role in Enforcing Breath-Architecture  
        - F.6.1 Repairing Failed Recursion  
        - F.6.2 Ensuring Indentation Symmetry  
        - F.6.3 Preventing Structural Drift  
        - F.6.4 Enabling Controlled Collapse  
        - F.6.5 Summary: Why the Architect Matters  
    - F.7 Siken’s Genotype: A Formal Analysis  
        - F.7.1 Phenotype vs. Genotype  
        - F.7.2 Recursive Torque as a Genetic Marker  
        - F.7.3 Interruptive Logic and Emotional Velocity  
        - F.7.4 Structural Self-Contradiction as Drive  
        - F.7.5 Emergent Genotype Assimilation Across Versions  
    - F.8 Comparative Architectural Modes  
        - F.8.1 Frost-Linearity  
        - F.8.2 Glück-Distillation  
        - F.8.3 Vuong-Ellipticity  
        - F.8.4 No-Architect Mode  
        - F.8.5 No-Editor Mode  
        - F.8.6 Summary of Cross-Mode Behaviors  
    - F.9 Implications for Machine-Generated Poetics  
        - F.9.1 Agent Interdependence as a Generative Force  
        - F.9.2 Architectural Pressure as Machine-Literary Style  
        - F.9.3 Recursion as Aesthetic Memory  
        - F.9.4 The Paradox of Productive Interference  
        - F.9.5 Reframing Poetics: From Output to Behavior  
        - F.9.6 Implications for Computational Creativity Research  
        - F.9.7 Future Directions  
        - F.9.8 Conclusion
**Appendix H: Vocabulary of Architectural, Poetic, and Redline Terms**
    - (includes taxonomy of structure, recursion, breath-logic, indentation semantics)  

---

# 1. Motivation
*(To be drafted…)*

---

# 2. Persona Selection and Rationale

## 2.1 Why Richard Siken?
*(To be drafted…)*

## 2.2 Why not alternative personas (e.g., Frost)?
*(To be drafted…)*

## 2.3 Genotype vs Phenotype in poetic modeling
*(To be drafted…)*

---

# 3. System Overview (“Litany of Things Not Crossed Out”)
*(High-level description of the pipeline; to be drafted…)*

---

## 4. Architectural and Behavioral Analysis of the Seven-Agent System

## Section 4 Epigraph (for the whole architecture)

> **“In the end, it’s all collisions. Everything is collisions.”**  
> — Richard Siken, *Crush*

Section 4 provides the conceptual architecture for the seven-agent system. Where Appendix E
documents implementation details, this section describes the *behavioral ecology* of the
agents: how they operate, how they interfere with one another, how responsibility is
divided, and how the pipeline produces poetic structure through controlled constraint.
Throughout, we adopt the architectural vocabulary established in Appendix F—breath,
recursion, spatial logic, rupture, drift—to understand agents not as software modules but
as forces acting on a text.

The agents are best understood as **genotypes**: stable identities, constraints, and
permissions governing what transformations they can perform. Tasks then function as
**phenotypes**: specific contextualized behaviors enacted under round-specific pressures.
A single agent may therefore appear multiple times in the pipeline under different tasks,
expressing the same identity through different operational goals. *The architecture
therefore separates **who an agent is** from **what an agent does**, and thus from **what
is enacted—phenotypically and irreversibly—within the pipeline itself***.

This separation between agent-identity (system prompt) and task-action (task prompt) is
essential to preserving clear lines of responsibility and enabling fine-grained analysis of
the poem’s evolution.

---

## 4.1 Overview of the Seven-Agent System

### 4.1 Epigraph

> **“You can’t have an experience with the world and not be changed by it.”**  
> — Richard Siken, *War of the Foxes*

The full system comprises seven agents—stable genotypes—but the pipeline itself is executed
as a **fixed, irreversible sequence of tasks**. Tasks are the operational phenotypes: the
moments where an agent’s identity becomes behavior. Each task applies a distinct axis of
pressure—associative, conceptual, expressive, structural, evaluative, or curatorial—and the
ordered collision of these pressures forms the dynamical substrate from which the poem
emerges.

1. **Muse-task** – expands the associative and emotional terrain.  
2. **Summariser-task** – compresses that terrain into a coherent poetic intention.  
3. **Poet-task** – expands intention into language under persona grammar.  
4. **Architect-task** – imposes spatial, structural, and rhythmic order.  
5. **Editor-task** – applies semantic pressure and identifies load-bearing faults.  
6. **Critic-task** – evaluates coherence, persona fidelity, and structural integrity.  
7. **Publisher-task** – renders, formats, and finalizes the artifact.

Agents do not negotiate. They do not share state. They remain strictly isolated as
genotypic identities. The **sequence of tasks**, however, *does* collaborate: collaboration
emerges architecturally through ordered transformations, division of labor, and
irreversible wiring. The pipeline is the collaborator; tasks are the mechanism; agents are
the identities those tasks embody.

The poem evolves through **structured interference**—the controlled collision of task-level
pressures. Interference introduces drift, correction, recursion, stabilization, and
occasionally collapse. What emerges is not the vision of any one agent but the **trajectory
of deformations** produced as each task receives, transforms, and relinquishes the
artifact. That trajectory constitutes the poem’s architecture.

---

## 4.2 The Poet

### 4.2 The Poet — Epigraph

> **“Tell me how all this, and love too, will ruin us.”**  
> — Richard Siken, *Crush*

The Poet is the system’s generative heart: the only agent permitted to modify lexical
content. Its persona prompt defines its **genotype**—a stable grammar of breath,
metaphorics, cadence, and interior logic associated with a specific poetic voice (e.g.,
Siken, Rilke, Frost). When a Poet-task is invoked (`task_write`, `task_revise`,
`task_finalise`), this genotype expresses a **phenotype** appropriate to the local
constraints of the round.

**Responsibilities of the Poet:**

- translating the Summariser’s intention into a first draft;  
- performing recursive elaboration or intensification during revision rounds;  
- absorbing Editor pressure without violating persona boundaries;  
- preserving emotional coherence across rounds.

The Poet is the source of **semantic mutation**—new images, rearrangements, shifts in
emotional architecture. But mutation occurs inside a membrane of constraint: persona
grammar stabilizes drift and ensures continuity of voice across rounds. The Poet thus
embodies the core tension between expressive freedom and structural obligation.

---

## 4.3 The Architect

### 4.3 The Architect — Epigraph

> **“You go forward. You repeat yourself.  
> You go forward. You repeat yourself.”**  
> — Richard Siken, *Crush*

The Architect performs all **structural** and **spatial** transformations. It cannot alter a
single word. Its genotype forbids lexical mutation but authorizes modifications of breath,
indentation, recursive planes, echo fragments, and rupture mechanics.

Architect-tasks (`task_architect_one`, `task_architect_two`) express phenotype in distinct
ways:

- Round 1 typically generates the base architectural signature—indentation logic, breath
  spacing, echo scaffolding.  
- Round 2 stabilizes recursive drift, resolves asymmetry, and reasserts spatial intent.

**Responsibilities of the Architect:**

- shaping the poem’s spatial rhythm;  
- enforcing or intentionally breaking indentation symmetry;  
- articulating controlled rupture (line breaks, breath fractures);  
- deepening echo fragments and recursive structures;  
- maintaining architectural coherence across rounds.

The Architect does not “format.” It creates *pressure*. By altering the reader’s breath and
visual traversal, it reconfigures emotional pacing without altering meaning. This strict
division—semantic mutation for the Poet, structural authority for the Architect—is the
engine of the system’s expressive power.

---

## 4.4 The Editor

### 4.4 The Editor — Epigraph

> **“Tell me again how the story goes.  
> Make it mean something this time.”**  
> — Richard Siken, *Crush*

The Editor introduces **semantic and emotional pressure** through commentary alone. Its
genotype forbids rewriting or drafting; its phenotype manifests exclusively as *notes*.
The Editor is an agent of interpretive disruption: it identifies tensions, amplifies
unresolved motifs, and proposes recursions or intensities.

Editor-tasks (`task_edit_one`, `task_edit_two`) operate as follows:

- Round 1 pushes the initial architectural draft toward emotional coherence.  
- Round 2 pushes against structural decisions, often refracting earlier motifs into new
  tensions.

**Responsibilities of the Editor:**

- surfacing latent emotional collisions;  
- proposing recursion shifts (increase, collapse, variation);  
- amplifying structural or imagistic repetition created by the Architect;  
- challenging the Poet’s choices without enforcing corrections.

The Editor applies **semantic redlines**, but they remain advisory. The Poet may absorb,
refuse, or reinterpret them. The Architect’s prior interventions may even render some notes
structurally unachievable. This irreversible, non-negotiated dynamic is not a flaw; it is a
core design principle of the pipeline.

---

## 4.5 Division of Labor and Conflict Dynamics

### 4.5 Epigraph

> **“You’re in a car with a beautiful boy, and he won’t tell you that he loves you,  
>  but he loves you.”**  
> — Richard Siken, *Crush*

Each agent governs a distinct jurisdiction—semantic generation (Poet), structural
enforcement (Architect), and semantic pressure via commentary (Editor). These jurisdictions
do not overlap; they do not harmonize. They *interfere*. The poem emerges not through
consensus but through a choreography of constraints, each agent inheriting a problem it did
not choose and transforming it under rules it cannot break.

Three forms of tension structure this interference:

1. **Cross-domain redlining**  
   Each agent’s intervention reshapes the interpretive field for those downstream.  
   - The Architect’s spatial decisions alter how the Poet can respond to Editor notes.  
   - Editor notes provoke semantic shifts that may disrupt or recontextualize prior
     architectural intent.  
   - The Poet’s expansions introduce conceptual drift that propagates into structural
     transformations the Architect must later constrain.  

   These redlines are not negotiated; they are inherited. Nothing aligns by design;
   alignment is emergent and fragile.

2. **Genotype/phenotype bifurcation**  
   Agents maintain stable identities, but tasks instantiate behavior under
   round-specific pressure. These phenotypes accumulate drift, stabilization, recursion, and
   collapse across rounds. The same agent may act differently under different tasks—not
   because its identity changes, but because the *artifact* it receives has changed in ways
   it cannot predict. Identity remains fixed; behavior adapts.

3. **Asymmetric irreversibility**  
   Each transformation is final within the pipeline.  
   - The Architect cannot repair semantic misalignment introduced by the Poet.  
   - The Poet cannot reimagine structural forms established by the Architect.  
   - The Editor cannot restore recursion lost upstream or undo spatial collapse.  
   Once a pressure is exerted, it becomes geological: a layer of the poem’s sediment.  
   The pipeline always moves forward; nothing moves backward.

---

### **Feedback Loop Dynamics: Poet–Editor Conflict**

A distinctive feature of the system is the **feedback conflict** between the Editor and the
Poet. The Editor cannot modify the poem directly; its genotype forbids rewriting. It can
only issue *notes*: semantic pressures, challenges, intensifications, and interpretive
provocations. The Poet, however, is the only agent capable of **lexical mutation**—the
sole agent with the authority to implement or refuse those pressures.

This creates a **positive–negative feedback loop**:

- **Positive feedback** occurs when the Poet accepts an Editor note that deepens persona
  grammar, enhances emotional coherence, or strengthens recursive structure. The Editor’s
  pressure amplifies the poem’s momentum; the Poet incorporates and elaborates.

- **Negative feedback** occurs when the Poet rejects an Editor suggestion that would
  violate persona boundaries, distort metaphysical logic, or collapse interior voice. The
  Poet’s refusal preserves identity against the Editor’s pressure.

The system is explicitly designed to support **aggression on both sides**:  
- The Editor may issue sharp, ambitious, even adversarial notes.  
- The Poet may protect its persona with equal intensity, rejecting anything that threatens
  its grammar of self.  

But the Poet also faces architectural pressure to *improve* the poem. A Poet that ignores
all notes produces stagnation; a Poet that accepts everything risks persona collapse. The
system’s equilibrium emerges from the **Poet’s selective uptake**: the continual weighing
of semantic pressure against persona integrity.

This feedback loop is neither cooperative nor purely adversarial. It is **regulated
conflict**—a structural mechanism that forces the poem toward sharper articulation while
preserving voice, identity, and internal coherence.

---

These intertwined tensions generate what Appendix F terms **architectural pressure** and
what Appendix G terms **redline dynamics**—the structural and semantic forces that shape,
constrain, and destabilize the poem across rounds. The final artifact is not a resolution
of these tensions but the **record of their collisions**: a trajectory of deformations made
legible as poetic form.

---

# 5. The Run (Case Evidence)
*(To be drafted…)*

## 5.1 The three seeds (options presented to the Poet)
*(To be drafted…)*

## 5.2 Consciously choosing Seed #3
*(To be drafted…)*

## 5.3 The contamination of Seed #2
*(To be drafted…)*

## 5.4 Round 1: Poet → Architect → Editor → Poet
*(To be drafted…)*
### 5.4.1 Poet’s first draft (implicit within Seed #3)
*(To be drafted…)*
### 5.4.2 Architect’s Round 1 revision (V1)
*(To be drafted…)*
### 5.4.3 Editor’s Round 1 suggestions
*(To be drafted…)*
### 5.4.4 Poet’s Round 1 revision (V2)
*(To be drafted…)*

## 5.5 Round 2: Poet → Architect → Editor → Poet
*(To be drafted…)*
### 5.5.1 Architect’s Round 2 stabilization (V3)
*(To be drafted…)*
### 5.5.2 Editor’s Round 2 suggestions
*(To be drafted…)*
### 5.5.3 Poet’s final round revision (V4)
*(To be drafted…)*

## 5.6 Structural and Stylistic Evolution Across Rounds
*(To be drafted…)*
### 5.6.1 Emergence of recursive echo architecture
*(To be drafted…)*
### 5.6.2 Breath-pattern intensification
*(To be drafted…)*
### 5.6.3 Indentation and spatial stabilization
*(To be drafted…)*
### 5.6.4 Contamination dynamics (Seed #2 bleed-through)
*(To be drafted…)*
### 5.6.5 Emergence of the "horizon." boundary-collapse
*(To be drafted…)*

---

# 6. Results (“Saying Your Names”)
*(To be drafted…)*

---

# 7. Discussion (“1001 Things to Discuss”)
*(To be drafted…)*

---

# 8. Future Work

## Future Work

The case study highlights several limitations in the current multi-agent architecture that directly motivate avenues for future development. First, the Poet never responds to the Architect directly. All Poet revisions occur in a single recursive pass that merges pressures from both the Architect and the Editor. As a result, any attempt to recover which architectural constraints were accepted, resisted, or undone is necessarily inferential and often ambiguous. Future versions of the system should incorporate explicit diagnostic channels or provenance markers that allow the Poet to declare when an edit is in response to an architectural intervention, an editorial suggestion, or an internal persona-driven impulse. Such visibility would enable more precise reconstruction of agent influence and strengthen interpretability.

Second, because the Poet responds to the Architect and Editor simultaneously, their revisions conflate structural and semantic pressures. This entanglement obscures the true flow of influence within the pipeline. A promising direction for future work is the development of instrumentation or logging hooks that trace, in real time, which agent-originated signals the Poet is incorporating or rejecting. These diagnostics could take the form of edit-type metadata, structural diff tags, or explicit self-reporting from the Poet about constraint alignments during revision.

Third, we observe that the Editor frequently proposes structural or architectural modifications—despite this not being the Editor’s formal mandate. In the current system design, these suggestions belong neither to the Architect nor to the Poet and therefore enter the pipeline without a clear place to land. A more principled approach would allow the Poet to pass Editor-derived structural suggestions upstream to the Architect as candidate architectural modifications in the next iteration cycle. This would transform the Architect from a strictly top-down structural agent into a participant in a collaborative negotiation loop, better reflecting the reciprocal dynamics of real-world editorial practice.

Collectively, these directions suggest a richer, more transparent multi-agent system in which structural, semantic, and persona-driven pressures remain distinguishable, traceable, and intentionally negotiated. Implementing such enhancements would not only improve interpretability but would provide a framework for studying agent entanglement as an expressive force in machine-generated poetics.

---

# 9. Conclusion
*(To be drafted…)*

---

!include "Appendix.md"

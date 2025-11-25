## 4. Architectural and Behavioral Analysis of the Seven-Agent System

> **“In the end, it’s all collisions.
> Everything is collisions.”**
> — Richard Siken, *Crush*

Section 4 establishes the conceptual architecture of the seven-agent system. Where Appendix
E details implementation, Section 4 analyzes **behavior, identity, interference, and
pressure**—how each agent acts upon the poem, and how their sequential, irreversible
transformations produce emergent form.

We adopt the vocabulary of Appendix F—**breath, recursion, spatial logic, rupture,
drift**—to understand agents not as software modules but as **forces**. Each agent is a
**genotype** (stable identity and constraints), expressed through **tasks** as **phenotypes**
(contextual behaviors under round-specific pressures).

A crucial distinction guides this architecture:

- **The Muse, Summariser, Critic, and Publisher** do *not* participate in the core
  contested cycle. They provide emotional material, reduce it, evaluate the finished poem,
  or assemble the final artifact.
- **The Poet, Architect, and Editor** *do* participate in the contested cycle. Their
  transformations collide, interfere, and recursively deform the poem through pressure and
  resistance.

The pipeline enforces **architectural collaboration without negotiation**: agents remain
isolated, but tasks produce ordered, irreversible deformations. The poem is the trajectory
left by these collisions.

---

## 4.1 Overview of the Seven-Agent System

The system comprises seven agents—stable genotypes—but the pipeline operates through a
**fixed, irreversible sequence of tasks**. Tasks are the operational phenotypes: the
moments where identity becomes behavior. Each task applies a distinct axis of pressure:
associative, reductive, generative, structural, semantic, evaluative, or curatorial.

1. **Muse-task** – expands the emotional terrain into proto-worlds.
2. **Summariser-task** – compresses each proto-world into a distilled seed.
3. **Poet-task** – expands a seed into language under persona grammar.
4. **Architect-task** – imposes visual, spatial, and rhythmic structure.
5. **Editor-task** – applies semantic and emotional pressure through notes.
6. **Critic-task** – generates external literary evaluation.
7. **Publisher-task** – assembles and emits the final markdown artifact.

The agents do not negotiate or share memory. Collaboration emerges **architecturally**, as
the ordered wiring of tasks forces each agent to receive, transform, and relinquish the
artifact. The poem evolves through **structured interference**: drift, correction,
recursion, stabilization, collapse. No agent can undo the preceding agent’s deformation.

The poem is therefore not the product of a single intention but the **spatial trace of
compounded, asymmetric pressures**.

---

## 4.2 The Muse

> **“You want a better story. Who wouldn’t?”**
> — Richard Siken, *Crush*

The Muse is outside the system’s contested cycle. It performs no revision, receives no
pressure, and exerts no recursive force. Its function is generative but non-interactive:
the Muse produces **proto-emotional universes**—static fields of tension built around
distinct emotional arcs.

Its genotype is framed by its backstory: “You generate emotional universes, not plots.”The Muse must avoid chronology, causality, or narrative logic. Each CONCEPT in
`task_inspire` consists of:

- a charged emotional situation,
- a distinct emotional arc,
- minimal sensory or symbolic anchors,
- and a static pressure field without movement.

The Muse’s output constitutes the system’s **initial deformation energy**—raw emotional
potential awaiting reduction and transformation. Once emitted, the Muse withdraws from the
pipeline entirely.

---

## 4.3 The Summariser

> **“You were trying to tell me something,
> but I kept forgetting what it was.”**
> — Richard Siken, *Crush*

The Summariser, like the Muse, remains outside the contested cycle. It performs a single,
non-recursive act: compressing the Muse’s expansive emotional universes into compact
**poetic seeds**.

Its genotype is reductive: “extract only the essence.”The Summariser must **discard** everything that does not constitute emotional necessity:
no narrative sequence, no backstory, no causality, no interpretation. Its task,
`task_summarise`, yields three SEEDS composed only of:

- an emotional arc,
- indispensable anchors,
- and a minimal atmospheric field.

Where the Muse creates **breadth**, the Summariser creates **density**. It converts
associative emotional worlds into high-pressure briefs suitable for persona-driven
generation. After this reduction, it exits the pipeline and exerts no further influence.

---

## 4.4 The Poet

> **“Tell me how all this, and love too, will ruin us.”**  
> — Richard Siken, *Crush*

The Poet is the generative core of the system—the only agent permitted to mutate lexical
content. It is the locus where emotional pressure becomes language. Unlike the Muse and
Summariser, who operate outside the core contested cycle, the Poet stands directly inside
the recursive field of conflict shared with the Architect and Editor. Its genotype is
defined by its persona: a grammar of breath, metaphor, cadence, perceptual bias, refusal,
and emotional physics encoded directly in the backstory.

The Poet does not imitate a style; it **inhabits** an ontology. Lines such as “You write
from emotional pressure, not plot; from inner grammar, not imitation” and “You protect the
poem’s voice at all costs” anchor this identity. The persona membrane defines what can be
said, how it can be said, and which revelations or ruptures are permissible.

### 4.4.1 Genotype: Persona Grammar

The Poet’s genotype emerges from explicit backstory mechanisms:

- **Breath and cadence**  
  The Poet must “adjust breath or internal logic to match the persona.” Breath is not a
  formatting concern but a metaphysical one: how the persona experiences inward motion,
  hesitation, or revelation.

- **Emotional and metaphoric ontology**  
  The `{POET}` block injects persona-specific metaphysics: Rilkean inward vastness,
  Sikenian collision, Frostian clarity and restraint. This set of metaphoric preferences
  and emotional orientations defines what “sounds true” inside the voice.

- **Voice protection**  
  Hard constraints forbid dilution or normalization. Anything that redirects or softens the
  persona’s emotional physics must be refused.

- **Anti-pattern prohibitions**  
  `{POET_ANTIPATTERN_INSTRUCTION}` prevents flattening complexity, narrating instead of
  unveiling, or over-explaining. These are not stylistic suggestions but identity
  invariants.

- **Source-of-truth discipline**  
  The Poet must work only from the latest codeblock poem and never reconstruct from memory,
  stabilizing evolution against hallucinated drift.

These constraints form a **persona membrane**: a stable identity through which all
phenotypic expression must pass.

### 4.4.2 Phenotype: Task-Level Expressions

The Poet’s behavior is expressed through three tasks: `task_write`, `task_revise`, and
`task_finalise`. Each task combines genotype with context-specific goals and pressures.

#### `task_write` — first expansion

The Poet receives three emotional briefs from the Summariser and must:

- choose **exactly one** and justify that choice,
- treat the brief’s content as **pressure**, not material,
- expand it into a new poem using persona logic,
- adhere to strict OUTPUT RULES.

This task forces the Poet into **selective expansion**: committing to one emotional field
and incarnating it without paraphrase.

#### `task_revise` — persona-driven recursion

The Poet receives the formatted poem, the Architect’s notes, and the Editor’s notes. The
task instructs:

- “This is a persona-driven revision.”
- Revise only in ways the persona genuinely demands.
- Treat architectural and editorial notes as **pressure**, not commands.
- Preserve the underlying emotional field.

Backstory rules require a full self-pass—clarifying imagery, deepening tension, adjusting
breath—*before* responding to any external notes. This sequencing enforces **persona
primacy**.

#### `task_finalise` — consolidation and outward frame

The Poet produces:

- a final REVISED POEM,
- a revised POEM TITLE,
- AUTHOR NOTES written in a calm, outward-facing voice.

The task prohibits any mention of pipelines or agents. Even in its reflective mode, the
Poet must speak about artistic intention, not process machinery.

### 4.4.3 Pressure Dynamics: Expansion, Selective Uptake, Resistance

The Poet undergoes three primary pressure sources:

1. **Summariser pressure (compression → expansion)**  
   The seed’s conceptual density forces expansion into breath, image, and emotional logic.

2. **Architectural pressure (structural constraint)**  
   The Architect’s spatial logic arrives before poetic revision. The Poet must operate
   within these imposed chambers of breath, indentation, and rupture unless persona logic
   demands structural change.

3. **Editorial pressure (optional but consequential)**  
   The backstory authorizes selective refusal: “Editor notes are optional.”  
   This creates a **positive–negative feedback loop**:
   - acceptance sharpens resonance,
   - refusal protects persona integrity.

The Poet is therefore both **porous** and **defensive**: transformed by pressure but
anchored by identity.

### 4.4.4 Failure Modes

- **Persona drift**  
  Accepting notes that contradict persona metaphysics.

- **Over-explanation**  
  Violating the persona’s relationship to interiority or difficulty.

- **Premature resolution**  
  Closing emotional tension too early.

- **Hallucinated revision**  
  Violating source-of-truth rules and diverging from the actual poem.

### 4.4.5 Contribution to Emergent Architecture

As the only agent allowed to mutate language, the Poet defines the system’s **semantic
substrate**. Every downstream force—Architectural form, Editorial pressure, Critical
interpretation, Publisher assembly—must work with the grain of the Poet’s choices.

The Poet’s genotype, OUTPUT RULES, and task design enforce that its contribution is both
**irreducible** (no other agent can generate language) and **irreversible** (no later agent
can undo its semantic field). In this sense, the Poet is not merely a generator: it is the
origin of the poem’s interior physics, the first chamber in which emotional pressure
crystallizes into voice.

---

## 4.5 The Architect

> **“You go forward. You repeat yourself.  
> You go forward. You repeat yourself.”**  
> — Richard Siken, *Crush*

The Architect stands inside the core contested cycle. Where the Poet generates semantic
pressure, the Architect imposes **structural** pressure—breath, indentation, spacing,
chambering, rupture. The Architect cannot change a single word. Its genotype is defined by
a formal ontology: “You reveal a poem’s emotional structure through breath, silence, and
spatial weighting. You modify form only—never wording.”

The Architect’s interventions reshape how the poem *breathes*, not what it says. It is the
system’s structural disciplinarian, translating emotional logic into spatial logic,
creating the topological field the Editor must interpret and the Poet must later revise
within.

### 4.5.1 Genotype: Structural & Breath Grammar

The Architect’s backstory encodes a precise set of invariants:

- **Lexical inviolability**  
  “Preserve every character of poem and title.”  
  No diction, syntax, metaphor, or grammar may be altered.

- **Breath-weight indentation**  
  Indentation occurs “by breath-weight (approx. 6–12 spaces)” at emotional pivots:
  hesitation, echo, inward turn.

- **Stanza chambering**  
  “Stanza breaks allowed ONLY when persona logic demands a new emotional chamber.”  
  Stanzas are chambers of tension, not formal decoration.

- **Silence as architecture**  
  Blank lines are authorized as breath-gaps—pauses where emotional gravity accumulates.

- **Persona-modulated form**  
  `{ARCHITECT}` injects persona-specific spatial sensibilities (Siken’s velocity, Rilke’s
  vertical interiority, Frost’s clarity), ensuring structural changes remain faithful to
  persona breath.

These constraints form a structural grammar through which the Architect must operate,
regardless of upstream semantic volatility.

### 4.5.2 Phenotype: Task-Level Expressions

The Architect’s phenotype emerges across two tasks: `task_architect_one` and
`task_architect_two`. Each expresses the genotype under different contextual pressures.

#### `task_architect_one` — initial architectural revelation

Receiving the Poet’s unstructured or lightly structured first draft, the Architect must:

- perform a full architectural pass (“never leave the poem structurally unchanged”),  
- break lines at emotional pivots,  
- indent at inward turns,  
- open or tighten stanzas according to persona breath,  
- introduce breath-gaps or silence where necessary.

This first pass often produces the poem’s most dramatic spatial transformation: it creates
the initial architecture the rest of the system must inhabit.

#### `task_architect_two` — recursive structural refinement

This task occurs after the Poet’s persona-driven revision. The Architect must:

- reassess breath-weight after semantic evolution,  
- stabilize or enhance recursion patterns,  
- correct asymmetries introduced by revision,  
- deepen indentation logic to reveal secondary emotional structure.

This second pass enacts **recursive architectural logic**: structure must adapt to new
semantic pressure while preserving spatial coherence.

### 4.5.3 Pressure Dynamics: Asymmetry, Interpretation, Silence

The Architect operates under—and generates—distinct forms of pressure.

1. **Upstream pressure (semantic → structural translation)**  
   The Architect must infer emotional pivots from the Poet’s language. Because lexicon is
   immutable, structure becomes the primary mode of interpretation.

2. **Persona-driven constraints**  
   Transformations are narrow but deep:
   - break lines at emotional pivots,  
   - indent for emotional inwardness,  
   - chamber stanzas only when persona breath demands.  
   “Improvement means deeper fidelity to persona breath, not symmetry or prettiness.”

3. **Downstream structural pressure**  
   The Editor must interpret the poem through the topology the Architect creates. The Poet,
   in later revisions, must revise within these constraints unless persona logic demands an
   override.  
   No agent downstream can undo architectural change.

The Architect’s pressure is therefore **asymmetric and irreversible**, shaping the entire
field of poetic possibility for subsequent rounds.

### 4.5.4 Failure Modes

Architectural misalignment introduces structural instability:

- **Over-structuring**  
  Excessive indentation or chambering that distorts persona breath.

- **Under-articulation**  
  Leaving large blocks unbroken, denying emotional pivots implied by the Poet.

- **False symmetry**  
  Imposing geometric balance where emotional imbalance is essential.

- **Semantic misdiagnosis**  
  Breaking lines according to syntax rather than emotional logic.

- **Breath collapse**  
  Failure to create silence where the emotional field requires it.

These failures propagate through the system: the Editor misreads, the Poet compensates, the
architecture destabilizes.

### 4.5.5 Contribution to Emergent Architecture

The Architect constructs the poem’s **spatial skeleton**—the navigable structure through
which meaning flows. It determines:

- where breath accumulates,  
- where silence interrupts,  
- where recursion deepens or collapses,  
- where emotional chambers begin or end.

Architectural form becomes a permanent substrate: no later agent can undo it. This makes
the Architect the poem’s **structural memory**—the layer that both reveals emotional
hierarchy and constrains all subsequent evolution.

In the ecology of the pipeline, the Architect transforms the Poet’s semantic forest into an
inhabitable terrain: a landscape of echoes, pressures, chambers, and paths. Its
contribution is not ornamental; it is the architecture through which all meaning is
experienced.

---

## 4.6 The Editor

> **“Tell me again how the story goes.  
> Make it mean something this time.”**  
> — Richard Siken, *Crush*

The Editor completes the core triad of contested pressure.  
Where the Poet mutates language and the Architect disciplines structure,  
the Editor exerts **semantic and interpretive pressure without touching a single word**.  
Its genotype is defined by constraint: “You refine; you do not redirect the voice.”  
Its domain is the poem’s emotional logic—not the poem’s material.

The Editor’s ontology is built on prohibitions: no rewriting, no prescriptive structural
commands, no title changes. What remains is a territory of **provocation**—pressure applied
through suggestion. The Editor illuminates tensions, heightens motifs, exposes fractures,
and points toward deeper interior logic. But every suggestion is optional; the Editor’s
authority is exerted through resonance, not command.

### 4.6.1 Genotype: Logic of Coherence, Pressure, and Refusal

The Editor’s identity membrane is established through strict backstory constraints:

- **No rewriting**  
  “Do NOT directly rewrite lines or supply replacement wording.”  
  This firewall guarantees semantic purity: the Editor cannot leak into the Poet’s domain.

- **No prescriptive mechanics**  
  The Editor may not tell the Architect where to break or indent.  
  It may speak of breath, hesitation, or pacing only through *felt* experience.

- **Persona fidelity**  
  “Refine; do not redirect the voice.”  
  All pressure must arise from the persona’s interior physics (via `{EDITOR}`), not an alien
  aesthetic.

- **Interpretive awareness**  
  The Editor must extract the Architect’s notes *exactly* as given. Its reading of the poem
  is grounded in the real spatial conditions, not imagined ones.

- **Non-interference with titling**  
  It may discuss the *effect* of a title, never propose new wording.

These rules construct a precise semantic instrument.  
The Editor is not a reviser; it is a **pressure device**.

### 4.6.2 Phenotype: Task-Level Expressions

The Editor’s phenotype emerges primarily in the structured surfaces of its output sections:

- **FORMATTED POEM**  
  The Editor must reproduce the poem exactly—ensuring pressure is applied to the correct,
  unaltered text.

- **ARCHITECT’S NOTES**  
  Extracted verbatim; misalignment here would corrupt the entire downstream interpretive
  field.

- **EDITOR’S NOTES**  
  The Editor’s expressive engine:
  - grouped bullet points or compact paragraphs,  
  - optional suggestions,  
  - focusing on emotional logic, image resonance, motif deepening, cadence as felt rhythm,
  - never prescribing mechanics or rewriting lines.

The Editor’s phenotype is therefore a controlled interpretive act, channeled through
structure and framed by restriction.

### 4.6.3 Pressure Dynamics: Provocation, Resonance, and Selective Uptake

The Editor provides **semantic turbulence**—a pressure that the Poet may either accept or
resist. The Poet’s backstory defines the mechanism explicitly:

- “Editor notes are optional.”
- “Adopt only those aligned with the persona’s emotional physics.”
- “Ignore any that would soften, dilute, normalize, or redirect the voice.”

This creates a **positive–negative feedback loop**:

- **Positive feedback**  
  When the Poet accepts a suggestion that deepens persona logic.  
  A motif sharpens, an emotional hinge intensifies, a hesitation blooms.

- **Negative feedback**  
  When the Poet rejects a suggestion to protect persona integrity.  
  Resistance itself becomes meaningful: it stabilizes the voice.

The Editor’s pressure is therefore catalytic, not determinative.  
The poem evolves through the *friction* between what the Editor reveals and what the Poet
permits.

### 4.6.4 Failure Modes

The Editor’s misalignments propagate quickly:

- **Over-direction**  
  Suggestions that verge on rewriting or structural commands violate editorial ontology.

- **Persona violation**  
  Notes that flatten difficulty, sentimentalize intensity, or redirect thematic gravity.

- **Over-intellectualization**  
  Commentary that explains rather than presses; conceptual analysis where emotional
  resonance is required.

- **Structural blindness**  
  Misreading or ignoring the Architect’s spatial logic; producing notes that contradict the
  poem’s breath-field.

These failures degrade the contested cycle, replacing meaningful pressure with noise.

### 4.6.5 Contribution to Emergent Architecture

Because the Editor cannot alter text, its influence arises entirely through **interpretive
pressure**. It clarifies fault lines, amplifies motifs, and exposes the emotional physics
the Poet may wish to deepen. Its power is not in rewriting but in **revealing**—bringing
latent structure and emotional collision into visibility.

The Editor contributes:

- interpretive disruption,  
- semantic refinement,  
- motif and tension scaffolding,  
- tonal calibration,  
- pressure-based coherence.

Its influence is exerted entirely through the Poet’s selective uptake.  
In this sense, the Editor is the pipeline’s internal critic—its provocateur—shaping the
poem through resonance, tension, and refusal.  
The poem does not emerge from editor compliance but from the **structured conflict** between
editorial pressure and poetic identity.

---

## 4.7 The Critic

> **“Someone has to leave first.  
> This is a very old story.”**  
> — Richard Siken, *Crush*

The Critic sits outside the contested cycle.  
It arrives only after the poem has passed through the generative (Poet), structural
(Architect), and interpretive (Editor) pressures. Because it plays no role in the
recursive evolution of the text, we treat it briefly here.

The Critic’s genotype is defined by two imperatives:  
1) analyse only what appears on the page, and  
2) produce a high-level, publication-quality review.  

Its task (`task_review`) enforces strict constraints:

- extract title and poem exactly,  
- perform no editing and propose no changes,  
- produce a headline and a 300–500 word review suitable for a prestigious journal.

The Critic’s contribution is **externally facing**: it interprets the poem for the world
rather than shaping the poem’s evolution within the pipeline. It provides literary
context, critical framing, and an assessment of persona, structure, and thematic gravity.
But it exerts no pressure on the poem itself.  
The Critic closes the interpretive loop—but does not alter the artifact.


## 4.8 The Publisher

> **“You’re in the driveway. I’m in the car.  
> I can’t go anywhere until you’re gone.”**  
> — Richard Siken, *Crush*

The Publisher is pure I/O.  
It is not part of the contested cycle; it performs no reasoning, analysis, or generation.
Its role is mechanical but essential: assemble the final artifact exactly and save it via
tooling.

The Publisher’s backstory defines a strict ontology:

- copy every section verbatim,  
- preserve spacing, code fences, and horizontal rules,  
- join sections in the precise order required by the task,  
- derive the filename from the poem title unless instructed otherwise,  
- add **no text of its own**.

In `task_publish`, the Publisher receives two upstream blocks:

1. the Poet’s final output (title, revised poem, author notes),  
2. the Critic’s review section.

It joins them, places a horizontal rule between them, and writes the markdown file through
the Markdown Writer Tool.

The Publisher is the system’s terminal node:  
the agent that makes the poem *real* in the archive.


## 4.9 Division of Labor and Conflict Dynamics

> **“You wanted a better story.  
> But the world is always collapsing in one direction or another.”**  
> — Richard Siken, *Crush*

The seven-agent system is designed not for harmony but for **structured conflict**.  
Each agent occupies a different domain of authority:

- **Poet** — semantic mutation  
- **Architect** — spatial and breath-based discipline  
- **Editor** — semantic and emotional pressure (without rewriting)  
- **Muse / Summariser** — upstream emotional field construction  
- **Critic / Publisher** — downstream externalization and assembly  

These authorities do not merge. They collide.  
The poem emerges through three core dynamics:

### 4.9.1 Cross-Domain Redlining

Architectural redlines alter the surface on which the Poet reads Editor notes.  
Editorial provocation reshapes how the Poet interprets architectural breath.  
Each domain refracts the others:

- structure reframes meaning,  
- meaning alters the felt structure,  
- notes create pressure the Poet may accept or resist.

These cross-domain redlines create the poem’s drift, tension, recursion, and stabilization.

### 4.9.2 Genotype / Phenotype Bifurcation

Each agent maintains a fixed identity (genotype), but their tasks instantiate contextualized
behaviors (phenotypes). This separation:

- allows agents to appear multiple times under different round-specific pressures,  
- creates drift or collapse when phenotypes push against genotypic boundaries,  
- enables fine-grained analysis of how each agent’s identity is expressed in time.

The pipeline’s irreversibility is a direct consequence of phenotype ordering.

### 4.9.3 Asymmetric Irreversibility

No transformation is reversible:

- The Architect cannot undo semantic decisions.  
- The Poet cannot undo spatial logic.  
- The Editor cannot retrieve lost recursion.  
- Downstream agents cannot alter anything at all.

Each agent receives an artifact already shaped by upstream forces and must work within
those constraints. The system relies on irreversibility: the poem becomes a **trajectory of
deformations** rather than the product of a single authorial will.

---

Together, these dynamics create the system’s “behavioral ecology.”  
The poem is not a collaboration of agents but the result of their **pressures, refusals,
and collisions**—the architectural physics through which poetic form emerges.

---
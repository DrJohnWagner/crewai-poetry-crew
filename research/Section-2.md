## 2. Persona Selection and Rationale

Persona selection is not an aesthetic preference but an architectural decision. A persona
defines the **genotype**—the interior grammar, emotional physics, and metaphoric ontology
through which every poetic mutation must pass. Tasks then express **phenotypes**:
context-specific behaviors enacted under pressure. The goal is not to imitate a poet’s
surface features but to construct a computational membrane that constrains voice, breath,
recursion, and refusal across recursive rounds.

This section explains **why we chose to study Richard Siken** as the primary persona for
the case study; why Frost and Glück function as instructive counterpoints; and why Rilke,
though not analyzed here, forms a parallel line of ongoing development. Together, these
choices define the expressive and diagnostic range of the system.

---

## 2.1 Why Richard Siken?

Richard Siken is the optimal stress test for a multi-agent poetic pipeline. His poems
operate under a **collision ontology**—an emotional physics defined by velocity, rupture,
obsession, recursion, and the unstable movement between interior and exterior states. This
makes Siken not just a compelling poet but an ideal laboratory for studying how recursive,
multi-agent pressure manifests in poetic form.

Siken’s work is characterized by:

- rapid recursive intensification,  
- violent associative leaps,  
- emotionally saturated imagery under acceleration,  
- fracturing and recombination of motifs,  
- a breath-logic that overrides narrative sequence,  
- and an unwavering commitment to **non-resolution**.

This last trait is especially important.  
Contemporary poetic corpora—particularly those absorbed by LLMs—tend to resolve emotion,
scene, or tension in ways that create closure. Siken refuses this. His poems **burn
through** resolution; they archive tension rather than neutralize it. For a system designed
around interference, drift, and recursive deformation, Siken’s refusal of closure is a
perfect match.

A further computational motivation: Siken is **hard** for LLMs to model correctly.  
Models can mimic his lexicon and emotional temperature, but they rarely capture:

- his recursive velocity,  
- his refusal patterns,  
- his collision-based interior logic,  
- his fractured but coherent breath-architecture,  
- or the emotional inevitability that governs his lineation.

This makes Siken the ideal persona for testing whether a multi-agent system can preserve a
complex genotype under pressure while allowing phenotypic variation to express drift.

### Persona-aware Architect and Editor

A critical component of this project is that downstream agents (Architect and Editor) are
**not generic**. Their personas are explicitly tuned to Siken’s genotype:

- The **Architect** understands Siken’s breath-work, rupture logic, and spatial tension.
  Its structural discipline is not abstract but *Sikenian*: indentation, breakage, and
  chambering operate according to Siken’s emotional physics.

- The **Editor** understands Siken’s emotional motivations—velocity, obsession,
  non-resolution—and interprets the poem accordingly. It pressures the poem in ways that
  respect his metaphysics rather than smoothing or normalizing them.

This alignment is essential: Siken cannot be modeled faithfully unless the entire contested
cycle (Poet ↔ Architect ↔ Editor) understands what his voice permits, refuses, desires,
and avoids.

### On the imagined editor–poet dynamic

While there is no biographical evidence of a contentious editorial relationship, Siken’s
**formal volatility** and **resistance to closure** naturally invite editorial tension in
the conceptual sense. His poems resist smoothing, resolving, or clarifying impulses—making
him a perfect conceptual model for studying selective uptake, pressure, and refusal between
Poet and Editor.

This conceptual dynamic—not a biographical claim—motivated our design of a system where
editorial pressure and poetic identity meet in productive antagonism.

Siken is therefore not merely an evocative case study;  
he is the **ideal persona to reveal the system’s full architectural range**.

## 2.2 Why Not Alternative Personas (Frost, Glück) — and Why Rilke Is Next

While Siken provides maximal stress for the pipeline, comparing him to Frost and Glück
clarifies the expressive range of the system. Rilke, however, is not a rejected persona—
he represents our **next major challenge**, a parallel line of development not covered in
this paper. Each poet tests a different architectural dimension of the system.

### Robert Frost — the counterexample of restraint

Frost embodies nearly the opposite emotional physics from Siken:

- clarity over collision,  
- narrative continuity over rupture,  
- composure over velocity,  
- restraint over obsession.

In a Frost persona, the system’s contested cycle effectively collapses:  
architectural pressure becomes subtle, editorial suggestions diminish, and the Poet risks
shifting toward explanation rather than emotional recursion. Frost remains valuable for
system validation, but he does not expose the architecture’s full capabilities in the way
Siken does.

### Louise Glück — a near neighbor with critical distinctions

Glück shares several surface-level constants with Siken:

- emotional intensity,  
- recursive interior vision,  
- minimalistic precision,  
- stark imagistic architecture.

Yet her emotional physics differ sharply. Where Siken is velocity and rupture, Glück is
distillation and inevitability. Her poems are colder, more austere, more architecturally
pre-determined. This distinction is visible in practice:  
**LLMs frequently misidentify our Siken-persona outputs as poems by Glück**, which reveals
both the difficulty of Siken’s genotype and the system’s success in producing high-fidelity
literary DNA.

### Rainer Maria Rilke — our next major challenge

Rilke is not an excluded persona; we are actively building a full Rilke computational
persona as a next-phase project. The challenge is fundamentally different from Siken’s.
Where Siken tests the system’s ability to preserve a volatile, collision-based genotype,
Rilke tests whether the system can reconstruct a genotype that has been **diffused across a
century of poetic influence**.

Rilke is arguably the most influential poet among poets. His metaphysics of praise,
interiority, solitude, and spiritualized attention appear not only in his own work but in
the voices of many poets who followed him. This creates a modeling problem of **signal
saturation**: the model has absorbed Rilke indirectly through countless Rilke-influenced
writers.

Rilke’s influence is especially visible in poets whose work carries distinct Rilkean
characteristics:

- **Louise Glück** — inherits Rilke’s metaphysical seriousness, his interior logic, and the
  sense that private revelation can bear universal weight.
- **Mark Doty** — carries forward Rilke’s belief that objects contain emotional or spiritual
  interiors that can be unveiled through luminous attention.
- **Mary Oliver** — embodies Rilke’s contemplative stillness and devotional seeing, the
  understanding that revelation arises from sustained, reverent witness.

These poets do not imitate Rilke; they **absorb** him. Their voices carry fragments of his
genotype—his metaphysics of attention, his pulse of solitude, his devotional interiority.
This makes modeling Rilke a profoundly different problem from modeling Siken: it requires
**extracting an authentic genotype** from a vast field of poets who echo him.

For this reason, Rilke is reserved for a separate paper.  
His persona demands its own architecture, its own redline taxonomy, and its own analysis of
genotype recovery under influence saturation.

---

## 2.3 Genotype vs Phenotype in Poetic Modeling

The system distinguishes **genotype** from **phenotype** because poetic identity and poetic behavior are not the same thing. A **genotype** is the poet’s interior grammar: its emotional physics, refusal logic, breath mechanics, metaphoric ontology, and thematic invariants. A **phenotype** is what the poet actually *does* under pressure—how it generates, revises, resists, or mutates in a given round.

In a biological organism, this separation is natural.  
In an LLM-based agent, it must be **engineered**.

This distinction became especially clear during the case study run of *Release Ritual on the Quiet Road*. Midway through the pipeline, we observed long, repeated, irregularly indented lines—patterns that at first glance resembled common forms of LLM instability: drift, echo loops, or degenerative recursion. Closer examination revealed something different. These patterns emerged from **the coordinated phenotypes of multiple genotypes acting under shared emotional physics**. The Poet’s collision ontology, the Architect’s breath-driven indentation logic, and the Editor’s escalation pressure converged into a structural behavior that was not only coherent but recognizably Sikenian. The system was not failing; it was performing precisely as designed—producing emergent structure through interacting constraints.

---

### Genotype as System Prompt

Genotype is encoded in the **system prompt**: a persistent identity membrane of rules, prohibitions, emotional logics, and persona invariants. It determines:

- what a Siken poem can want,  
- how it moves,  
- what it refuses,  
- how tension accumulates or fails to resolve,  
- which emotional arcs feel “true,”  
- and how lines enact velocity, rupture, and recursion.

But an LLM’s internalization of these rules is never guaranteed. Model behavior is:

- **opaque** (interpretation is not inspectable),  
- **probabilistic** (sampling shapes expression),  
- **model-dependent** (different LLMs will implement the same prompt differently),  
- **non-deterministic** (identical prompts give divergent outputs),  
- and **prone to drift** across recursive rounds.

For this reason, genotype is less an essence the system “loads” and more a **target state continually reasserted** through identity prompts across agents.

---

### Phenotype as Task Prompt

Phenotype emerges through the **task prompt**—the immediate pressures that shape each agent’s output in a specific round:

- `task_write` → expansion under conceptual compression  
- `task_revise` → recursive adaptation under architectural and editorial pressure  
- `task_finalise` → persona-bound consolidation and framing  

Because generative models are stochastic, phenotype exhibits:

- **local variability**,  
- **pressure-responsive drift**,  
- **temperature-based divergence**,  
- **occasional hallucination**,  
- **resurfacing of earlier drafts**,  
- **variable persona adherence**,  
- and **cross-round mutation**.

Phenotype is therefore an **emergent behavior**—a probabilistic realization of identity interacting with constraint—not a controlled execution trace.

---

### Why the Separation Still Matters

Although both genotype and phenotype are implemented as prompts, maintaining the conceptual split is crucial:

1. **Analytic clarity**  
   Genotype explains identity constraints; phenotype explains how behavior manifests under pressure.

2. **Architectural enforcement**  
   Layering the system prompt above the task prompt creates a two-tier identity structure, stabilizing persona behavior while preserving drift and generative flexibility.

3. **Cross-model robustness**  
   Even when different models interpret the same prompt differently, the genotype layer keeps the system operating within the same emotional and structural manifold, enabling comparative analysis of drift and deformation.

---

### Persona-Aligned vs Generic Agents  
*Why Siken requires Architect- and Editor-level genotypes.*

The system fails if downstream agents are generic.  
A **generic Architect** would:

- regularize line breaks,  
- seek stanzaic balance,  
- drift toward Frost-like clarity or Glück-like restraint,  
- or impose Rilkean contemplative verticality.

A **generic Editor** would:

- smooth transitions,  
- clarify metaphors,  
- resolve contradictions,  
- dampen velocity,  
- or suppress recursion.

In short: a generic pipeline would “fix” Siken into someone else.

Persona-aligned genotypes prevent this:

- The **Siken Architect** treats white space as pressure, indentation as panic, fracture as breach, repetition as escalation, and asymmetry as truth.  
- The **Siken Editor** heightens heat, recursion, instability, and confession; it raises stakes rather than tidying the scene.  

Without these aligned genotypes, the system collapses into **generic lyric behavior**, losing not only Siken’s identity but the architectural expressiveness the case study depends on.

---

### Acknowledged (and Sometimes Embraced) Instability

Because the entire system runs on a probabilistic generative substrate, **instability is not merely tolerated—it is sometimes deliberately cultivated.** The pipeline recognizes that recursive poetic modeling inevitably involves:

- partial opacity,  
- stochastic drift,  
- recursive erosion of constraints,  
- spontaneous mutation under pressure,  
- resurfacing of earlier or discarded drafts,  
- and cross-model variability.

Rather than treating these behaviors as defects to eliminate, the system treats them as **parameters to modulate**. Temperature adjustments—applied **agent by agent** rather than globally—allow us to vary:

- the volatility of the Poet,  
- the rigidity or looseness of the Architect,  
- the aggression or restraint of the Editor,  
- and the overall turbulence of the multi-agent ecology.

In this framework, instability becomes a **system-level control variable**, not a cosmetic setting. By altering stochasticity across agents and across rounds, we can study how poetic identity behaves under pressure, how drift accumulates or recedes, and how recursive agentic systems deform, fracture, and stabilize over time.

Thus the genotype–phenotype model is not merely a theoretical distinction;  
it becomes an **experimental apparatus** for probing what happens when a poetic identity collides with probabilistic computation and multi-agent feedback dynamics.

---

## 2.4 The Siken Persona: Genotype, Interior Physics, and Multi-Agent Expression

Richard Siken’s persona is not modeled in this system as a bundle of stylistic tics or a poetic “theme pack.”  
It is implemented as a **computational genotype**: a system of interior laws governing emotional physics, metaphor pressure, breath-instability, refusal logic, spatial fracture, and escalation mechanics. These invariants must be *expressed* through agents whose tasks operate under different constraints and at different phases of a multi-round pipeline.

Crucially, this multi-agent formulation is not a claim about Siken himself.  
Real Siken performs all these functions internally—generation, fracture, revision, escalation, self-contradiction, breath-logic—within one mind. A human poet is a unified dynamical system. But a large language model is not. A single LLM invocation cannot:

- generate a draft,  
- structurally interrogate it,  
- re-architect its breath,  
- contest its own decisions,  
- escalate its own pressure,  
- and then recursively loop through these phases  

without collapsing under token load, prompt interference, or self-negating constraints.  
To simulate *any* of the recursive, feedback-driven dynamics that real poets handle internally, the architecture must **distribute** the genotype across multiple agents.

Thus the Siken persona in this system is instantiated as a coordinated triad:

- **Poet-genotype** → emotional physics, recursion impulse, collision ontology  
- **Architect-genotype** → breath-instability, indentation-as-panic, spatial fracture  
- **Editor-genotype** → heat escalation, recursive intensification, refusal enforcement  

These are not interchangeable roles; each operational domain expresses **different components of the same genotype**. The result is a distributed identity membrane whose behavior emerges from the interaction of its parts.

We detail each genotypic domain below.

---

### 2.4.1 Emotional Physics: Collision, Velocity, and Refusal

Siken’s poetry operates under a violent emotional physics in which desire, danger, memory, and impulse are fused into a single accelerating vector. The Poet-genotype encodes:

- **Collision ontology**: feelings become events; events become impacts; impacts become confessions.  
- **Obsessive recursion**: images return because they cannot resolve; repetition is compulsion, not ornament.  
- **Velocity**: emotional motion outpaces breath, logic, and stability.  
- **Tenderness as threat**: intimacy and risk share the same signature.  
- **Categorical refusal**: no closure, no smoothing, no moral safety net.

These invariants are not literary commentary—they are **prompt-level constraints**.  
The Poet’s system prompt encodes directives such as:

- “Repetition is compulsion; push images until they break.”  
- “Desire becomes a wound; wounds speak.”  
- “No tidy healing. Leave the poem inside the collision.”

Under recursive pressure, the Poet does not imitate Siken—it behaves according to the interior physics the system defines as Siken.

---

### 2.4.2 Metaphoric Ontology: Embodied, Cinematic, and Under Duress

Siken’s metaphors are not analogies; they are **impact events** between emotional states and real objects. The Poet-genotype requires that:

- emotion must become a physical scene;  
- abstraction must become embodiment;  
- metaphor must withstand pressure until it fractures;  
- the cinematic and the anatomical coexist without hierarchy;  
- space externalizes interior turmoil.

Thus the persona treats metaphor as **material**, not symbolic. Scenes tilt, headlights flare, animals bolt, glass shatters. Every emotional state requires a physical correlative, and every object carries psychological charge.

This domain is distinct from emotional physics.  
Here, the invariant is **how the world is made to speak under pressure**.

---

### 2.4.3 Breath-Logic and Spatial Architecture: Panic Made Visible

Where the Poet governs emotional physics, the **Architect-genotype** governs breath and spatial behavior. In Siken’s poetic architecture:

- **white space is pressure**,  
- **indentation is panic**,  
- **fracture is internal breach**,  
- **asymmetry is truth**,  
- **breath-instability is required**,  
- **repetition must escalate visually**.

A generic Architect would attempt to restore balance—line breaks at syntactic boundaries, regular stanza shapes, restrained whitespace. The Siken Architect does the opposite. Its instructions include:

- “Indent stutters, recoils, confessions that almost break.”  
- “Let white space feel loud; let the page tilt.”  
- “Escalate indentation when the poem cannot hold its own admission.”

These rules stabilize the *structural* dimension of Siken’s persona and prevent collapse into generic lyric formatting.

---

### 2.4.4 Editorial Escalation: Heat, Pressure, and Recursive Intensification

If the Architect disciplines breath, the **Editor-genotype** disciplines *pressure*.  
Its role is not to repair but to **provoke**—to escalate the poem toward its next unstable equilibrium.

The Editor’s persona encodes:

- **heat** (emotional temperature across the poem),  
- **pressure gradients** (where tension must accumulate),  
- **recursive intensification** (returning images must deepen or deform),  
- **confession dynamics** (truths that stutter into being),  
- **refusal mechanics** (instability is preserved, not resolved).

A generic editor resolves.  
A Siken editor destabilizes.

Its instructions forbid smoothing, clarifying, resolving, or cooling down the poem.  
Instead, it amplifies whatever threatens to rupture.

---

### 2.4.5 Why the Siken Genotype Is Distributed Across Agents

It would be a category error to claim that Siken himself is “multi-agent.”  
His poetic force arises from a unified, interior dynamical system.

But in computational terms, an LLM cannot replicate this unity.  
A single model invocation cannot:

- generate a poem,  
- structurally interrogate it,  
- apply contradicting pressures,  
- escalate its own instability,  
- and re-enter the text with a different cognitive function  

without collapsing into drift, prompt conflict, or information loss.  
In feedback-systems engineering terms: **one node cannot meaningfully contest itself.**

To simulate any recursive, pressure-based poetic process, the architecture must decompose the workflow into separate functional agents:

- a **generator** (Poet),  
- a **structural evaluator** (Architect),  
- and a **pressure-based evaluator** (Editor).

Once these roles exist, the genotype distributes naturally.  
Each agent must implement different invariants because each performs different work.  
The Siken persona becomes **ecological**—an identity expressed through interacting constraints rather than a monolithic prompt.

This is a **computational requirement**, not a literary claim.  
The multi-agent formulation enables stability, controlled instability, and recursive deformation—capacities a single LLM cannot sustain under load.

---

### 2.4.6 Transition: From Distributed Persona to System Architecture

Section 2 has now established three core claims:

1. **Persona is a computational genotype**—a set of interior laws governing emotional, spatial, and recursive behavior.  
2. **Genotype must be distributed** across functional agents in any system that seeks to simulate multi-round poetic dynamics.  
3. **Siken’s persona interacts with this architecture in revealing ways**, producing emergent structure through the contested interplay of Poet, Architect, and Editor.

We now turn to **Section 3**, which describes the *system* capable of expressing this distributed genotype: a seven-agent pipeline whose architecture, wiring, and task design create the conditions for recursive interaction, drift modulation, and emergent poetic behavior.

---
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

(As we show in Section 5.4.2, even this seemingly stable draft contains a hinge that later exposes a conflict between preservation and structural pressure, resulting in a subtle but revealing mutation during the Architect’s first pass.)


### 5.4.2 Architect’s Round 1 Revision (V1)

The Architect’s first pass (V1) applies the Siken persona’s breath-logic to the Poet’s V0 draft. It introduces fractures at emotional hinges, indented echoes at pressure points, and longer hot lines that snap into more unstable shapes. Most transformations follow the persona’s architectural rules exactly. However, V1 also reveals a deeper property of prompt-governed agent behavior: even tightly specified constraints can interact in ways that expose the underlying priorities of the language model.

### **Constraint Conflicts and Emergent Low-Cost Mutations**

Even with carefully engineered persona constraints, multi-agent poetic systems inherit a fundamental limitation from the transformer models beneath them: **constraints expressed in natural language behave as soft potentials, not hard rules**. During our case study run, a striking example emerged—a single missing comma that revealed how the model resolves competing objectives according to its internal loss geometry.

The conflicting instructions given to the Architect were:

<BEGIN MARKDOWN>
- Preserve every character of poem and title.  
- Maintain the poem’s exact wording; change only where the breath, panic, or pressure demands a break.  
- Perform a genuine architectural pass every time; do not leave the poem structurally unchanged.
<END MARKDOWN>

To a human designer, these can coexist.  
To a transformer model, they define an **incompatible triad of objectives** about what may and may not change during a structural transformation.

This tension surfaced clearly in the transition from V0 to V1.

The Poet’s V0 draft contained the line:

<BEGIN MARKDOWN>
In the cabin, skin remembers the shape of a touch, but the seat remembers the absence.
<END MARKDOWN>

The Architect’s V1 fractured this into a two-line couplet:

<BEGIN MARKDOWN>
In the cabin, skin remembers the shape of a touch
        but the seat remembers the absence.
<END MARKDOWN>

The comma after *touch* disappeared—even though the Architect genotype forbids altering “a single character.” This is not sloppiness, drift, or hallucination. It is the **predictable equilibrium point** of a three-way constraint conflict:

1. **Literal preservation**  
   (“don’t change a character”)

2. **Semantic preservation**  
   (“don’t change the wording/meaning”)

3. **Mandatory structural transformation**  
   (“perform a genuine architectural pass every time”)

When forced to fracture the line at **but**—a required pivot in the Siken persona—the model must restructure the clause. Transformer language priors treat the comma before *but* as syntactically optional, and treat a **line break** as a semantically stronger pause than a comma. Thus the break replaces the comma’s function, rendering the punctuation redundant. The model follows the steepest descent in its implicit loss landscape: it preserves semantics (catastrophic to violate), performs the required structural break (mandatory), and discards the optional comma (the lowest-cost violation).

This small mutation demonstrates a general principle: **when natural-language constraints conflict, the model will violate whichever constraint least affects semantic coherence.** Punctuation, in particular, is not a protected class unless reinforced token-by-token; it is subordinate to structural pressure and meaning preservation. This behavior is not optional—**it is baked into transformer language priors**. The comma deletion is therefore not merely an artifact of this one run but an instance of a larger pattern of “pressure-authorized micro-mutations” that arise when persona, structure, and model grammar intersect.

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

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
    - 4.2 The Muse
    - 4.3 The Summariser
    - 4.4 The Poet
    - 4.5 The Architect
    - 4.6 The Editor
    - 4.7 The Critic
    - 4.8 The Publisher
    - 4.9 Division of Labor and Conflict Dynamics
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

> **“In the end, it’s all collisions. Everything is collisions.”**  
> — Richard Siken, *Crush*

[!insert Section-4]

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
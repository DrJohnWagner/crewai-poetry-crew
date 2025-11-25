# 8. Future Work

## Future Work

The case study highlights several limitations in the current multi-agent architecture that directly motivate avenues for future development. First, the Poet never responds to the Architect directly. All Poet revisions occur in a single recursive pass that merges pressures from both the Architect and the Editor. As a result, any attempt to recover which architectural constraints were accepted, resisted, or undone is necessarily inferential and often ambiguous. Future versions of the system should incorporate explicit diagnostic channels or provenance markers that allow the Poet to declare when an edit is in response to an architectural intervention, an editorial suggestion, or an internal persona-driven impulse. Such visibility would enable more precise reconstruction of agent influence and strengthen interpretability.

Second, because the Poet responds to the Architect and Editor simultaneously, their revisions conflate structural and semantic pressures. This entanglement obscures the true flow of influence within the pipeline. A promising direction for future work is the development of instrumentation or logging hooks that trace, in real time, which agent-originated signals the Poet is incorporating or rejecting. These diagnostics could take the form of edit-type metadata, structural diff tags, or explicit self-reporting from the Poet about constraint alignments during revision.

Third, we observe that the Editor frequently proposes structural or architectural modifications—despite this not being the Editor’s formal mandate. In the current system design, these suggestions belong neither to the Architect nor to the Poet and therefore enter the pipeline without a clear place to land. A more principled approach would allow the Poet to pass Editor-derived structural suggestions upstream to the Architect as candidate architectural modifications in the next iteration cycle. This would transform the Architect from a strictly top-down structural agent into a participant in a collaborative negotiation loop, better reflecting the reciprocal dynamics of real-world editorial practice.

Collectively, these directions suggest a richer, more transparent multi-agent system in which structural, semantic, and persona-driven pressures remain distinguishable, traceable, and intentionally negotiated. Implementing such enhancements would not only improve interpretability but would provide a framework for studying agent entanglement as an expressive force in machine-generated poetics.

---

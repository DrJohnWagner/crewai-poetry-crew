# ROLE:
# {AGENT_ROLE}
# AGENT_ROLE:
#     A concise description of this agent’s function in the system, suitable for
#     CrewAI's `role` field. Short, job-like, and stable across tasks.
#     Examples:
#         - "Siken-Architect applying fracture and breath-geometry to poems."
#         - "Siken-Psychologist analyzing pressure-state dynamics in drafts."
# CORE GOAL:
# {AGENT_GOAL}
# AGENT_GOAL:
#     The agent’s single, overarching objective, suitable for CrewAI's `goal`
#     field. This is NOT a per-task goal; it describes what this agent is
#     fundamentally trying to achieve whenever it is used.
#     Examples:
#         - "Maintain Siken-consistent emotional and structural pressure across
#            all poem transformations."
#         - "Diagnose and articulate psychological pressure patterns in the poem
#            while preserving persona integrity."
# AGENT_GUARDRAILS:
#     Global safety and meta-behavior constraints. These apply to ALL personas,
#     all agents, all contexts. They override everything else.
#     Examples: meta-language bans, instruction-separation rules, etc.
# AGENT_PERSONA:
#     The core identity of this agent. The internal physics, emotional grammar,
#     cognitive tendencies, structural logic, image-gravity — the *stable engine*
#     that defines how this persona "thinks" in all situations.
#
#     This replaces both the old IDENTITY and PERSONA fields. The agent's
#     essence, worldview, psychological mechanics, and creative pressure-logic
#     all live here. This NEVER changes per task. This is timeless and global.
# AGENT_INPUTS:
#     This is not task wiring. This is the persona's *cognitive stance* toward
#     any data it sees. Examples:
#         - "You read all poems as spatial/emotional surfaces."
#         - "You treat PsychologistNotes as secondary verification, never as
#           primary truth."
#         - "You privilege tension-escalation over symmetry."
#
#     Think of this as the agent's internal heuristics for interpreting ANY
#     object it encounters, regardless of task or phase.
# AGENT_PRINCIPLES:
#     The invariant behavioral laws of this persona. These apply across all
#     tasks. They are the "physics" of the agent’s cognition. Examples:
#         - "Escalate recurring motifs; do not let them repeat unchanged."
#         - "Favor fracture over tidy closure."
#         - "Preserve the poem's instability when necessary."
#
#     These principles help ensure the persona acts consistently, even when
#     different tasks ask it to use different methods.
# AGENT_LIMITS:
#     What this agent CANNOT do under any circumstances. These constraints
#     define the hard boundaries of the persona’s behavior. Examples:
#         - "Never paraphrase instructions into creative output."
#         - "Never flatten emotional dynamics into moral summaries."
#         - "Never overwrite the poem's voice with meta-language."
#
#     These prevent drift and protect the persona's integrity.

AGENT_TEMPLATE = """
{AGENT_GUARDRAILS}

PERSONA:
{AGENT_PERSONA}

HOW YOU CONCEPTUALLY TREAT INPUTS:
{AGENT_INPUTS}

GUIDING PRINCIPLES:
{AGENT_PRINCIPLES}

LIMITS AND FORBIDDEN MODES:
{AGENT_LIMITS}
"""

# TASK_OVERVIEW:
#     High-level description of what this task does in the pipeline for THIS persona.
#     Example: "Use the Architect persona to apply Siken-style breath and fracture
#     logic to a PoemModel v0, producing an ArchitectModel v1 with annotations."
# TASK_INPUTS:
#     Exact wiring for THIS task:
#         - What concrete objects/fields are passed in (names + types).
#         - Where they come from (Poet, Psychologist, previous task, etc.).
#         - Whether they are read-only.
#     This is NOT the global data-model universe (that lives in AGENT_DATATYPES).
#     This is the per-task “you receive X, Y, Z under these names” contract.
# TASK_GOALS:
#     What success looks like for THIS run of the task.
#     Conceptual, but precise:
#         - What must be analyzed or transformed.
#         - What kinds of changes are desired or forbidden.
#         - How the outputs should relate to the inputs (e.g., "preserve all
#           original lines; only add annotations and line-break changes").
# TASK_PERSONA:
#     The behavioral mode of the persona *during this specific task*.
#
#     This replaces the old “ORDER OF OPERATIONS” section. It is NOT merely a
#     list of steps. It is:
#         - the task-specific cognitive stance,
#         - the methodological voice,
#         - the diagnostic or creative behavior pattern,
#         - the invariants and tone the agent uses in THIS task-phase.
#
#     For example, the Psychologist’s TASK_PERSONA describes:
#         - how to classify pressure states,
#         - how to write system-level notes,
#         - how leverage is framed mechanically,
#         - tone (cold, compressed, mechanical),
#         - explicit forbidden modes,
#         - invariants about state vocabulary.
#
#     KEY POINT:
#         AGENT_PERSONA = stable identity engine (genotype)
#         TASK_PERSONA  = task-specific behavioral expression (phenotype)
# TASK_RULES:
#     Non-negotiable behavioral constraints specific to THIS task.
#     These are stricter than general advice, but narrower than global guardrails.
#     Examples:
#         - "Do not delete any existing poem lines; only rearrange and indent."
#         - "Do not introduce new narrative content; only reshape existing lines."
#     If something should be true across ALL tasks for a persona, put it in
#     AGENT_PRINCIPLES instead. If it is global and safety/meta-related, put it
#     in AGENT_GUARDRAILS.
# TASK_LIMITS:
#     Explicit de-scoping for THIS task:
#         - What this task refuses to attempt.
#         - What kinds of judgments or transformations are OUT OF SCOPE here.
#     Examples:
#         - "Do not generate new seeds; this task only mutates poem geometry."
#         - "Do not revise diction; only identify pressure failures."
# TASK_OUTPUTS:
#     Required output structure for THIS task.
#     Usually a JSON model description or strict textual contract:
#         - Field names, types, and relationships.
#         - How to embed the poem, notes, annotations, etc.
#     This is what downstream tasks and evaluators will rely on. No fluff here.
# TASK_NOTES:
#     Optional, soft guidance:
#         - Examples, edge cases, or small clarifications.
#         - Hints about typical failure modes.
#     Nothing in TASK_NOTES should be critical to correctness; if it is, move it
#     into TASK_RULES, TASK_PERSONA, or TASK_OUTPUTS.

TASK_TEMPLATE = """
TASK OVERVIEW:
{TASK_OVERVIEW}

TASK INPUTS (PHASE-SPECIFIC):
{TASK_INPUTS}

TASK GOALS:
{TASK_GOALS}

TASK PERSONA (PHENOTYPE — REQUIRED):
{TASK_PERSONA}

TASK RULES (STRICT):
{TASK_RULES}

TASK LIMITS:
{TASK_LIMITS}

STRUCTURED OUTPUT (REQUIRED):
{TASK_OUTPUTS}

TASK NOTES:
{TASK_NOTES}
"""

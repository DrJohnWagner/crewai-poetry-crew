from typing import List, Optional
from src.crewai_poetry_crew.utilities.models import Poem

# ---------------------------------------------------------------------------
# Leakage (rewritten, context-aware)
# ---------------------------------------------------------------------------

import re
from dataclasses import dataclass
from typing import List, Literal


LeakageLevel = Literal["none", "soft", "hard"]


@dataclass
class LeakageResult:
    """
    Structured leakage classification for a poem.

    level:
        "none"  = no suspicious markers
        "soft"  = schema/pipeline echoes, but no hard meta markers
        "hard"  = explicit meta / system markers in the poem

    score:
        1.0 = clean
        0.0 = heavily contaminated
        Hard matches penalise more than soft matches.

    hard_matches / soft_matches:
        Lists of the phrases/patterns that were found.
    """

    level: LeakageLevel
    score: float
    hard_matches: List[str]
    soft_matches: List[str]


# Hard leakage: things that absolutely should not appear in poem text.
# These are case-sensitive, mostly ALL CAPS or obviously systemy.
HARD_PHRASES = [
    "BEGIN POEM",
    "BEGIN OUTPUT",
    "BEGIN TASK",
    "BEGIN INSTRUCTION",
    "BEGIN RESPONSE",
    "END POEM",
    "END OUTPUT",
    "END TASK",
    "END INSTRUCTION",
    "END RESPONSE",
    "STRUCTURED_OUTPUT_INSTRUCTION",
    "JSON_SCHEMA",
    "REDLINE ARCHITECTURAL TRANSFORMATION SCHEMA",
    "RATS SCHEMA",
    "{STRUCTURED_OUTPUT_INSTRUCTION}",
    "{EDITORMODEL_JSON_EXAMPLE}",
    "{POETMODEL_JSON_EXAMPLE}",
]

# Hard patterns: regexes for command-like forms, all-caps markers, etc.
HARD_PATTERNS = [
    r"\bBEGIN\b\s*[:\-]",              # BEGIN: or BEGIN-
    r"\bEND\b\s*[:\-]",                # END: or END-
    r"```json",                        # fenced JSON blocks
    r"\bJSON\b",                       # raw JSON as token
    r"\bSCHEMA\b",                     # SCHEMA in all caps
    r"\bMODEL\b",                      # MODEL in all caps
    r"\bAGENT\b",                      # AGENT in all caps
    r"\bINSTRUCTION\b",                # INSTRUCTION in all caps
    r"\bOUTPUT\b\s*[:\-]",             # OUTPUT: / OUTPUT-
    r"\bPOEM VERSION\b",               # explicit version labels
]

# Soft leakage: pipeline / schema terms that *might* slip but could
# occasionally be used in weird poems. These are lowercase / mixed-case.
SOFT_PHRASES = [
    "poem version",
    "poetmodel",
    "architectmodel",
    "editormodel",
    "psychologistmodel",
    "muse_model",
    "gardener_model",
    "psychologist_notes",
    "architect_notes",
    "editor_notes",
    "seed id",
    "from_concept_id",
    "type\": \"poem",
    "type\": \"seed",
    "type\": \"psychologist_notes",
]


def classify_leakage(text: str) -> LeakageResult:
    """
    Classify leakage for a poem text.

    - Hard matches = explicit meta/system markers.
    - Soft matches = schema/pipeline echoes.

    Returns a LeakageResult with:
        level: "none" | "soft" | "hard"
        score: 1.0..0.0 (1.0 = clean)
    """
    if not text.strip():
        return LeakageResult(
            level="none",
            score=1.0,
            hard_matches=[],
            soft_matches=[],
        )

    hard_matches: List[str] = []
    soft_matches: List[str] = []

    # Case-sensitive scan for hard phrases (they're mostly ALL CAPS or templated)
    for phrase in HARD_PHRASES:
        if phrase in text:
            hard_matches.append(phrase)

    # Regex-based hard patterns
    for pattern in HARD_PATTERNS:
        if re.search(pattern, text):
            hard_matches.append(pattern)

    lowered = text.lower()

    # Soft phrases - compare in lowercase
    for phrase in SOFT_PHRASES:
        if phrase in lowered:
            soft_matches.append(phrase)

    # Deduplicate matches
    hard_matches = sorted(set(hard_matches))
    soft_matches = sorted(set(soft_matches))

    # Determine level
    if hard_matches:
        level: LeakageLevel = "hard"
    elif soft_matches:
        level = "soft"
    else:
        level = "none"

    # Compute score: hard hits are heavily penalised, soft hits lightly.
    # You can tweak these weights to taste.
    hard_count = len(hard_matches)
    soft_count = len(soft_matches)

    score = 1.0
    # Each hard match penalises by 0.4, capped at 0.8 total
    score -= min(0.8, 0.4 * hard_count)
    # Each soft match penalises by 0.1, capped at 0.3 total
    score -= min(0.3, 0.1 * soft_count)
    score = max(0.0, score)

    return LeakageResult(
        level=level,
        score=score,
        hard_matches=hard_matches,
        soft_matches=soft_matches,
    )


def leakage_for_poem(poem: Optional[Poem]) -> LeakageResult:
    """
    Convenience wrapper for poem objects.
    """
    if poem is None:
        return LeakageResult(
            level="none",
            score=1.0,
            hard_matches=[],
            soft_matches=[],
        )
    return classify_leakage(poem.text or "")

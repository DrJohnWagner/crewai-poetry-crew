# evaluation/metrics.py

from __future__ import annotations

import math
import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

from src.crewai_poetry_crew.utilities.models import Snapshot, Poem  # import your Pydantic types
from evaluation.snapshots import build_snapshots_from_json

# Import leakage classifier + types from external module
from evaluation.LeakageResult import (
    LeakageResult,
    LeakageLevel,
    HARD_PHRASES,
    HARD_PATTERNS,
    SOFT_PHRASES,
)
from evaluation.VersionMetrics import VersionMetrics


# ---------------------------------------------------------------------------
# Tokenisation / helpers
# ---------------------------------------------------------------------------

_WORD_RE = re.compile(r"\w+", re.UNICODE)


def _tokenize(text: str) -> List[str]:
    """Simple lowercase word tokenizer."""
    return [m.group(0).lower() for m in _WORD_RE.finditer(text or "")]


def lexical_delta(a: str, b: str) -> float:
    """
    0.0 = identical vocabulary
    1.0 = disjoint vocabulary (no shared tokens)

    Uses 1 - Jaccard(similarity) over word sets.
    """
    ta = set(_tokenize(a))
    tb = set(_tokenize(b))

    if not ta and not tb:
        return 0.0

    union = ta | tb
    inter = ta & tb

    return 1.0 - (len(inter) / len(union))


def structural_delta(a: str, b: str) -> float:
    """
    Rough structural difference metric based on:
      - line count difference
      - indentation (leading spaces) per line
    """
    lines_a = (a or "").splitlines()
    lines_b = (b or "").splitlines()

    if not lines_a and not lines_b:
        return 0.0

    len_a = len(lines_a)
    len_b = len(lines_b)
    max_len = max(len_a, len_b)

    # Line-count component
    line_count_component = abs(len_a - len_b) / max_len

    # Indentation component
    max_indent_diff = 0
    for i in range(max_len):
        la = lines_a[i] if i < len_a else ""
        lb = lines_b[i] if i < len_b else ""
        ia = len(la) - len(la.lstrip(" "))
        ib = len(lb) - len(lb.lstrip(" "))
        max_indent_diff = max(max_indent_diff, abs(ia - ib))

    indent_component = min(1.0, max_indent_diff / 8.0)

    return (line_count_component + indent_component) / 2.0


# ---------------------------------------------------------------------------
# Leakage wrapper (the real classifier is in LeakageResult.py)
# ---------------------------------------------------------------------------

def classify_leakage(text: str) -> LeakageResult:
    """
    Perform context-aware leakage detection using rules
    defined in LeakageResult.py.
    """
    if not text.strip():
        return LeakageResult(level="none", score=1.0,
                             hard_matches=[], soft_matches=[])

    hard_matches: List[str] = []
    soft_matches: List[str] = []

    # Hard phrase scan (case-sensitive)
    for phrase in HARD_PHRASES:
        if phrase in text:
            hard_matches.append(phrase)

    # Hard regex patterns
    for pattern in HARD_PATTERNS:
        if re.search(pattern, text):
            hard_matches.append(pattern)

    # Soft phrase scan (case-insensitive)
    lowered = text.lower()
    for phrase in SOFT_PHRASES:
        if phrase in lowered:
            soft_matches.append(phrase)

    # Deduplicate
    hard_matches = sorted(set(hard_matches))
    soft_matches = sorted(set(soft_matches))

    # Determine level
    if hard_matches:
        level: LeakageLevel = "hard"
    elif soft_matches:
        level = "soft"
    else:
        level = "none"

    # Score
    hard_count = len(hard_matches)
    soft_count = len(soft_matches)

    score = 1.0
    score -= min(0.8, 0.4 * hard_count)   # strong penalty
    score -= min(0.3, 0.1 * soft_count)   # weak penalty
    score = max(0.0, score)

    return LeakageResult(
        level=level,
        score=score,
        hard_matches=hard_matches,
        soft_matches=soft_matches,
    )


def leakage_for_poem(poem: Optional[Poem]) -> LeakageResult:
    """Safe wrapper for Poem objects."""
    if poem is None:
        return LeakageResult(level="none", score=1.0,
                             hard_matches=[], soft_matches=[])
    return classify_leakage(poem.text or "")


def _roles_present(snapshot: Snapshot) -> List[str]:
    roles: List[str] = []
    if snapshot.poet: roles.append("poet")
    if snapshot.psychologist: roles.append("psychologist")
    if snapshot.architect: roles.append("architect")
    if snapshot.editor: roles.append("editor")
    return roles


def evaluate_snapshots(snapshots: Dict[int, Snapshot]) -> Dict[str, object]:
    """
    Evaluate leakage, lexical change, structural change across versions.
    """
    if not snapshots:
        return {
            "versions": [],
            "global": {
                "final_poem_leakage_score": None,
                "final_poem_leakage_level": None,
                "avg_leakage_score": None,
                "avg_lexical_delta": None,
                "avg_structural_delta": None,
            },
        }

    version_ids = sorted(snapshots.keys())
    version_metrics: List[VersionMetrics] = []

    prev_poem: Optional[Poem] = None
    lexical_deltas: List[float] = []
    structural_deltas: List[float] = []
    leakage_scores: List[float] = []

    for vid in version_ids:
        snap = snapshots[vid]
        poem = snap.poem

        leakage_result = leakage_for_poem(poem)
        leakage_scores.append(leakage_result.score)

        # diffs from previous poem
        if prev_poem is not None and poem is not None:
            ld = lexical_delta(prev_poem.text or "", poem.text or "")
            sd = structural_delta(prev_poem.text or "", poem.text or "")
            lexical_deltas.append(ld)
            structural_deltas.append(sd)
        else:
            ld = None
            sd = None

        offenders = leakage_result.hard_matches + leakage_result.soft_matches

        vm = VersionMetrics(
            version=vid,
            roles=_roles_present(snap),
            leakage_score=leakage_result.score,
            leakage_level=leakage_result.level,
            leakage_offenders=offenders,
            lexical_delta_from_prev=ld,
            structural_delta_from_prev=sd,
        )
        version_metrics.append(vm)

        if poem:
            prev_poem = poem

    # Global summary
    final_poem = snapshots[version_ids[-1]].poem
    final_leak = leakage_for_poem(final_poem)

    avg_leak = sum(leakage_scores) / len(leakage_scores)
    avg_lex = sum(lexical_deltas) / len(lexical_deltas) if lexical_deltas else None
    avg_str = sum(structural_deltas) / len(structural_deltas) if structural_deltas else None

    return {
        "versions": [vm.as_dict() for vm in version_metrics],
        "global": {
            "final_poem_leakage_score": final_leak.score,
            "final_poem_leakage_level": final_leak.level,
            "final_poem_leakage_offenders": (
                final_leak.hard_matches + final_leak.soft_matches
            ),
            "avg_leakage_score": avg_leak,
            "avg_lexical_delta": avg_lex,
            "avg_structural_delta": avg_str,
        },
    }


# ---------------------------------------------------------------------------
# Convenience entry point
# ---------------------------------------------------------------------------

def evaluate_run_log(path: str | Path) -> Dict[str, object]:
    """Load a run log JSON → build snapshots → evaluate metrics."""
    snapshots = build_snapshots_from_json(path)
    return evaluate_snapshots(snapshots)

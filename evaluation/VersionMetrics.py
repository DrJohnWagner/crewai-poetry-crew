from __future__ import annotations

from typing import List, Optional

# Import leakage classifier + types from external module
from evaluation.LeakageResult import LeakageLevel

class VersionMetrics:
    """Lightweight container for per-version metrics."""

    def __init__(
        self,
        version: int,
        roles: List[str],
        leakage_score: float,
        leakage_level: LeakageLevel,
        leakage_offenders: List[str],
        lexical_delta_from_prev: Optional[float],
        structural_delta_from_prev: Optional[float],
    ) -> None:
        self.version = version
        self.roles = roles
        self.leakage_score = leakage_score
        self.leakage_level = leakage_level
        self.leakage_offenders = leakage_offenders
        self.lexical_delta_from_prev = lexical_delta_from_prev
        self.structural_delta_from_prev = structural_delta_from_prev

    def as_dict(self) -> dict:
        return {
            "version": self.version,
            "roles": self.roles,
            "leakage_score": self.leakage_score,
            "leakage_level": self.leakage_level,
            "leakage_offenders": self.leakage_offenders,
            "lexical_delta_from_prev": self.lexical_delta_from_prev,
            "structural_delta_from_prev": self.structural_delta_from_prev,
        }


from dataclasses import dataclass, field
from typing import List, Optional


@dataclass(frozen=True)
class MatchConfig:
    """
    Represents a match configuration that can be used to request matching at a match service.
    """
    match_function: Optional[str] = None
    match_mode: Optional[str] = None
    threshold: Optional[float] = None


@dataclass(frozen=True)
class MatchRequest:
    """
    Represents a request to match the domain bit strings against the range bit strings.
    """
    match_config: MatchConfig = field(default_factory=MatchConfig)
    domain: List[str] = field(default_factory=list)
    range: List[str] = field(default_factory=list)


@dataclass(frozen=True)
class Match:
    """
    Represents a match returned by the match service.
    """
    domain_vector: str
    range_vector: str
    confidence: float

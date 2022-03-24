from dataclasses import dataclass
from trading_platform.base import Base


@dataclass
class Quote(Base):

	symbol: str

	open: float

	close: float

	high: float

	low: float

	volume: int

	timestamp: int

from datetime import datetime
from dataclasses import dataclass
from trading_platform.base import Base


@dataclass
class Position(Base):

	id: int

	symbol: str

	quantity: int

	created_at: datetime

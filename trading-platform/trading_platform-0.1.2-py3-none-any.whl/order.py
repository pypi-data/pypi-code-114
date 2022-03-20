from datetime import datetime
from dataclasses import dataclass
from trading_platform.base import Base


@dataclass
class Order(Base):

	id: int

	symbol: str

	type: str

	status: str

	direction: str

	amount: float

	fill_price: float

	amount_after_fill: float

	quantity: int

	filled_at: datetime

	cancelled_at: datetime

	created_at: datetime

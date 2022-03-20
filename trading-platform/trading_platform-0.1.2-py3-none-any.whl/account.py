from datetime import datetime
from dataclasses import dataclass
from trading_platform.base import Base


@dataclass
class Account(Base):

	api_token: str

	balance: float

	pending_balance: float

	created_at: datetime
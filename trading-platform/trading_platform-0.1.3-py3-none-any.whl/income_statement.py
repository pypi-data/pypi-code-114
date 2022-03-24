from datetime import datetime
from dataclasses import dataclass
from trading_platform.base import Base


@dataclass
class IncomeStatement(Base):

	end_date: int

	total_revenue: int

	cost_of_revenue: int

	gross_profit: int

	research_development: int

	selling_general_administrative: int
	
	non_recurring: int

	other_operating_expenses: int

	total_operating_expenses: int

	operating_income: int

	total_other_income_expense_net: int

	ebit: int

	interest_expense: int

	income_before_tax: int

	income_tax_expense: int

	minority_interest: int

	net_income_from_continuing_ops: int

	discontinued_operations: int

	extraordinary_items: int

	effect_of_accounting_charges: int

	other_items: int

	net_income: int

	net_income_applicable_to_common_shares: int
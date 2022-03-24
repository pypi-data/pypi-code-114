from __future__ import annotations
import requests
from enum import Enum
from pprint import pprint
from typing import List

from trading_platform.income_statement import IncomeStatement
from trading_platform.order import Order
from trading_platform.account import Account
from trading_platform.position import Position
from trading_platform.quote import Quote


class Direction(Enum):
	BUY = "buy"
	SELL = "sell"


class Client:

	def __init__(self, base_url: str, api_token: str = None, api_version: str = "v1") -> None:
		self.base_url = base_url
		self.api_token = api_token
		self.api_version = api_version

	def __get_auth_header(self)-> dict:
		if self.api_token is None:
			raise Exception("Please supply api token")

		return {
			"Authorization": f"Bearer {self.api_token}"
		}

	def __validate_response(self, res)-> dict:
		if res.status_code != 200:
			raise Exception(f"Status code {res.status_code}")

		body = res.json()

		if body["success"] == False:
			msg = body["error"]
			raise Exception(f"Request error: {msg}")

		return body

	def set_api_token(self, api_token: str):
		self.api_token = api_token

	def place_order(self, symbol: str, direction: str, quantity: int, amount: float)-> Order:

		direction = Direction(direction.lower())

		payload = {
			"symbol": symbol.upper(),
			"amount": float(amount),
			"type": "limit",
			"direction": str(direction.value),
			"quantity": quantity
		}

		res = requests.post(
			f"{self.base_url}/api/{self.api_version}/order",
			json=payload,
			headers=self.__get_auth_header(),
		)

		body = self.__validate_response(res)

		order = body["order"]

		return Order(
			order["id"],
			order["symbol"],
			order["type"],
			order["status"],
			order["direction"],
			order["amount"],
			order["fill_price"],
			order["amount_after_fill"],
			order["quantity"],
			order["filled_at"] if "filled_at" in order else None,
			order["cancelled_at"] if "cancelled_at" in order else None,
			order["created_at"],
		)

	def get_orders(self) -> List[Order]:
		res = requests.get(
			f"{self.base_url}/api/{self.api_version}/orders",
			headers=self.__get_auth_header(),
		)

		body = self.__validate_response(res)

		orders = body["orders"]

		return [Order(
			order["id"],
			order["symbol"],
			order["type"],
			order["status"],
			order["direction"],
			order["amount"],
			order["fill_price"],
			order["amount_after_fill"],
			order["quantity"],
			order["filled_at"] if "filled_at" in order else None,
			order["cancelled_at"] if "cancelled_at" in order else None,
			order["created_at"],
		) for order in orders ]

	def open_account(self)-> Account:
		res = requests.post(f"{self.base_url}/api/{self.api_version}/account")

		body = self.__validate_response(res)

		account = body["account"]

		self.set_api_token(account["api_token"])

		return Account(
			account["api_token"],
			account["balance"],
			account["pending_balance"],
			account["created_at"]
		)

	def get_account(self)-> Account:

		res = requests.post(
			f"{self.base_url}/api/{self.api_version}/account",
			headers=self.__get_auth_header()
		)

		body = self.__validate_response(res)

		account = body["account"]

		return Account(
			account["api_token"],
			account["balance"],
			account["pending_balance"],
			account["created_at"]
		)

	def get_portfolio(self)-> List[Position]:
		res = requests.get(
			f"{self.base_url}/api/{self.api_version}/positions",
			headers=self.__get_auth_header()
		)

		body = self.__validate_response(res)

		positions = body["positions"]

		return [ Position(
			position["id"],
			position["symbol"],
			position["quantity"],
			position["created_at"]
		) for position in positions ]

	def get_historic_quotes(self, start: str, symbol: str)-> List[Quote]:

		res = requests.get(
			f"{self.base_url}/api/{self.api_version}/data/historic?start={start}&symbol={symbol}",
		)

		body = self.__validate_response(res)

		quotes = body["data"]

		return [ Quote(
			quote["symbol"],
			quote["open"],
			quote["close"],
			quote["high"],
			quote["low"],
			quote["volume"],
			quote["timestamp"],
		) for quote in quotes ]

	def get_income_statement_history_quarterly(self, symbol: str)-> List[IncomeStatement]:

		res = requests.get(
			f"{self.base_url}/api/{self.api_version}/fundamental/{symbol}/income-statement-history-quarterly",
		)

		body = self.__validate_response(res)

		data = body["data"]

		return [ IncomeStatement(
			d["endDate"],
			d["totalRevenue"],
			d["costOfRevenue"],
			d["grossProfit"],
			d["researchDevelopment"],
			d["sellingGeneralAdministrative"],
			d["nonRecurring"],
			d["otherOperatingExpenses"],
			d["totalOperatingExpenses"],
			d["operatingIncome"],
			d["totalOtherIncomeExpenseNet"],
			d["ebit"],
			d["interestExpense"],
			d["incomeBeforeTax"],
			d["incomeTaxExpense"],
			d["minorityInterest"],
			d["netIncomeFromContinuingOps"],
			d["discontinuedOperations"],
			d["extraordinaryItems"],
			d["effectOfAccountingCharges"],
			d["otherItems"],
			d["netIncome"],
			d["netIncomeApplicableToCommonShares"]
		) for d in data ]

if __name__ == "__main__":
	c = Client("http://192.168.1.17:8080")
	statements = c.get_income_statement_history_quarterly("aapl")
	pprint(statements)
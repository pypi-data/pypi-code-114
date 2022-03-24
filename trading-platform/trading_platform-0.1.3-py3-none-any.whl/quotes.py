from __future__ import annotations

import requests

from trading_platform.quote import QuoteCollection


class Quotes:
	def __init__(self, url: str) -> None:
		self.url = url

	def get_quotes(self, symbol: str, start: str, interval: str)-> QuoteCollection:
		try:
			response = requests.get(
				f"{self.url}/api/v1/data/historic?start={start}&symbol={symbol}"
			)

			body = response.json()

			if body["success"] is False:
				raise Exception(body["error"])
			
			return QuoteCollection(body["data"])

		except Exception as e:
			print(str(e))
			return None

if __name__ == "__main__":
	from pprint import pprint

	q = Quotes("http://localhost:8080")
	quotes = q.get_quotes("AAPL", "2022-01-01 20:00", "1m")

	pprint(quotes.to_dict())
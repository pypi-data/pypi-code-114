import json

from notebuild.tool.fastapi import add_api_routes, api_route
from notecoin.database.connect import RedisConnect
from notecoin.okex.server.const import account_account, market_tickers
from notecoin.strategy.domain import OkexCoin


class AutoSeller(RedisConnect):
    def __init__(self, prefix="/sell",  *args, **kwargs):
        self.usdt = 0
        self.coin_map = {}
        super(AutoSeller, self).__init__(prefix=prefix, *args, **kwargs)
        add_api_routes(self)

    def load_account(self):
        self.coin_map = {}
        data = account_account.get_value()

        for detail in data:
            if detail['ccy'] == 'USDT':
                self.usdt = float(detail['availBal'])
                continue
            coin = OkexCoin.instance_by_account(detail)
            if coin.money > 1:
                self.coin_map[coin.coin_id] = coin

    def update_price(self):
        data = json.loads(market_tickers.get_value().to_json(orient="records"))
        data_map = dict([(cin['instId'], cin['last']) for cin in data])
        for coin in self.coin_map.values():
            coin.price = float(data_map[coin.coin_id])

    def to_json(self):
        return {
            "res": round(self.usdt, 2),
            "coins": [coin.to_json() for coin in self.coin_map.values()]
        }

    @api_route("/update")
    def update_value(self, suffix=""):
        self.load_account()
        self.update_price()
        for coin in self.coin_map.values():
            coin.watch()
        return self.to_json()

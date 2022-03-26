from notebuild.tool.fastapi import add_api_routes, api_route
from notecoin.database.base import create_session
from notecoin.database.connect import RedisConnect
from notecoin.okex.database.client import OkexClientAccountBalance
from notecoin.okex.database.websocket import OkexSocketPublicTickers
from notecoin.strategy.domain import OkexCoin


class AutoSeller(RedisConnect):
    def __init__(self, prefix="/sell", *args, **kwargs):
        self.total = 0
        self.usdt = 0
        self.coin_map = {}
        self.session = create_session()
        super(AutoSeller, self).__init__(prefix=prefix, *args, **kwargs)
        add_api_routes(self)

    def load_account(self):
        self.coin_map = {}
        details = self.session.query(OkexClientAccountBalance).filter(OkexClientAccountBalance.eqUsd > 10).all()
        for _detail in details:
            detail = _detail.json()
            if detail['ccy'] == 'USDT':
                self.usdt = float(detail['availBal'])
                continue
            coin = OkexCoin.instance_by_account(detail)
            if coin.money > 1:
                self.coin_map[coin.coin_id] = coin

    def update_price(self):
        details = self.session.query(OkexSocketPublicTickers).all()
        data_map = dict([(detail.instId, detail.last) for detail in details])

        for coin in self.coin_map.values():
            coin.price = float(data_map[coin.coin_id])

    def to_json(self):
        self.total = self.usdt
        for coin in self.coin_map.values():
            self.total += coin.money

        return {
            "total": self.total,
            "res": round(self.usdt, 2),
            "coins": [coin.to_json() for coin in self.coin_map.values()]
        }

    @api_route("/update")
    def update_value(self, suffix=""):
        res = {}
        res['load'] = self.load_account()
        res['update_price'] = self.update_price()
        for coin in self.coin_map.values():
            coin.watch()

        res.extends(self.to_json())
        return res

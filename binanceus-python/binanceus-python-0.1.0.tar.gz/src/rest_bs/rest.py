from binance.spot import Spot
from typing import Optional
import logging
from typing import DefaultDict, Dict
from collections import defaultdict


class BsClient(Spot):
    def __init__(self,
                 api_key: Optional[str] = None,
                 api_secret: Optional[str] = None,
                 base_url: Optional[str] = "https://api.binance.us"):
        super().__init__(base_url=base_url, key=api_key, secret=api_secret)
        self._logger = logging.getLogger('root')

        # Setup Parameters
        self._account_balances: DefaultDict[str, Dict[str, float]] = defaultdict(dict)
        self._can_trade: bool = False
        self._maker_fee: int = 0
        self._taker_fee: int = 0

    def setup(self):
        self._load_account_info()

    def _load_account_info(self, recvWindow: Optional[str] = 60000):
        info = super().account(recvWindow=recvWindow)
        self._maker_fee = info['makerCommission']
        self._taker_fee = info['takerCommission']
        self._can_trade = info['canTrade']

        for coin in info['balances']:
            asset = coin['asset']
            del coin['asset']
            for key, val in coin.items():
                coin[key] = float(val)
            self._account_balances[asset].update(coin)

    def get_account_balances(self):
        return self._account_balances

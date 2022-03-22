from collections import defaultdict
from typing import DefaultDict, List, Dict, Set, Optional
import time
import logging

from binance.websocket.spot.websocket_client import SpotWebsocketClient

# TODO: data structure reset upon new connection
# TODO: add logging support


class BsWebsocketClient(SpotWebsocketClient):
    def __init__(self, steam_url: Optional[str] = "wss://stream.binance.us:9443"):
        super().__init__(stream_url=steam_url)

        # Setup Parameters
        self._book_tops: DefaultDict[str, List[float]] = defaultdict(lambda: [0, 0, 0, 0])
        self._orderbook_timestamps: DefaultDict[str, float] = defaultdict(float)
        self._orderbook_timestamps.clear()
        self._subscriptions: Set[str] = set()
        self._account_balances: DefaultDict[str, Dict[str, float]] = defaultdict(dict)
        self._logger = logging.getLogger('root')

    def _handle_book_top_message(self, message: Dict) -> None:
        if len(message) != 6:
            return
        else:
            symbol = message['s']
            bid = float(message['b'])
            bid_qty = float(message['B'])
            ask = float(message['a'])
            ask_qty = float(message['A'])
            self._book_tops[symbol] = [bid, bid_qty, ask, ask_qty]
            self._orderbook_timestamps[symbol] = time.time()

    def _handle_account_update_message(self, message: Dict) -> None:
        raise NotImplementedError()  # TODO: Handle account updates thru websockets

    def subscribe_user_data(self, listen_key: str):
        raise NotImplementedError()  # TODO: account updates

    def subscribe(self, symbol: str) -> None:
        """Subscribe to real-time updates to the best bid or ask's price or quantity for a specified symbol.
        https://docs.binance.us/?python#ticker-streams

        Args:
            symbol: str
                Symbol to subscribe to. Use uppercase, ex. BTCUSD
        """
        self.book_ticker(
            symbol=symbol,
            id=len(self._subscriptions) + 1,
            callback=self._handle_book_top_message
        )
        self._logger.info(f"BinanceUS: Subscribed to orderbook top for symbol: {symbol}")
        self._subscriptions.add(symbol)

    def unsubscribe(self, symbol: str):
        raise NotImplementedError()

    def get_book_top(self, symbol: str) -> List[float]:
        """Returns top bid and ask for a given symbol."""
        assert symbol in self._subscriptions, f"You are not subscribed to symbol {symbol}"
        return self._book_tops[symbol]

    def get_book_timestamp(self, symbol: str) -> float:
        """Returns local-time timestamp of last orderbook update for a given symbol."""
        return self._orderbook_timestamps[symbol]
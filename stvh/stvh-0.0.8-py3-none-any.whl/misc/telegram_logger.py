from datetime import datetime
from typing import Any, Callable, Optional

import requests


class TelegramLogger:
    def __init__(
        self,
        token: str,
        chat_id: str,
        callback: Optional[Callable[[str], Any]],
    ) -> None:
        """TODO

        Args:
            token (str):
            chat_id (str):
        """
        self._url: str = f"https://api.telegram.org/bot{token}/sendMessage"
        self._chat_id: str = chat_id
        self._callback: Optional[Callable[[str], Any]] = callback
        self._msgs: list[str] = []

    def add(self, msg: str) -> None:
        """TODO

        Args:
            msg (str):
        """
        self._msgs.append(TelegramLogger.format_msg(msg))

        if self._callback is not None:
            self._callback(msg)

    def flush(self) -> None:
        """TODO"""
        if len(self._msgs) == 0:
            return

        resp = requests.post(
            url=self._url,
            params={
                "chat_id": self._chat_id,
                "text": "\n".join(self._msgs),
            },
        )
        resp.raise_for_status()  # what is the purpose of this line?
        del self._msgs[:]

    def send(self, msg: str) -> None:
        """TODO

        Args:
            msg (str):
        """
        self.add(msg)
        self.flush()

    @staticmethod
    def format_msg(msg: str) -> str:
        """TODO

        Args:
            msg (str):

        Returns:
        """
        return f"[{datetime.now().strftime('%b %d %H:%M:%S')}]\n{msg}"

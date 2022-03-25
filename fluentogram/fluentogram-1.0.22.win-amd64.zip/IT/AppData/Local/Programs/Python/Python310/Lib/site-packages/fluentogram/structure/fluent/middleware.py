# coding=utf-8
"""
Translator Middleware for aiogram3.
"""

from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import Message

from fluentogram.structure.fluent import TranslatorHub, TranslatorRunner


class I18nMiddleware(BaseMiddleware):
    """Middleware, creates a Translator Runner instance and pulling into the message context,
    Look for an i18n object in the handler, like:

    def ...handler(message: Message, ..., i18n: TranslatorRunner): ...
    """

    def __init__(self, translator_hub_alias: str = "translator_hub", translator_alias: str = "i18n") -> None:
        self._hub_alias = translator_hub_alias
        self._alias = translator_alias

    async def __call__(
            self,
            handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
            event: Message,
            data: Dict[str, Any]
    ) -> Any:
        translator_hub: TranslatorHub = data.get(self._hub_alias)
        if translator_hub:
            data[self._alias]: TranslatorRunner = translator_hub.get_translator_by_locale(event.from_user.language_code)
        return await handler(event, data)

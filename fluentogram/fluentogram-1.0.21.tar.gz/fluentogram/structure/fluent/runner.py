# coding=utf-8
"""
A translator runner by itself
"""
from typing import TypeVar, List

from fluentogram.structure.fluent import FluentTranslator
from fluentogram.structure.fluent.attrib_tracer import AttribTracer

TTranslatorRunner = TypeVar("TTranslatorRunner", bound="TranslatorRunner")


class TranslatorRunner(AttribTracer):
    """This is one-shot per Telegram event translator with attrib tracer access way."""

    def __init__(self, translators: List[FluentTranslator]) -> None:
        super().__init__()
        self.translators = translators
        self.request_line = ""

    def get(self, key: str, **kwargs) -> str:
        """Faster, direct way to use translator, without sugar-like typing supported attribute access way"""
        self.request_line = key
        return self.__call__(**kwargs)

    def __call__(self, **kwargs) -> str:
        for translator in self.translators:
            try:
                text = translator.get(self.request_line[:-1], **kwargs)
                self.request_line = ""
                return text
            except KeyError:
                continue

    def __getattr__(self, item: str) -> TTranslatorRunner:
        self.request_line += f"{item}{self.translators[0].separator}"
        return self

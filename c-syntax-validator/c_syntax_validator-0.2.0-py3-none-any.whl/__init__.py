from enum import Enum
import io

import antlr4

from .parser.CLexer import CLexer
from .parser.CParser import CParser


class InputTarget(Enum):
    EXPRESSION = "expr"
    STATEMENT = "stmt"
    BLOCK_BODY = "block-body"
    FILE = "file"


class InvalidCodeException(Exception):
    reasons: list[str]

    def __init__(self, reasons: list[str]):
        super().__init__("Invalid code")
        assert reasons, "Empty reasons"
        self.reasons = reasons

    def __str__(self):
        return "\n".join(self.reasons)


class ValidatorErrorListener(antlr4.error.ErrorListener.ErrorListener):
    msgs: list[str]

    def __init__(self):
        self.msgs = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        self.msgs.append(f"line {line}:{column} {msg}")


def validate_text(text: str, target: InputTarget):
    assert isinstance(text, str)
    return _validate_antlr_input_stream(antlr4.InputStream(text), target)


def _validate_antlr_input_stream(stream: antlr4.InputStream, target: InputTarget):
    assert isinstance(stream, antlr4.InputStream)
    assert isinstance(target, InputTarget)
    lexer = CLexer(stream)
    tokens = antlr4.CommonTokenStream(lexer)
    parser = CParser(tokens)
    listener = ValidatorErrorListener()
    parser.removeErrorListeners()
    parser.addErrorListener(listener)
    if target == InputTarget.EXPRESSION:
        parser.expression()
    elif target == InputTarget.STATEMENT:
        parser.statement()
    elif target == InputTarget.BLOCK_BODY:
        parser.blockItemList()
    elif target == InputTarget.FILE:
        parser.compilationUnit()
    else:
        raise AssertionError(str(target))

    if listener.msgs:
        raise InvalidCodeException(listener.msgs)

from dataclasses import dataclass

from jsons import JsonSerializable, KEY_TRANSFORMER_LISPCASE, KEY_TRANSFORMER_SNAKECASE

@dataclass
class PingResponseBody(JsonSerializable):
    version: str

@dataclass
class PingErrorBody(JsonSerializable):
    error: str


class ClipboardText(JsonSerializable):
    def __init__(self, text: str):
        if (not text) or (text.strip() == ''):            
            self.text = None
        else:
            self.text = text

@dataclass
class ClipboardCopyRequest(JsonSerializable):
    copy: ClipboardText
@dataclass
class ClipboardRequestBody(JsonSerializable
        .with_dump(key_transformer=KEY_TRANSFORMER_LISPCASE)
        .with_load(key_transformer=KEY_TRANSFORMER_SNAKECASE)):
    clipboard_request: ClipboardCopyRequest


@dataclass
class ClipboardContent(JsonSerializable):
    content: ClipboardText
    error: str
@dataclass
class ClipboardResponseBody(JsonSerializable.with_dump(strip_nulls=True)):
    clipboard: ClipboardContent

def clipboard_content_response(text):
    return ClipboardResponseBody(ClipboardContent(ClipboardText(text), None))

def clipboard_error_response(error_message):
    return ClipboardResponseBody(ClipboardContent(None, error_message))

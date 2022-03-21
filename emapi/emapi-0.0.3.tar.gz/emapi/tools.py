import re
from typing import Callable
from inspect import getdoc, signature

from .constants import OPENAPI_FIELDS

TITLE_TO_SNAKE = re.compile(r"(?<!^)(?=[A-Z])")


def format_field(name: str, description: str, default: str, typ: str) -> dict:
	field = {"name": name, "description": description, "default": default}
	for k, v in zip(("type", "format"), OPENAPI_FIELDS.get(typ, (typ,))):
		field[k] = v
	return field


def get_method_signature_data(m: Callable) -> dict:
	param_regex = re.compile(":param (.*):(.*)")
	ret = {}
	sig = signature(m)
	doc = getdoc(m)
	for p in (doc or "").split("\n"):
		r = param_regex.search(p)
		if r:
			arg_name = r.group(1)
			f = sig.parameters[arg_name]
			ret[arg_name] = format_field(
				arg_name, r.group(2).strip(), f.default.__name__ if not f.default == f.empty else None, f.annotation.__name__
			)
	return ret


def title_to_snake(val: str) -> str:
	return TITLE_TO_SNAKE.sub("_", val).lower()

"""Dict utils like attr and dot-notation access."""
import copy

__all__ = [
    "AttrDict",
    "attrify",
    "flatten_dotdict",
    "inflate_dotdict",
    "get_field",
]


class AttrDict(dict):
    """Dictionary exposing keys as attributes and dot-notated key support."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize AttrDict from nested or dot-notated fields."""
        # always inflate dot-notation to deep nesting
        data = copy.deepcopy(inflate_dotdict(dict(*args, **kwargs)))
        # avoid recursion by attrifying the values instead of the top-level dict
        dict.__init__(self, {k: attrify(v) for k, v in data.items()})

    def get(self, name: str, default=None):
        """Get value for a dict key or return default - supports dot-notation."""
        try:
            return self[name]
        except KeyError:
            return default

    def __getitem__(self, name: str):
        """Get value for a dict key - supports dot-notation."""
        node = self
        for part in name.split("."):
            node = dict.__getitem__(node, part)
        return node

    def __setitem__(self, name: str, value) -> None:
        """Set value for a dict key - supports dot-notation."""
        node = self
        *parts, last = name.split(".")
        for part in parts:
            node = dict.setdefault(node, part, AttrDict())
        dict.__setitem__(node, last, attrify(value))

    def __getattr__(self, name: str):
        """Get attr by name - same as dict key access."""
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name) from None

    def __setattr__(self, name: str, value) -> None:
        """Set attr by name - does not support dot-notation."""
        self[name] = value

    def flat(self) -> dict:
        """Return nested dicts flattened using dot-notation."""
        return flatten_dotdict(self)


def attrify(data):
    """Return data with dicts cast to AttrDict for dot notation access."""
    if isinstance(data, dict):
        return AttrDict((key, value) for key, value in data.items())
    if isinstance(data, list):
        return [attrify(elem) for elem in data]
    return data


def flatten_dotdict(deep: dict, prefix: str = "") -> dict:
    """Flatten dictionary using dot-notation: {a: b: c} => {a.b: c}."""
    flat = {}
    for key, value in deep.items():
        key = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(flatten_dotdict(value, prefix=key))
        else:
            flat[key] = value
    return flat


def inflate_dotdict(flat: dict) -> dict:
    """Inflate flat dot-notation dictionary: {a.b: c} => {a: b: c}."""
    deep = node = {}  # type: ignore
    for key, value in flat.items():
        parts = key.split(".")
        path, key = parts[:-1], parts[-1]
        for part in path:
            node = node.setdefault(part, {})
        node[key] = value
        node = deep
    return deep


def get_field(obj, field: str):
    """Return an object's key/attr with support for nesting/dot-notation."""
    # dot-notated
    try:
        return obj[field]
    except (TypeError, KeyError):
        pass
    try:
        return getattr(obj, field)
    except AttributeError as exc:
        if f"object has no attribute {field!r}" not in exc.args[0]:
            raise
    # nested
    node = obj
    for part in field.split("."):
        try:
            node = node[part]
            continue  # pragma: no cover
        except (TypeError, KeyError):
            pass
        try:
            node = getattr(node, part)
            continue
        except AttributeError as exc:
            if f"object has no attribute {part!r}" not in exc.args[0]:
                raise
        return None
    return node  # pragma: no cover

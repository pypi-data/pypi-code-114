"""templating"""

from collections.abc import Iterable, Iterator, Callable
from typing import Union, Any, Generic, TypeVar
from functools import wraps
from fractions import Fraction
import ast

from ...model import Ingredient, IngredientGroup, AmountRange


def load_text_file(path: str) -> str:
    with open(path, encoding="utf-8") as f:
        return f.read()


def fill_template(template: str, env: dict[str, Any]) -> str:
    while True:
        try:
            marker = next(find_placeholders(template))
        except StopIteration:
            break
        value = eval_restricted(marker.strip(), env)
        template = template.replace("{{" + marker + "}}", format_value(value))
    return template


def format_value(val: Any) -> str:
    if val is None:
        return ""
    if val == Fraction(1, 2):
        return "½"
    if val == Fraction(1, 4):
        return "¼"
    if val == Fraction(3, 4):
        return "¾"
    return f"{val}"


def find_placeholders(s: str, start: int = 0) -> Iterator[str]:
    start_seq = "{{"
    while (pos := s.find(start_seq, start)) != -1:
        pos += len(start_seq)
        end_pos = s.find("}}", pos)
        if end_pos == -1:
            raise ValueError(
                f"No closing }}}} for placeholder starting with '{s[pos:pos+10]}'"
            )
        if s[pos] == ".":
            pos += 1
        span = slice(pos, end_pos)
        yield s[span]
        start = span.stop


T = TypeVar("T")


class FallbackValue(Generic[T]):
    """When :eval_restricted: hits instances of this class,
    it will immediately return the contained value."""

    def __init__(self, value: T):
        self.value = value

    def __getattribute__(self, attribute: str) -> "FallbackValue[T]":
        return self

    def __getitem__(self, key: Union[str, int]) -> "FallbackValue[T]":
        return self


R = TypeVar("R")
S = TypeVar("S")


def accept_fallback_value(
    f: Callable[[T], R]
) -> Callable[[Union[T, FallbackValue[S]]], Union[R, FallbackValue[S]]]:
    @wraps(f)
    def wrapped(obj: Union[T, FallbackValue[S]]) -> Union[R, FallbackValue[S]]:
        if isinstance(obj, FallbackValue):
            return obj
        return f(obj)

    return wrapped


def eval_restricted(
    expression: str,
    environment: dict[str, Any],
) -> Any:
    compiled_expression = compile_expression(
        expression,
        allowed_ast_types=(
            ast.Call,
            ast.Attribute,
            ast.Subscript,
            ast.Name,
            ast.Constant,
            ast.GeneratorExp,
            ast.comprehension,
            ast.UnaryOp,
            ast.BinOp,
            ast.Add,
            ast.Not,
            ast.Load,
            ast.Store,
        ),
    )
    result = eval_without_builtins(compiled_expression, environment)
    if isinstance(result, FallbackValue):
        # __getattribute__ is overridden:
        return object.__getattribute__(result, "value")
    return result


def eval_without_builtins(expression: Any, environment: dict[str, Any]) -> Any:
    return eval(  # pylint: disable=eval-used
        expression, {**environment, "__builtins__": {}}
    )


def compile_expression(expression: str, allowed_ast_types: tuple[type, ...]) -> Any:
    if len(expression) > 120:
        raise ValueError("Expression too long (>=120 chars)")
    tree = ast.parse(expression)
    (expr,) = tree.body
    if not isinstance(expr, ast.Expr):
        raise ValueError("Only expressions are allowed")
    for node in ast.walk(expr.value):
        if not isinstance(node, allowed_ast_types):
            raise ValueError(
                f"{type(node).__name__}: not allowed in restricted expressions.\nOriginal expression: {expression}"
            )
        if isinstance(node, ast.Attribute) and node.attr.startswith("_"):
            raise ValueError("Accessing attributes starting with '_' is not allowed")
    return compile(ast.Expression(expr.value), "<string>", "eval", dont_inherit=True)


NO_DEFAULT = object()


def dict_selector(
    expression: str, default: Any = NO_DEFAULT
) -> Callable[[dict[str, Any]], Any]:
    compiled_expression = compile_expression(
        expression,
        allowed_ast_types=(
            ast.Attribute,
            ast.Subscript,
            ast.Name,
            ast.Constant,
            ast.Dict,
            ast.Load,
            ast.Call,
            ast.BinOp,
            ast.Add,
        ),
    )

    if default is NO_DEFAULT:

        def select(obj: dict[str, Any]) -> Any:
            return eval_without_builtins(compiled_expression, obj)

        return select

    def select_default(obj: dict[str, Any]) -> Any:
        try:
            return eval_without_builtins(compiled_expression, obj)
        except (AttributeError, KeyError, IndexError):
            return default

    return select_default


def class_selector(expression: str, default: Any = NO_DEFAULT) -> Callable[[Any], Any]:
    selector = dict_selector("obj." + expression, default)

    def wrapped_selector(obj: Any) -> Any:
        return selector({"obj": obj})

    return wrapped_selector


def fmt_ingredients(
    ingredients: list[Union[Ingredient, IngredientGroup]]
) -> Union[str, FallbackValue[Any]]:
    def format_parts(
        ingredients: list[Union[Ingredient, IngredientGroup]]
    ) -> Iterable[str]:
        for item in ingredients:
            if isinstance(item, Ingredient):
                yield format_ingredient(item)
            elif isinstance(item, IngredientGroup):
                yield item.name
                yield from (
                    "\t" + format_ingredient(subitem) for subitem in item.ingredients
                )
            else:
                raise ValueError(
                    f"Invalid item of type {type(item).__name__} in ingredient list"
                )

    return "\n".join(format_parts(ingredients))


def format_amount(amount: Union[Fraction, AmountRange]) -> str:
    if isinstance(amount, Fraction):
        return f"{amount}"
    return f"{amount.min}-{amount.max}"


def format_ingredient(ingredient: Ingredient) -> str:
    parts = (
        format_amount(ingredient.amount) if ingredient.amount is not None else None,
        ingredient.unit,
        ingredient.name,
    )

    return " ".join(part for part in parts if part is not None)

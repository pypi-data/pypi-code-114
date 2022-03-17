import collections.abc
import inspect
import warnings
from typing import Any
from typing import Callable
from typing import Collection
from typing import Iterable
from typing import Iterator
from typing import List
from typing import Mapping
from typing import MutableMapping
from typing import NamedTuple
from typing import Optional
from typing import overload
from typing import Sequence
from typing import Set
from typing import Tuple
from typing import Type
from typing import TYPE_CHECKING
from typing import TypeVar
from typing import Union

import attr

from .._code import getfslineno
from ..compat import ascii_escaped
from ..compat import final
from ..compat import NOTSET
from ..compat import NotSetType
from _pytest.config import Config
from _pytest.deprecated import check_ispytest
from _pytest.outcomes import fail
from _pytest.warning_types import PytestUnknownMarkWarning

if TYPE_CHECKING:
    from ..nodes import Node


EMPTY_PARAMETERSET_OPTION = "empty_parameter_set_mark"


def istestfunc(func) -> bool:
    return callable(func) and getattr(func, "__name__", "<lambda>") != "<lambda>"


def get_empty_parameterset_mark(
    config: Config, argnames: Sequence[str], func
) -> "MarkDecorator":
    from ..nodes import Collector

    fs, lineno = getfslineno(func)
    reason = "got empty parameter set %r, function %s at %s:%d" % (
        argnames,
        func.__name__,
        fs,
        lineno,
    )

    requested_mark = config.getini(EMPTY_PARAMETERSET_OPTION)
    if requested_mark in ("", None, "skip"):
        mark = MARK_GEN.skip(reason=reason)
    elif requested_mark == "xfail":
        mark = MARK_GEN.xfail(reason=reason, run=False)
    elif requested_mark == "fail_at_collect":
        f_name = func.__name__
        _, lineno = getfslineno(func)
        raise Collector.CollectError(
            "Empty parameter set in '%s' at line %d" % (f_name, lineno + 1)
        )
    else:
        raise LookupError(requested_mark)
    return mark


class ParameterSet(NamedTuple):
    values: Sequence[Union[object, NotSetType]]
    marks: Collection[Union["MarkDecorator", "Mark"]]
    id: Optional[str]

    @classmethod
    def param(
        cls,
        *values: object,
        marks: Union["MarkDecorator", Collection[Union["MarkDecorator", "Mark"]]] = (),
        id: Optional[str] = None,
    ) -> "ParameterSet":
        if isinstance(marks, MarkDecorator):
            marks = (marks,)
        else:
            assert isinstance(marks, collections.abc.Collection)

        if id is not None:
            if not isinstance(id, str):
                raise TypeError(f"Expected id to be a string, got {type(id)}: {id!r}")
            id = ascii_escaped(id)
        return cls(values, marks, id)

    @classmethod
    def extract_from(
        cls,
        parameterset: Union["ParameterSet", Sequence[object], object],
        force_tuple: bool = False,
    ) -> "ParameterSet":
        """Extract from an object or objects.

        :param parameterset:
            A legacy style parameterset that may or may not be a tuple,
            and may or may not be wrapped into a mess of mark objects.

        :param force_tuple:
            Enforce tuple wrapping so single argument tuple values
            don't get decomposed and break tests.
        """

        if isinstance(parameterset, cls):
            return parameterset
        if force_tuple:
            return cls.param(parameterset)
        else:
            # TODO: Refactor to fix this type-ignore. Currently the following
            # passes type-checking but crashes:
            #
            #   @pytest.mark.parametrize(('x', 'y'), [1, 2])
            #   def test_foo(x, y): pass
            return cls(parameterset, marks=[], id=None)  # type: ignore[arg-type]

    @staticmethod
    def _parse_parametrize_args(
        argnames: Union[str, List[str], Tuple[str, ...]],
        argvalues: Iterable[Union["ParameterSet", Sequence[object], object]],
        *args,
        **kwargs,
    ) -> Tuple[Union[List[str], Tuple[str, ...]], bool]:
        if not isinstance(argnames, (tuple, list)):
            argnames = [x.strip() for x in argnames.split(",") if x.strip()]
            force_tuple = len(argnames) == 1
        else:
            force_tuple = False
        return argnames, force_tuple

    @staticmethod
    def _parse_parametrize_parameters(
        argvalues: Iterable[Union["ParameterSet", Sequence[object], object]],
        force_tuple: bool,
    ) -> List["ParameterSet"]:
        return [
            ParameterSet.extract_from(x, force_tuple=force_tuple) for x in argvalues
        ]

    @classmethod
    def _for_parametrize(
        cls,
        argnames: Union[str, List[str], Tuple[str, ...]],
        argvalues: Iterable[Union["ParameterSet", Sequence[object], object]],
        func,
        config: Config,
        nodeid: str,
    ) -> Tuple[Union[List[str], Tuple[str, ...]], List["ParameterSet"]]:
        argnames, force_tuple = cls._parse_parametrize_args(argnames, argvalues)
        parameters = cls._parse_parametrize_parameters(argvalues, force_tuple)
        del argvalues

        if parameters:
            # Check all parameter sets have the correct number of values.
            for param in parameters:
                if len(param.values) != len(argnames):
                    msg = (
                        '{nodeid}: in "parametrize" the number of names ({names_len}):\n'
                        "  {names}\n"
                        "must be equal to the number of values ({values_len}):\n"
                        "  {values}"
                    )
                    fail(
                        msg.format(
                            nodeid=nodeid,
                            values=param.values,
                            names=argnames,
                            names_len=len(argnames),
                            values_len=len(param.values),
                        ),
                        pytrace=False,
                    )
        else:
            # Empty parameter set (likely computed at runtime): create a single
            # parameter set with NOTSET values, with the "empty parameter set" mark applied to it.
            mark = get_empty_parameterset_mark(config, argnames, func)
            parameters.append(
                ParameterSet(values=(NOTSET,) * len(argnames), marks=[mark], id=None)
            )
        return argnames, parameters


@final
@attr.s(frozen=True, init=False, auto_attribs=True)
class Mark:
    #: Name of the mark.
    name: str
    #: Positional arguments of the mark decorator.
    args: Tuple[Any, ...]
    #: Keyword arguments of the mark decorator.
    kwargs: Mapping[str, Any]

    #: Source Mark for ids with parametrize Marks.
    _param_ids_from: Optional["Mark"] = attr.ib(default=None, repr=False)
    #: Resolved/generated ids with parametrize Marks.
    _param_ids_generated: Optional[Sequence[str]] = attr.ib(default=None, repr=False)

    def __init__(
        self,
        name: str,
        args: Tuple[Any, ...],
        kwargs: Mapping[str, Any],
        param_ids_from: Optional["Mark"] = None,
        param_ids_generated: Optional[Sequence[str]] = None,
        *,
        _ispytest: bool = False,
    ) -> None:
        """:meta private:"""
        check_ispytest(_ispytest)
        # Weirdness to bypass frozen=True.
        object.__setattr__(self, "name", name)
        object.__setattr__(self, "args", args)
        object.__setattr__(self, "kwargs", kwargs)
        object.__setattr__(self, "_param_ids_from", param_ids_from)
        object.__setattr__(self, "_param_ids_generated", param_ids_generated)

    def _has_param_ids(self) -> bool:
        return "ids" in self.kwargs or len(self.args) >= 4

    def combined_with(self, other: "Mark") -> "Mark":
        """Return a new Mark which is a combination of this
        Mark and another Mark.

        Combines by appending args and merging kwargs.

        :param Mark other: The mark to combine with.
        :rtype: Mark
        """
        assert self.name == other.name

        # Remember source of ids with parametrize Marks.
        param_ids_from: Optional[Mark] = None
        if self.name == "parametrize":
            if other._has_param_ids():
                param_ids_from = other
            elif self._has_param_ids():
                param_ids_from = self

        return Mark(
            self.name,
            self.args + other.args,
            dict(self.kwargs, **other.kwargs),
            param_ids_from=param_ids_from,
            _ispytest=True,
        )


# A generic parameter designating an object to which a Mark may
# be applied -- a test function (callable) or class.
# Note: a lambda is not allowed, but this can't be represented.
Markable = TypeVar("Markable", bound=Union[Callable[..., object], type])


@attr.s(init=False, auto_attribs=True)
class MarkDecorator:
    """A decorator for applying a mark on test functions and classes.

    ``MarkDecorators`` are created with ``pytest.mark``::

        mark1 = pytest.mark.NAME              # Simple MarkDecorator
        mark2 = pytest.mark.NAME(name1=value) # Parametrized MarkDecorator

    and can then be applied as decorators to test functions::

        @mark2
        def test_function():
            pass

    When a ``MarkDecorator`` is called, it does the following:

    1. If called with a single class as its only positional argument and no
       additional keyword arguments, it attaches the mark to the class so it
       gets applied automatically to all test cases found in that class.

    2. If called with a single function as its only positional argument and
       no additional keyword arguments, it attaches the mark to the function,
       containing all the arguments already stored internally in the
       ``MarkDecorator``.

    3. When called in any other case, it returns a new ``MarkDecorator``
       instance with the original ``MarkDecorator``'s content updated with
       the arguments passed to this call.

    Note: The rules above prevent a ``MarkDecorator`` from storing only a
    single function or class reference as its positional argument with no
    additional keyword or positional arguments. You can work around this by
    using `with_args()`.
    """

    mark: Mark

    def __init__(self, mark: Mark, *, _ispytest: bool = False) -> None:
        """:meta private:"""
        check_ispytest(_ispytest)
        self.mark = mark

    @property
    def name(self) -> str:
        """Alias for mark.name."""
        return self.mark.name

    @property
    def args(self) -> Tuple[Any, ...]:
        """Alias for mark.args."""
        return self.mark.args

    @property
    def kwargs(self) -> Mapping[str, Any]:
        """Alias for mark.kwargs."""
        return self.mark.kwargs

    @property
    def markname(self) -> str:
        """:meta private:"""
        return self.name  # for backward-compat (2.4.1 had this attr)

    def with_args(self, *args: object, **kwargs: object) -> "MarkDecorator":
        """Return a MarkDecorator with extra arguments added.

        Unlike calling the MarkDecorator, with_args() can be used even
        if the sole argument is a callable/class.
        """
        mark = Mark(self.name, args, kwargs, _ispytest=True)
        return MarkDecorator(self.mark.combined_with(mark), _ispytest=True)

    # Type ignored because the overloads overlap with an incompatible
    # return type. Not much we can do about that. Thankfully mypy picks
    # the first match so it works out even if we break the rules.
    @overload
    def __call__(self, arg: Markable) -> Markable:  # type: ignore[misc]
        pass

    @overload
    def __call__(self, *args: object, **kwargs: object) -> "MarkDecorator":
        pass

    def __call__(self, *args: object, **kwargs: object):
        """Call the MarkDecorator."""
        if args and not kwargs:
            func = args[0]
            is_class = inspect.isclass(func)
            if len(args) == 1 and (istestfunc(func) or is_class):
                store_mark(func, self.mark)
                return func
        return self.with_args(*args, **kwargs)


def get_unpacked_marks(obj: object) -> Iterable[Mark]:
    """Obtain the unpacked marks that are stored on an object."""
    mark_list = getattr(obj, "pytestmark", [])
    if not isinstance(mark_list, list):
        mark_list = [mark_list]
    return normalize_mark_list(mark_list)


def normalize_mark_list(
    mark_list: Iterable[Union[Mark, MarkDecorator]]
) -> Iterable[Mark]:
    """
    Normalize an iterable of Mark or MarkDecorator objects into a list of marks
    by retrieving the `mark` attribute on MarkDecorator instances.

    :param mark_list: marks to normalize
    :returns: A new list of the extracted Mark objects
    """
    for mark in mark_list:
        mark_obj = getattr(mark, "mark", mark)
        if not isinstance(mark_obj, Mark):
            raise TypeError(f"got {repr(mark_obj)} instead of Mark")
        yield mark_obj


def store_mark(obj, mark: Mark) -> None:
    """Store a Mark on an object.

    This is used to implement the Mark declarations/decorators correctly.
    """
    assert isinstance(mark, Mark), mark
    # Always reassign name to avoid updating pytestmark in a reference that
    # was only borrowed.
    obj.pytestmark = [*get_unpacked_marks(obj), mark]


# Typing for builtin pytest marks. This is cheating; it gives builtin marks
# special privilege, and breaks modularity. But practicality beats purity...
if TYPE_CHECKING:
    from _pytest.scope import _ScopeName

    class _SkipMarkDecorator(MarkDecorator):
        @overload  # type: ignore[override,misc]
        def __call__(self, arg: Markable) -> Markable:
            ...

        @overload
        def __call__(self, reason: str = ...) -> "MarkDecorator":
            ...

    class _SkipifMarkDecorator(MarkDecorator):
        def __call__(  # type: ignore[override]
            self,
            condition: Union[str, bool] = ...,
            *conditions: Union[str, bool],
            reason: str = ...,
        ) -> MarkDecorator:
            ...

    class _XfailMarkDecorator(MarkDecorator):
        @overload  # type: ignore[override,misc]
        def __call__(self, arg: Markable) -> Markable:
            ...

        @overload
        def __call__(
            self,
            condition: Union[str, bool] = ...,
            *conditions: Union[str, bool],
            reason: str = ...,
            run: bool = ...,
            raises: Union[Type[BaseException], Tuple[Type[BaseException], ...]] = ...,
            strict: bool = ...,
        ) -> MarkDecorator:
            ...

    class _ParametrizeMarkDecorator(MarkDecorator):
        def __call__(  # type: ignore[override]
            self,
            argnames: Union[str, List[str], Tuple[str, ...]],
            argvalues: Iterable[Union[ParameterSet, Sequence[object], object]],
            *,
            indirect: Union[bool, Sequence[str]] = ...,
            ids: Optional[
                Union[
                    Iterable[Union[None, str, float, int, bool]],
                    Callable[[Any], Optional[object]],
                ]
            ] = ...,
            scope: Optional[_ScopeName] = ...,
        ) -> MarkDecorator:
            ...

    class _UsefixturesMarkDecorator(MarkDecorator):
        def __call__(self, *fixtures: str) -> MarkDecorator:  # type: ignore[override]
            ...

    class _FilterwarningsMarkDecorator(MarkDecorator):
        def __call__(self, *filters: str) -> MarkDecorator:  # type: ignore[override]
            ...


@final
class MarkGenerator:
    """Factory for :class:`MarkDecorator` objects - exposed as
    a ``pytest.mark`` singleton instance.

    Example::

         import pytest

         @pytest.mark.slowtest
         def test_function():
            pass

    applies a 'slowtest' :class:`Mark` on ``test_function``.
    """

    # See TYPE_CHECKING above.
    if TYPE_CHECKING:
        skip: _SkipMarkDecorator
        skipif: _SkipifMarkDecorator
        xfail: _XfailMarkDecorator
        parametrize: _ParametrizeMarkDecorator
        usefixtures: _UsefixturesMarkDecorator
        filterwarnings: _FilterwarningsMarkDecorator

    def __init__(self, *, _ispytest: bool = False) -> None:
        check_ispytest(_ispytest)
        self._config: Optional[Config] = None
        self._markers: Set[str] = set()

    def __getattr__(self, name: str) -> MarkDecorator:
        """Generate a new :class:`MarkDecorator` with the given name."""
        if name[0] == "_":
            raise AttributeError("Marker name must NOT start with underscore")

        if self._config is not None:
            # We store a set of markers as a performance optimisation - if a mark
            # name is in the set we definitely know it, but a mark may be known and
            # not in the set.  We therefore start by updating the set!
            if name not in self._markers:
                for line in self._config.getini("markers"):
                    # example lines: "skipif(condition): skip the given test if..."
                    # or "hypothesis: tests which use Hypothesis", so to get the
                    # marker name we split on both `:` and `(`.
                    marker = line.split(":")[0].split("(")[0].strip()
                    self._markers.add(marker)

            # If the name is not in the set of known marks after updating,
            # then it really is time to issue a warning or an error.
            if name not in self._markers:
                if self._config.option.strict_markers or self._config.option.strict:
                    fail(
                        f"{name!r} not found in `markers` configuration option",
                        pytrace=False,
                    )

                # Raise a specific error for common misspellings of "parametrize".
                if name in ["parameterize", "parametrise", "parameterise"]:
                    __tracebackhide__ = True
                    fail(f"Unknown '{name}' mark, did you mean 'parametrize'?")

                warnings.warn(
                    "Unknown pytest.mark.%s - is this a typo?  You can register "
                    "custom marks to avoid this warning - for details, see "
                    "https://docs.pytest.org/en/stable/how-to/mark.html" % name,
                    PytestUnknownMarkWarning,
                    2,
                )

        return MarkDecorator(Mark(name, (), {}, _ispytest=True), _ispytest=True)


MARK_GEN = MarkGenerator(_ispytest=True)


@final
class NodeKeywords(MutableMapping[str, Any]):
    __slots__ = ("node", "parent", "_markers")

    def __init__(self, node: "Node") -> None:
        self.node = node
        self.parent = node.parent
        self._markers = {node.name: True}

    def __getitem__(self, key: str) -> Any:
        try:
            return self._markers[key]
        except KeyError:
            if self.parent is None:
                raise
            return self.parent.keywords[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self._markers[key] = value

    # Note: we could've avoided explicitly implementing some of the methods
    # below and use the collections.abc fallback, but that would be slow.

    def __contains__(self, key: object) -> bool:
        return (
            key in self._markers
            or self.parent is not None
            and key in self.parent.keywords
        )

    def update(  # type: ignore[override]
        self,
        other: Union[Mapping[str, Any], Iterable[Tuple[str, Any]]] = (),
        **kwds: Any,
    ) -> None:
        self._markers.update(other)
        self._markers.update(kwds)

    def __delitem__(self, key: str) -> None:
        raise ValueError("cannot delete key in keywords dict")

    def __iter__(self) -> Iterator[str]:
        # Doesn't need to be fast.
        yield from self._markers
        if self.parent is not None:
            for keyword in self.parent.keywords:
                # self._marks and self.parent.keywords can have duplicates.
                if keyword not in self._markers:
                    yield keyword

    def __len__(self) -> int:
        # Doesn't need to be fast.
        return sum(1 for keyword in self)

    def __repr__(self) -> str:
        return f"<NodeKeywords for node {self.node}>"

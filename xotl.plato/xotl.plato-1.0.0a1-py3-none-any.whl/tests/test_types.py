import contextlib
import typing as t

from hypothesis import given, settings
from hypothesis import strategies as st
from xotl.plato.testing import (
    ExtendedBaseTestCase,
    TypedValue,
    date_types,
    datetime_types,
    duration_types,
    float_types,
    floats,
    hashable_types,
    integer_types,
    nonhashable_types,
    object_types,
    optional_types,
    string_types,
    strings,
    supertypes,
    types,
    with_min_or_max,
)
from xotl.plato.types import (
    BaseNumberType,
    DateTimeType,
    DateType,
    DurationType,
    FloatType,
    IntegerType,
    MinMaxType,
    ObjectType,
    OptionalType,
    StringType,
    Type,
)
from xotl.tools.objects import temp_attributes


class BaseCase(ExtendedBaseTestCase):
    def assertTypeMember(
        self,
        value,
        type_object: Type,
        *,
        msg: str = None,
    ):
        try:
            type_object.dump(value, validate=True)
        except (TypeError, ValueError):
            raise self.failureException(
                msg
                or f"Value {value!r} is not a member of type {type_object.simplified_repr!r}"
            )

    def assertNotTypeMember(
        self,
        value,
        type_object: Type,
        *,
        msg: str = None,
    ):
        try:
            type_object.dump(value, validate=True)
        except (TypeError, ValueError):
            pass
        else:
            raise self.failureException(
                msg
                or f"Unexpected member {value!r} of type {type_object.simplified_repr!r}"
            )


class TestTypes(BaseCase):
    @given(types)
    def test_type_reprs(self, type_object):
        # full_repr is reversible
        self.assertEqual(
            type_object,
            Type.from_full_repr(type_object.full_repr),
        )

        # simplified_repr is not empty and starts with constructor's name
        self.assertTrue(
            type_object.simplified_repr.startswith(type_object.constructor_name)
        )

        # all types have a depth
        self.assertGreaterEqual(type_object.depth, 0)

        # all types are pickable
        self.assertPickable(type_object)

        # types are reflexible
        self.assertEqual(type_object, type_object)

    @given(TypedValue.strategy(hashable_types))
    def test_parsing_dumping_hashable_values(self, typed_value: TypedValue):
        type_object, value = typed_value
        assert type_object.parse(type_object.dump(value)) == value

    @given(TypedValue.strategy(nonhashable_types))
    def test_parsing_dumping_nonhashable_values(self, typed_value: TypedValue):
        type_object, value = typed_value
        assert type_object.parse(type_object.dump(value)) == value

    @settings(deadline=None)
    @given(st.data(), integer_types.filter(with_min_or_max))
    def test_integer_type_ensure_min_and_max(self, data, t: IntegerType):
        self._test_minmax(data, t, st.integers)

    @settings(deadline=None)
    @given(st.data(), float_types.filter(with_min_or_max))
    def test_float_types_ensure_min_and_max(self, data, t: FloatType):
        self._test_minmax(data, t, floats)

    @settings(deadline=None)
    @given(st.data(), date_types.filter(with_min_or_max))
    def test_date_types_ensure_min_and_max(self, data, t: DateType):
        def dates(**kwargs):
            min_value = max(
                kwargs.pop(
                    "min_value",
                    DateType.MIN_POSSIBLE_VALUE,
                ),
                DateType.MIN_POSSIBLE_VALUE,
            )
            return st.dates(min_value=min_value, **kwargs)

        self._test_minmax(data, t, dates)

    @settings(deadline=None)
    @given(st.data(), datetime_types.filter(with_min_or_max))
    def test_datetime_types_ensure_min_and_max(self, data, t: DateTimeType):
        def datetimes(**kwargs):
            min_value = max(
                kwargs.pop("min_value", DateTimeType.MIN_POSSIBLE_VALUE),
                DateTimeType.MIN_POSSIBLE_VALUE,
            )
            return st.datetimes(min_value=min_value, **kwargs)

        self._test_minmax(data, t, datetimes)

    @settings(deadline=None)
    @given(st.data(), duration_types.filter(with_min_or_max))
    def test_duration_types_ensure_min_and_max(self, data, t: DurationType):
        def durations(**kwargs):
            min_value = max(
                kwargs.pop(
                    "min_value",
                    DurationType.MIN_POSSIBLE_VALUE,
                ),
                DurationType.MIN_POSSIBLE_VALUE,
            )
            return st.timedeltas(min_value=min_value, **kwargs)

        self._test_minmax(data, t, durations)

    def _test_minmax(
        self,
        data,
        t: t.Union[MinMaxType, BaseNumberType],
        minmax_strategy_factory,
    ):
        if (min_value := t.min_value) is not None:
            invalid_values = minmax_strategy_factory(max_value=min_value)
            if t.min_included:
                invalid_values = invalid_values.filter(lambda i: i != min_value)
        elif (max_value := t.max_value) is not None:
            invalid_values = minmax_strategy_factory(min_value=max_value)
            if t.max_included:
                invalid_values = invalid_values.filter(lambda i: i != max_value)
        value = data.draw(invalid_values)
        self.assertNotTypeMember(value, t)

    @settings(deadline=None)
    @given(st.data(), string_types.filter(lambda t: t.selection))
    def test_string_types_ensure_selection(self, data, t: StringType):
        possible_values = {v for v, _ in t.selection}  # type: ignore
        value = data.draw(strings().filter(lambda s: s not in possible_values))
        self.assertNotTypeMember(value, t)

    @settings(deadline=None)
    @given(st.data(), integer_types.filter(lambda t: t.selection))
    def test_integer_types_ensure_selection(self, data, t: StringType):
        possible_values = {v for v, _ in t.selection}  # type: ignore
        value = data.draw(
            st.integers().filter(lambda s: s not in possible_values)
        )
        self.assertNotTypeMember(value, t)

    @given(optional_types())
    def test_optional_type_flattens(self, optional_type: OptionalType):
        self.assertEqual(OptionalType(optional_type), optional_type)


class TestSubtyping(BaseCase):
    assertSubtype = BaseCase.assertLessEqual

    def assertNotSubtype(self, t, t1, msg=None):
        if t <= t1:
            raise self.failureException(
                msg or f"Unexpected sub-type {t!r} of {t1!r}"
            )

    @given(types)
    def test_types_are_reflexible(self, type_object):
        self.assertSubtype(type_object, type_object)
        self.assertSubtype(
            type_object,
            Type.from_full_repr(type_object.full_repr),
        )

    def assertSubtypeValueRelation(self, data, t: Type, value: t.Any):
        supertype = data.draw(supertypes(t))
        self.assertSubtype(t, supertype)
        self.assertTypeMember(value, supertype)

    @given(st.data(), TypedValue.strategy())
    def test_subtype_values(self, data, typed_value: TypedValue):
        self.assertSubtypeValueRelation(data, typed_value.t, typed_value.value)

    @settings(deadline=None)
    @given(st.data(), object_types, types)
    def test_object_types_require_match(
        self,
        data,
        object_type: ObjectType,
        type_object: Type,
    ):
        shape = dict(object_type.shape)
        # Our strategy only generates keys from 'attr0' to 'attr9', so can
        # assume 'extra' is already in the shape.
        shape["extra"] = OptionalType(type_object)
        self.assertNotSubtype(object_type, t2 := ObjectType(shape))
        try:
            value = data.draw(object_type.get_strategy())
        except TypeError as cause:
            raise TypeError(
                f"While drawing values from {object_type!r}"
            ) from cause
        self.assertNotTypeMember(value, t2)

    def test_types_docstests(self):
        self.runModuleDoctest("xotl.plato.types")


class TestSchemata(ExtendedBaseTestCase):
    def test_schema_docstests(self):
        self.runModuleDoctest("xotl.plato.schema")


@contextlib.contextmanager
def _patch_full_repr_remove_ns(t: Type):
    "Patches the `t` to give a full_repr without a ':ns:' key."
    _super_full_repr = type(t).full_repr.fget  # type: ignore

    def _nsless_full_repr(self):
        res = _super_full_repr(self)
        res.pop(":ns:")
        return res

    with temp_attributes(type(t), {"full_repr": property(_nsless_full_repr)}):
        assert ":ns:" not in t.full_repr
        yield

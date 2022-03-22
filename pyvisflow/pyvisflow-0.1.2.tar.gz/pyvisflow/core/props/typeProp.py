from __future__ import annotations

from abc import abstractmethod
from typing import Callable, Generic, List, Optional, Set, Tuple, Dict, TYPE_CHECKING, Generator, TypeVar, Union
from pyvisflow.core.props.nameProp import NamePropInfo
from pyvisflow.core.props.valueProp import ValuePropInfo

from pyvisflow.utils.helper import value2code

from .absProp import AbsPropInfo
from .combineProp import CombinePropInfo
from .methodProp import MethodPropInfo
from .indexProp import IndexPropInfo
from .fnsMethodProp import FnsMethodPropInfo

if TYPE_CHECKING:
    from pyvisflow.core.props.propValuator import Valuator


class TypePropInfo(AbsPropInfo):
    def __init__(self, parent: AbsPropInfo) -> None:
        super().__init__(parent.valuator, parent)


class StrTypePropInfo(TypePropInfo):
    def __init__(self, parent: AbsPropInfo) -> None:
        super().__init__(parent)

    def __eq__(self, __o: Union[str, StrTypePropInfo]):
        v = None
        if isinstance(__o, str):
            v = ValuePropInfo(None, __o)
        else:
            v = __o
        cb = CombinePropInfo('==', self, v)
        return BoolTypePropInfo(cb)

    def __ne__(self, __o: StrTypePropInfo):
        cb = CombinePropInfo('!=', self, __o)
        return BoolTypePropInfo(cb)

    def __add__(self, other: Union[str, StrTypePropInfo]):
        val = None
        if isinstance(other, str):
            val = ValuePropInfo(None, other)
        else:
            assert isinstance(
                other, TypePropInfo
            ), f'other type is [{type(other)}],it must be str, StrTypePropInfo'
            val = ValuePropInfo.try2PropInfo(other)

        cb = CombinePropInfo('+', self, val)
        return StrTypePropInfo(cb)

    def __radd__(self, other: Union[str, StrTypePropInfo]):
        return self + other

    # def __int__(self) -> int:
    #     return self.toNumber()

    # def __float__(self) -> :
    #     return self.toNumber()

    def slice(self, start: int, end: Optional[int] = None):
        m = MethodPropInfo(self.valuator, self, 'slice', [start, end])

        res = StrTypePropInfo(m)
        return res

    def toNumber(self):
        m = FnsMethodPropInfo('toNumber', [self])
        return NumberTypePropInfo(m)

    def length(self):
        m = NamePropInfo(self.valuator, self, 'length')
        res = NumberTypePropInfo(m)
        return res

    def _ex_gen_expr(self):
        return ''


class NumberTypePropInfo(TypePropInfo):
    def __init__(self, parent: AbsPropInfo) -> None:
        super().__init__(parent)

    def __eq__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('==', other)

    def __ne__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('!=', other)

    def __lt__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('<', other)

    def __le__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('<=', other)

    def __gt__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('>', other)

    def __ge__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4comp('>=', other)

    def __combine(self, logic: str,
                  other: Union[float, int, NumberTypePropInfo]):
        val = None
        if isinstance(other, (float, int)):
            val = ValuePropInfo(None, other)
        else:
            assert isinstance(
                other, TypePropInfo
            ), f'other type is [{type(other)}],it must be float,int'
            val = ValuePropInfo.try2PropInfo(other)

        return CombinePropInfo(logic, self, val)

    def __combine4comp(self, logic: str,
                       other: Union[float, int, NumberTypePropInfo]):
        cb = self.__combine(logic, other)
        return BoolTypePropInfo(cb)

    def __combine4cal(self, logic: str,
                      other: Union[float, int, NumberTypePropInfo]):
        cb = self.__combine(logic, other)
        return NumberTypePropInfo(cb)

    def __add__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4cal('+', other)

    def __radd__(self, other: Union[float, int, NumberTypePropInfo]):
        return self + other

    def __sub__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4cal('-', other)

    def __rsub__(self, other: Union[float, int, NumberTypePropInfo]):
        return self - other

    def __mul__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4cal('*', other)

    def __rmul__(self, other: Union[float, int, NumberTypePropInfo]):
        return self * other

    def __truediv__(self, other: Union[float, int, NumberTypePropInfo]):
        return self.__combine4cal('/', other)

    def __rtruediv__(self, other: Union[float, int, NumberTypePropInfo]):
        return self / other

    def __floordiv__(self, other: Union[float, int, NumberTypePropInfo]):
        oper1 = self.__combine4cal('/', other)
        m = FnsMethodPropInfo('floor', [oper1], package_var='Math')
        return m

    def __rfloordiv__(self, other: Union[float, int, NumberTypePropInfo]):
        return self // other

    def _ex_gen_expr(self):
        return ''


class BoolTypePropInfo(TypePropInfo):
    def __init__(self, parent: AbsPropInfo) -> None:
        super().__init__(parent)

    def __and__(self, other: BoolTypePropInfo):
        cb = CombinePropInfo('&&', self, other)
        return BoolTypePropInfo(cb)

    def __or__(self, other: BoolTypePropInfo):
        cb = CombinePropInfo('||', self, other)
        return BoolTypePropInfo(cb)

    def ex_gen_expr(self):
        return ''


T = TypeVar('T', str, int)
TItem = TypeVar('TItem', StrTypePropInfo, NumberTypePropInfo)


class SubscriptableTypePropInfo(TypePropInfo, Generic[T, TItem]):
    def __init__(self, parent: AbsPropInfo) -> None:
        super().__init__(parent)

    def __getitem__(self, item: Union[T, TItem]) -> TItem:
        idx = IndexPropInfo(self.valuator, self, item)

        if hasattr(self, '__orig_class__'):
            if self.__orig_class__.__args__[1] == StrTypePropInfo:
                return StrTypePropInfo(idx)

            if self.__orig_class__.__args__[1] == NumberTypePropInfo:
                return NumberTypePropInfo(idx)

        return SubscriptableTypePropInfo(idx)

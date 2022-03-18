from enum import Enum
from functools import lru_cache
from typing import cast

from ..extensions import Enums


class FeatureBaseMatchType(Enums.KnownString):
    NUCLEOTIDE = "nucleotide"
    PROTEIN = "protein"

    def __str__(self) -> str:
        return str(self.value)

    @staticmethod
    @lru_cache(maxsize=None)
    def of_unknown(val: str) -> "FeatureBaseMatchType":
        if not isinstance(val, str):
            raise ValueError(f"Value of FeatureBaseMatchType must be a string (encountered: {val})")
        newcls = Enum("FeatureBaseMatchType", {"_UNKNOWN": val}, type=Enums.UnknownString)  # type: ignore
        return cast(FeatureBaseMatchType, getattr(newcls, "_UNKNOWN"))

from datetime import timedelta
from typing import Iterable, Optional, Protocol, Union

import pandas as pd
from atoti_core import BaseCondition, BaseLevel, BaseMeasure


class _ExecuteGaq(Protocol):  # type: ignore
    def __call__(
        self,
        *,
        cube_name: str,
        measures: Iterable[BaseMeasure],
        levels: Iterable[BaseLevel],
        condition: Optional[BaseCondition] = None,
        include_totals: bool,
        scenario: str,
        timeout: Union[int, timedelta],
    ) -> pd.DataFrame:
        ...

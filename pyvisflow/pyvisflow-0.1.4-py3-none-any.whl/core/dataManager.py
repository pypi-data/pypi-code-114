from typing import Dict, List, Generator
import pandas as pd
from pydantic import BaseModel

from pyvisflow.utils.helper import df2array_dict
from pyvisflow.models.TStaticData import TDataframe, TInfo, TColumnsType


def _2infos(df: pd.DataFrame) -> TInfo:
    cols = df.columns.tolist()
    rows = len(df)
    return TInfo(columns=cols, rows=rows)


def _2columnsType(df: pd.DataFrame) -> List[TColumnsType]:
    return [
        TColumnsType(name=name, type=str(t))
        for name, t in zip(df.columns, df.dtypes)
    ]


class TDataFrameInfo(BaseModel):
    id: str
    type: str = 'dataframe'


class DataFrameManager():
    def __init__(self) -> None:
        self.data_dict: Dict[str, pd.DataFrame] = {}

    def mark_data(self, data: pd.DataFrame):
        data_id = str(id(data))
        if not data_id in self.data_dict:
            self.data_dict[data_id] = data

        return TDataFrameInfo(id=data_id)

    def reset(self):
        self.data_dict.clear()

    def to_model(self) -> List[TDataframe]:

        return [
            TDataframe(id=id,
                       infos=_2infos(df),
                       columnsType=_2columnsType(df),
                       data=df2array_dict(df))
            for id, df in self.data_dict.items()
        ]

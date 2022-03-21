from typing import Dict, List, Optional
from pydantic import BaseModel

from pyvisflow.models.TWatchInfo import TWatchInfo
from .TComponent import TComponent
from .TStaticData import TStaticData


class TReactData(BaseModel):
    id: str
    data: Dict


class TConfig(BaseModel):
    staticData: TStaticData
    cps: List[TComponent]
    reactDatas: Optional[List[TReactData]] = []
    watchInfo: TWatchInfo

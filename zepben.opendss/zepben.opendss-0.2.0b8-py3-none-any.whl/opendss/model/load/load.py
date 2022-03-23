#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

import abc
from datetime import date
from typing import List

__all__ = ["Load", "LoadShape", "LoadPoint", "zero_load_point", "LoadShapeInfo", "LoadShapeInfoProvider"]

from zepben.opendss import LoadConnection


class Load(metaclass=abc.ABCMeta):
    def __init__(
            self,
            load_connection_uid: str,
            kw: float,
            pf: float
    ):
        self.load_connection_uid = load_connection_uid
        self.kw = kw
        self.pf = pf


class LoadShape(Load):

    def __init__(
            self,
            load_connection_uid: str,
            kw: float,
            pf: float,
            shape: List[float],
            interval: float
    ):
        super().__init__(load_connection_uid, kw, pf)
        self.shape = shape
        self.interval = interval


class LoadPoint(Load):

    def __init__(
            self,
            load_connection_uid: str,
            kw: float,
            pf: float
    ):
        super().__init__(load_connection_uid, kw, pf)


def zero_load_point(load_conn: LoadConnection):
    return LoadPoint(load_connection_uid=load_conn.uid, kw=0.0, pf=1.0)


class LoadShapeInfo:

    def __init__(self, kw: float, pf: float, shape: List[float], interval: float):
        self.kw = kw
        self.pf = pf
        self.shape = shape
        self.interval = interval


class LoadShapeInfoProvider(metaclass=abc.ABCMeta):

    async def get_load_shape_info(self, conducting_equipment_mrid: str, from_date: date, to_date: date) -> LoadShapeInfo:
        raise NotImplementedError

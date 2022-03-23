#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
from datetime import date
from typing import Dict, Callable

from zepben.opendss import NetworkModel
from zepben.opendss.model.load.load import Load, LoadPoint, LoadShapeInfoProvider, LoadShape

__all__ = ["LoadModel", "single_point_load_model", "load_model_from_load_shape_info_provider", "update_loads_in_model"]


class LoadModel:

    def __init__(
        self,
        network: NetworkModel,
        loads: Dict[str, Load] = None
    ):
        self.network = network
        self.loads = {} if loads is None else loads

    def add_load(self, load: Load):
        if load.load_connection_uid not in self.network.load_connections:
            raise ReferenceError(f"No load connection found with uid {load.load_connection_uid}.")

        self.loads[load.load_connection_uid] = load

    def remove_load(self, uid: str):
        del self.loads[uid]

    def copy(self):
        raise NotImplementedError("Copy method is not implemented")


def single_point_load_model(network_model: NetworkModel, kw: float, pf: float) -> LoadModel:
    load_model = LoadModel(network_model)
    for load_conn in network_model.load_connections.values():
        load_model.add_load(LoadPoint(load_connection_uid=load_conn.uid, kw=kw, pf=pf))
    return load_model


async def load_model_from_load_shape_info_provider(load_shape_info_provider: LoadShapeInfoProvider, from_date: date, to_date: date,
                                                   network_model: NetworkModel) -> LoadModel:
    load_model = LoadModel(network_model)
    for load_conn in network_model.load_connections.values():
        await _add_to_load_model(load_model, load_shape_info_provider, load_conn.uid, from_date, to_date)
    return load_model


async def _add_to_load_model(load_model: LoadModel, load_shape_info_provider: LoadShapeInfoProvider, load_uid: str, from_date: date, to_date: date):
    load_shape_info = await load_shape_info_provider.get_load_shape_info(load_uid, from_date, to_date)
    load_model.add_load(LoadShape(load_uid, load_shape_info.kw, load_shape_info.pf, load_shape_info.shape, load_shape_info.interval))


def update_loads_in_model(load_model: LoadModel, load_updater: Callable[[Load], None], load_filter: Callable[[Load], bool] = lambda _: True):
    for load in load_model.loads.values():
        if load_filter(load):
            load_updater(load)

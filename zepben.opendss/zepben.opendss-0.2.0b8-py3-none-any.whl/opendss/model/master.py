#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

from zepben.opendss import NetworkModel
from zepben.opendss.model.load.load_model import LoadModel
from zepben.opendss.model.metering.metering_model import MeteringModel

__all__ = ["Master"]


class Master:

    def __init__(
            self,
            network_model: NetworkModel,
            load_model: LoadModel,
            metering_model: MeteringModel
    ):
        self.network_model = network_model
        self.load_model = load_model
        self.metering_model = metering_model

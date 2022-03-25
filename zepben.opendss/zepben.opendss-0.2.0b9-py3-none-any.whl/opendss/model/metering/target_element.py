#  Copyright 2022 Zeppelin Bend Pty Ltd
#
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.

__all__ = ["TargetElement"]

from typing import Literal


class TargetElement:

    def __init__(
            self,
            uid: str,
            element_type: Literal["Transformer", "Line", "Load"]
    ):
        self.uid = uid
        self.element_type = element_type

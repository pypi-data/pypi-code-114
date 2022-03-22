# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from __future__ import annotations

from typing import List

from availsim4core.src.context.context import Context
from availsim4core.src.context.system.children_logic.oo import Oo
from availsim4core.src.context.system.component_tree.component import Component
from availsim4core.src.context.system.component_tree.status import Status


class ToleratedFault(Oo):

    def __init__(self, fault_tolerance: int):
        super().__init__(0)
        self.fault_tolerance = fault_tolerance

    def __repr__(self):
        return f"{self.fault_tolerance}FT"

    def evaluate(self, list_of_children: List[Component], context: Context) -> Status:
        self.minimum_number_of_required_component = len(list_of_children) - self.fault_tolerance
        return super().evaluate(list_of_children, context)

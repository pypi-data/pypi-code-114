# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from availsim4core.src.context.system.component_tree.basic import Component

from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.component_tree.status import Status
from availsim4core.src.results.result_record_entry_component import ResultRecordEntryComponent
from availsim4core.src.timeline.record import Record
from availsim4core.src.context.system.rca_trigger import RootCauseAnalysisTrigger


class RecordComponent(Record):
    """
    Class of record dedicated to components
    A record is an object used to keep trace of the state of the system
    """
    __slots__ = 'component', 'status'

    def __init__(self,
                 component: Component,
                 status: Status,
                 timestamp: float,
                 phase: Phase,
                 description: str):
        super().__init__(timestamp, phase, description)
        self.component = component
        self.status = status

    def __eq__(self, other):
        if not isinstance(other, RecordComponent):
            return NotImplemented
        return super().__eq__(other) \
               and self.component == other.component \
               and self.status == other.status

    def __repr__(self):
        return super().__repr__() \
               + f" component: {self.component.name} -> id: {self.component.global_id}" \
                 f" status: {self.status} , phase: {self.phase}"

    def __str__(self):
        return f"RecordComponent at {self.timestamp}: " \
               f"{self.component.name}_{self.component.local_id}_{self.component.global_id} " \
               f"with status {self.status} on phase {self.phase.name}__{self.status}"

    def get_result_record_entry(self):
        return ResultRecordEntryComponent(self.component,
                                          self.status,
                                          self.phase,
                                          self.description)

    def check_if_in_rca_triggers(self, rca_triggers, current_phase_name):
        return RootCauseAnalysisTrigger(self.component.name, str(self.component.status), current_phase_name) in rca_triggers
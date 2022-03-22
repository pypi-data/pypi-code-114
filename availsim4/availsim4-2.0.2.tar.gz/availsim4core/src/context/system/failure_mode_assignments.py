# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from availsim4core.src.context.system.failure_mode import FailureMode


class FailureModeAssignments:
    __slots__ = 'component_name', 'failure_mode'

    def __init__(self,
                 component_name: str,
                 failure_mode: FailureMode):
        self.component_name = component_name
        self.failure_mode = failure_mode

    def __eq__(self, other):
        if not isinstance(other, FailureModeAssignments):
            return NotImplemented
        return self.component_name == other.component_name and \
               self.failure_mode == other.failure_mode

    def __repr__(self):
        return f"component_name: {self.component_name} -> " \
               f"failure_mode.name: {self.failure_mode.name}"

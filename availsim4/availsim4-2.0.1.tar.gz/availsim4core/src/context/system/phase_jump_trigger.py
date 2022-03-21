# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List

from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.component_tree.status import Status


class PhaseJumpTrigger:

    def __init__(self,
                 component_name: str,
                 component_status: Status,
                 from_phase: str,
                 to_phase: str):
        self.component_name = component_name
        self.component_status = component_status
        self.from_phase = from_phase
        self.to_phase = to_phase

    def __str__(self):
        return f"Phase Jump trigger on {self.component_name}, "\
        f"status {self.component_status} from phase {self.from_phase} to phase {self.to_phase}"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.component_name, self.component_status,
                     self.from_phase, self.to_phase))

    def __eq__(self, other):
        if not isinstance(other, PhaseJumpTrigger):
            return NotImplemented
        return self.component_name == other.component_name and \
               self.component_status == other.component_status and \
               self.from_phase == other.from_phase and \
               self.to_phase == other.to_phase


class PhaseJumpTriggerFactory:
    
    @staticmethod
    def build(triggering_component_name: str,
              triggering_component_status_list: List[str],
              triggering_from_phase_list: List[str],
              triggering_to_phase: str,
              phase_list: List[Phase]) -> List[PhaseJumpTrigger]:
        return [PhaseJumpTrigger(
            triggering_component_name,
            Status(status),
            next((phase for phase in phase_list if phase.name == from_phase), None),
            next((phase for phase in phase_list if phase.name == triggering_to_phase), None)
        )
            for status in triggering_component_status_list
            for from_phase in triggering_from_phase_list]

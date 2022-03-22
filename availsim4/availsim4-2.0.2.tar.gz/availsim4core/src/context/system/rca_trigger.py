# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List


class RootCauseAnalysisTrigger:

    def __init__(self, component_name: str, component_status: str, phase: str):
        self.component_name = component_name
        self.component_status = component_status
        self.phase = phase

    def __str__(self):
        return f"RCA trigger on {self.component_name}, status {self.component_status} in phase {self.phase}"

    def __repr__(self):
        return str(self)

    def __hash__(self):
        return hash((self.component_name, self.component_status, self.phase))

    def __eq__(self, other):
        if not isinstance(other, RootCauseAnalysisTrigger):
            return NotImplemented
        return self.component_name == other.component_name and \
               self.component_status == other.component_status and \
               self.phase == other.phase


class RootCauseAnalysisTriggerFactory:
    
    @staticmethod
    def build(triggering_component_name: str,
              triggering_component_statuses: List[str], 
              triggering_phases: List[str]) -> List[RootCauseAnalysisTrigger]:
        return [RootCauseAnalysisTrigger(triggering_component_name, status, phase) 
                for status in triggering_component_statuses 
                for phase in triggering_phases]

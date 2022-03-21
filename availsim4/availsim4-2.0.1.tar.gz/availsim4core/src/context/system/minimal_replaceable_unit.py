# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from typing import List

from availsim4core.src.context.system.component_tree.status import Status
from availsim4core.src.context.system.probability_law.probability_law import ProbabilityLaw
from availsim4core.src.context.system.probability_law.probability_law_factory import ProbabilityLawFactory


class MinimalReplaceableUnit:
    """
    Domain object class to represent a MinimalReplaceableUnit.
    This class represent both the TRIGGER mru and TARGET mru.
    """

    def __init__(self,
                 name: str,
                 repair_law: ProbabilityLaw,
                 repair_schedule: str,
                 triggering_status: Status,
                 scope_common_ancestor: List[str]):
        self.name = name
        self.repair_law: ProbabilityLaw = repair_law
        self.repair_schedule: str = repair_schedule
        self.status = triggering_status
        self.scope_common_ancestor = scope_common_ancestor

    def __hash__(self):
        return hash((type(self), self.name,
                     self.repair_schedule,
                     self.status,
                     *self.scope_common_ancestor))

    def __str__(self):
        return f"{self.name} - {self.repair_law} - {self.repair_schedule} - {self.status} - {self.scope_common_ancestor}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if not isinstance(other, MinimalReplaceableUnit):
            return NotImplemented
        return self.name == other.name and \
               self.repair_law == other.repair_law and \
               self.repair_schedule == other.repair_schedule and \
               self.status == other.status and \
               self.scope_common_ancestor == other.scope_common_ancestor


class MinimalReplaceableUnitFactory:
    """
    Utility class to build a 'MinimalReplaceableUnit'.
    """

    @staticmethod
    def build(mru_name,
              mru_repair_law_name,
              mru_repair_parameters,
              minimal_replaceable_repair_schedule,
              triggering_status_list_of_str,
              scope_common_ancestor_name_str) -> List[MinimalReplaceableUnit]:
        """
        This methods returns a List of {MinimalReplaceableUnit}.
        For each `triggering_status` it creates a different mru.
        """
        return [MinimalReplaceableUnit(mru_name,
                                       ProbabilityLawFactory.build(mru_repair_law_name,
                                                                   mru_repair_parameters),
                                       minimal_replaceable_repair_schedule,
                                       Status(triggering_status),
                                       scope_common_ancestor_name_str)
                for triggering_status in triggering_status_list_of_str]

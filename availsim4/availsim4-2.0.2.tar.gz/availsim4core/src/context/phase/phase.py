# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from __future__ import annotations
from availsim4core.src.context.system.probability_law.probability_law import ProbabilityLaw


class Phase:
    """
    Class dealing with phases, defining each of them
    """
    __slots__ = 'name', 'law', 'next', 'is_first_phase', 'next_phase_if_failure'

    def __init__(self,
                 phase_name: str,
                 phase_law: ProbabilityLaw,
                 phase_first: bool):
        self.name = phase_name
        self.law = phase_law
        self.next = None
        self.is_first_phase = phase_first
        self.next_phase_if_failure = None

    def set_next_phase(self, next_phase):
        self.next = next_phase

    def set_next_phase_if_failure(self, next_phase_if_failure):
        self.next_phase_if_failure = next_phase_if_failure

    def __hash__(self):
        return hash((type(self), self.name))

    def __eq__(self, other):
        if not isinstance(other, Phase):
            return NotImplemented
        return self.name == other.name

    def __str__(self):
        if self.next is None or self.next_phase_if_failure is None:
            return (f"Phase name:{self.name} ~ "
                    f"law:{self.law} ~ "
                    f"first:{self.is_first_phase} ~ ")
        else:
            return (f"Phase name:{self.name} ~ "
                    f"law:{self.law} ~ "
                    f"next:{self.next.name} ~ "
                    f"first:{self.is_first_phase} ~ "
                    f"next if failure:{self.next_phase_if_failure.name}")
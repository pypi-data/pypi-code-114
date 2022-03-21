# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging
from typing import Set

from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.failure import Failure, FailureType
from availsim4core.src.context.system.inspection import Inspection
from availsim4core.src.context.system.probability_law.probability_law import ProbabilityLaw
import numpy


class FailureModeError(Exception):
    pass


class FailureMode:
    """
    Defines the failure attributes based on a probability law.
    Also defines the repair attributes related to this failure based on a probability law.
    # TODO : Refactoring of this class introducing dedicated classes for the failure / repair / inspection :
    cf https://gitlab.cern.ch/availsim4/availsim4core/-/issues/30
    """
    __slots__ = 'name', 'failure_law', 'repair_law', 'failure', 'held_before_repair_phase_set', 'inspection', \
                'phase_set', 'failure_mode_next_phase_if_failure', 'phase_change_trigger', 'held_after_repair_phase_set', \
                'uniform_samples_for_quasi_monte_carlo', 'sample_generation_time'

    def __init__(self,
                 name: str,
                 failure_law: ProbabilityLaw,
                 repair_law: ProbabilityLaw,
                 failure: Failure,
                 held_before_repair_phase_set: Set[Phase],
                 inspection: Inspection,
                 phase_set: Set[Phase],
                 failure_mode_next_phase_if_failure: Phase,
                 phase_change_trigger: str,
                 held_after_repair_phase_set: Set[Phase]):

        if failure.type_of_failure == FailureType.BLIND and phase_change_trigger == 'AFTER_REPAIR':
            message = f"Wrong combination of type_of_failure ({failure}) " \
                      f"and phase_change_timing ({phase_change_trigger}) " \
                      f"for the failure mode named {name}"
            logging.exception(message)
            raise FailureModeError(message)

        self.name = name
        self.failure_law = failure_law
        self.repair_law = repair_law
        self.failure = failure
        self.held_before_repair_phase_set = held_before_repair_phase_set
        self.inspection = inspection
        self.phase_set = phase_set
        self.failure_mode_next_phase_if_failure = failure_mode_next_phase_if_failure
        self.phase_change_trigger = phase_change_trigger
        self.held_after_repair_phase_set = held_after_repair_phase_set
        self.uniform_samples_for_quasi_monte_carlo = []
        self.sample_generation_time = 0.0

    def __hash__(self):
        return hash((type(self), self.name))

    def __str__(self):
        return (f"{self.name} :: "
                f"{self.failure_law} / "
                f"{self.repair_law} / "
                f"{self.failure} / "
                f"{[phase.name for phase in self.held_before_repair_phase_set]} / "
                f"{self.inspection} / "
                f"{[phase.name for phase in self.phase_set]} / "
                f"{self.phase_change_trigger} /"
                f"{[phase.name for phase in self.held_after_repair_phase_set]}")

    def __eq__(self, other):
        if not isinstance(other, FailureMode):
            return NotImplemented
        return self.name == other.name

    def set_uniform_samples_for_quasi_monte_carlo(self, uniform_samples_for_quasi_monte_carlo: numpy.ndarray):
        self.uniform_samples_for_quasi_monte_carlo = list(uniform_samples_for_quasi_monte_carlo)
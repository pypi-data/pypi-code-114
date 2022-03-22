# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from availsim4core.src.context.system.component_tree.basic import Basic

from availsim4core.src.context.context import Context
from availsim4core.src.context.system.failure import FailureType
from availsim4core.src.context.system.failure_mode import FailureMode
from availsim4core.src.discrete_event_simulation.event.b_event.failure_event.blind_failure_event import \
    BlindFailureEvent
from availsim4core.src.discrete_event_simulation.event.b_event.failure_event.detectable_failure_event import \
    DetectableFailureEvent
import logging


class FailureEventFactoryError(Exception):
    pass


class FailureEventFactory:
    """
    Utility class to build a 'FailureEvent'.
    """

    @staticmethod
    def build(absolute_time_to_failure,
              context: Context,
              basic: Basic,
              failure_mode: FailureMode):
        """
        Given an absolute_time and a type of failure, it returns the corresponding FailureEvent at the correct timing.
        """

        if failure_mode.failure.type_of_failure == FailureType.DETECTABLE:
            return DetectableFailureEvent(absolute_time_to_failure,
                                          context,
                                          basic,
                                          failure_mode)

        elif failure_mode.failure.type_of_failure == FailureType.BLIND:
            return BlindFailureEvent(absolute_time_to_failure,
                                     context,
                                     basic,
                                     failure_mode)

        else:
            message_exception = f"Wrong type of failure {failure_mode.failure.type_of_failure} in the sheet failureModes"
            logging.exception(message_exception)
            raise FailureEventFactoryError(message_exception)

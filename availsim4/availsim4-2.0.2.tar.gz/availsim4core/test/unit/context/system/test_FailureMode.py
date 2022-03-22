# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import unittest

from availsim4core.src.context.phase.phase import Phase
from availsim4core.src.context.system.failure import FailureType, Failure
from availsim4core.src.context.system.failure_mode import FailureMode, FailureModeError
from availsim4core.src.context.system.inspection import Inspection
from availsim4core.src.context.system.probability_law.probability_law import ProbabilityLaw


class test_FailureFactory(unittest.TestCase):

    def test_failure_mode_exception(self):
        """
        This test check that AvailSim4 will detect the combination of type_of_failure = "BLIND" and phase_change_timing = "AFTER_REPAIR"
        """
        with self.assertRaises(FailureModeError) as context:

            NO_PHASE = Phase("NONE", ProbabilityLaw("", 0, False), False)
            NO_PHASE.set_next_phase(NO_PHASE)
            NO_PHASE.set_next_phase_if_failure(NO_PHASE)

            expected_inspection = Inspection("inspection_test", 1, 2)

            FailureMode("TEST_FAILURE",
                        ProbabilityLaw("", 0, False),
                        ProbabilityLaw("", 0, False),
                        Failure(FailureType.BLIND),
                        "[]",
                        expected_inspection,
                        [],
                        NO_PHASE,
                        'AFTER_REPAIR',
                        []
                    )

        self.assertTrue("Wrong combination of type_of_failure" in str(context.exception))

# SPDX-License-Identifier: GPL-3.0-only
# (C) Copyright CERN 2021. All rights not expressly granted are reserved. 

import logging

from availsim4core.src.context.system.failure import Failure, FailureType
from availsim4core.src.context.system.system_utils import SystemUtils


class FailureFactoryError(Exception):
    pass


class FailureFactory:

    @staticmethod
    def build(failure_mode_type_of_failure_str):

        if "DETECTABLE" == failure_mode_type_of_failure_str:
            return Failure(FailureType.DETECTABLE)

        elif "BLIND" == SystemUtils.extract_name_of_function_from_string(failure_mode_type_of_failure_str):
            return Failure(FailureType.BLIND)
        else:
            message = f"Wrong type of failure : {failure_mode_type_of_failure_str} not found "
            logging.exception(message)
            raise FailureFactoryError(message)

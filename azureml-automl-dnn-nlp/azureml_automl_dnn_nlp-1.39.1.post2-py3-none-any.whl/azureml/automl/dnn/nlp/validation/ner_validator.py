# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""
This module is for data validation purpose for dnn nlp NER scenario
"""

from .validators import AbstractNERDataValidator
from .utils import raise_validation_error
from typing import Optional

from azureml.automl.dnn.nlp.common.constants import DataLiterals, DatasetValidationConstants, ValidationLiterals

import os


class NLPNERDataValidator(AbstractNERDataValidator):
    """Data validation class for NER scenario only"""

    def validate(self, dir: str, train_file: str, valid_file: Optional[str] = None) -> None:
        """
        Data validation for NER scenario only.

        Validations include:
            1. Exactly one white space is in each line, if the line is not "\n"
            2. There are at least 50 (for now) samples in the training set
            3. There is exactly one empty line in the end of each file
            4. All labels starts with 'I-' or 'B-'
            5. No consecutive empty lines in the file

        :param dir: directory where ner data should be downloaded
        :param train_file: name of downloaded training file
        :param valid_file: name of downloaded validation file. None if no validation
        :return None
        """

        self.error_message1 = "Validation Error: Each line in {} set should either contain exactly one white space"
        self.error_message1 += " to separate token and its label, or it should be an empty line '\\n'"

        self.error_message2 = "Validation Error: At least {} training samples are required"
        self.error_message2 = self.error_message2.format(DatasetValidationConstants.MIN_TRAINING_SAMPLE)

        self.error_message3 = "Validation Error: Excatly one empty line is expected at the end of {} set file"

        self.error_message4 = "Validation Error: All labels in {} set should"
        self.error_message4 += " either start with 'I-' or 'B-', or be exactly 'O'"

        self.error_message5 = "Validation Error: {} set file should not have consecutive empty lines"

        self.error_message6 = "Validation Error: Tokens should not be empty strings"

        self.error_message7 = "Validation Error: File should not start with an empty line"

        self._check_file_format(dir, train_file, ValidationLiterals.TRAINING_SET, True)
        if valid_file is not None:
            self._check_file_format(dir, train_file, ValidationLiterals.VALID_SET, False)

    def _check_file_format(
        self,
        dir: str,
        file: str,
        split: str,
        check_size: Optional[bool] = False
    ) -> None:
        '''
        Main validation function that checks the format of a txt file.

        :param dir: directory where ner data should be downloaded
        :param file: name of downloaded file
        :param split: indicator of whether it's training or validation set
        :param check_size: whether to check how many samples are available in the dataset
        :return None
        '''
        file_path = os.path.join(dir, file)
        with open(file_path, encoding=DataLiterals.ENCODING, errors=DataLiterals.ERRORS) as f:
            line = f.readline()
            if line == "\n":
                raise_validation_error(self.error_message7)
            if line.startswith('-DOCSTART-'):  # optional beginning of a file, ignored with the following line
                line = f.readline()
                line = f.readline()
            cnt = 0
            prev_line = None
            while line:  # not the end of file
                self._check_line_format(line, split)
                if line == '\n':  # empty line
                    if prev_line == '\n':
                        raise_validation_error(self.error_message5.format(split))
                    cnt += 1
                prev_line = line
                line = f.readline()
            if prev_line != '\n':
                cnt += 1

            if prev_line == '\n' or prev_line[-1] != '\n':
                raise_validation_error(self.error_message3.format(split))
            if check_size and cnt < DatasetValidationConstants.MIN_TRAINING_SAMPLE:
                raise_validation_error(self.error_message2)

    def _check_line_format(self, line: str, split: str) -> None:
        '''
        Check if one line follows the correct format. To be specific:
            1. Check if this line is empty line ('\n') or has exactly one white space
            2. If the line is not empty, check if the label starts with 'B-' or 'I-'

        :param line: string for that line
        :param split: indicator of whether it's training or validation set
        :return None
        '''
        if line != '\n' and line.count(' ') > 1:
            raise_validation_error(self.error_message1.format(split))
        if line != '\n':
            token, label = line.split(' ')
            if len(token) == 0:
                raise_validation_error(self.error_message6)
            if not (label.strip() == "O" or label.startswith("I-") or label.startswith("B-")):
                raise_validation_error(self.error_message4.format(split))

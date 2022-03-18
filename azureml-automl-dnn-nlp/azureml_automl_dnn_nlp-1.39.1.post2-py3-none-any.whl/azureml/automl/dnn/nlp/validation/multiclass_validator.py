# ---------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# ---------------------------------------------------------

"""
This module is for data validation purpose for dnn nlp multiclass scenario
"""

import pandas as pd
from typing import Optional

from azureml.automl.dnn.nlp.common.constants import DatasetValidationConstants
from azureml.automl.dnn.nlp.validation.utils import raise_validation_error
from azureml.automl.dnn.nlp.validation.validators import AbstractNLPClassificationDataValidator


class NLPMulticlassDataValidator(AbstractNLPClassificationDataValidator):
    """Data validation class for multiclass scenario only"""

    def check_custom_validation(
        self,
        label_column_name: str,
        train_data: pd.DataFrame,
        valid_data: Optional[pd.DataFrame] = None
    ) -> None:
        """
        Data validation for multiclass scenario only.

        Validation includes:
            1. check if training data contains at least two unique class labels

        :param label_col_name: Column name of label column.
        :param train_data: The training set data to validate.
        :param valid_data: The validation set data to validate
        :return: None
        """
        self._check_min_label_classes(train_data, label_column_name)

    def _check_min_label_classes(self, train_df: pd.DataFrame, label_column_name: str):
        """Check if the training data contains a minimum number of unique class labels

        :param train_df: training dataframe
        :param label_column_name: Name/title of the label column
        :param is_multiclass: Bool flag to help distinguish between multiclass and multilabel
        """
        num_unique_label_classes = len(pd.unique(train_df[label_column_name]))
        error_message = "Validation Error: Training data must contain at least {} unique label classes"
        if num_unique_label_classes < DatasetValidationConstants.MIN_LABEL_CLASSES:
            raise_validation_error(error_message.format(DatasetValidationConstants.MIN_LABEL_CLASSES))

import pandas as pd
import pytest
from azureml.automl.core.shared.exceptions import DataException
from azureml.automl.dnn.nlp.common.constants import DatasetValidationConstants
from azureml.automl.dnn.nlp.validation.multiclass_validator import NLPMulticlassDataValidator

from .conftest import get_multiclass_label_columns_data, get_test_feature_columns_data


class TestDataValidation:

    @pytest.mark.parametrize('two_or_more_unique_label_classes', [True, False])
    def test_multiclass_data_validator_labels(self, two_or_more_unique_label_classes):
        train_features, _ = get_test_feature_columns_data(True, True, True, True)
        train_labels = get_multiclass_label_columns_data(two_or_more_unique_label_classes)

        train_data = pd.concat([train_features, train_labels], axis=1)
        valid_data = train_data.copy()
        should_pass = all([two_or_more_unique_label_classes])
        try:
            validator = NLPMulticlassDataValidator()
            validator.validate("label", train_data, valid_data)
            passed = True
        except DataException:
            passed = False

        error_message = "Training data must contain at least {} unique label classes"
        assert should_pass == passed, error_message.format(DatasetValidationConstants.MIN_LABEL_CLASSES)


import pandas as pd
import pytest

from azureml.automl.core.shared.exceptions import DataException
from azureml.automl.dnn.nlp.validation.multilabel_validator import NLPMultilabelDataValidator
from azureml.automl.dnn.nlp.validation.multiclass_validator import NLPMulticlassDataValidator

from .conftest import get_multilabel_label_columns_data, get_test_feature_columns_data


@pytest.mark.parametrize('same_column', [True, False])
@pytest.mark.parametrize('same_order', [True, False])
@pytest.mark.parametrize('same_type', [True, False])
@pytest.mark.parametrize('no_duplicate_column_name', [True, False])
@pytest.mark.parametrize('validator_class', [NLPMulticlassDataValidator(), NLPMultilabelDataValidator()])
def test_multilabel_data_validator_features(same_column, same_order, same_type,
                                            no_duplicate_column_name, validator_class):
    train_labels, valid_labels = get_multilabel_label_columns_data(True, True, True, True, True, True)
    train_features, valid_features = get_test_feature_columns_data(
        same_column,
        same_order,
        same_type,
        no_duplicate_column_name
    )
    train_data = pd.concat([train_features, train_labels], axis=1)
    valid_data = pd.concat([valid_features, valid_labels], axis=1)
    should_pass_with_valid = all([same_column, same_order, same_type, no_duplicate_column_name])
    should_pass_without_valid = all([no_duplicate_column_name])
    try:
        validator = validator_class
        validator.validate("label", train_data, valid_data)
        passed_with_valid = True
    except DataException:
        passed_with_valid = False
    try:
        validator = validator_class
        validator.validate("label", train_data, None)
        passed_without_valid = True
    except DataException:
        passed_without_valid = False
    error_message = f"{same_column}, {same_order}, {same_type}, {no_duplicate_column_name}"
    assert should_pass_with_valid == passed_with_valid, "with valid set " + error_message
    assert should_pass_without_valid == passed_without_valid, "without valid set " + error_message

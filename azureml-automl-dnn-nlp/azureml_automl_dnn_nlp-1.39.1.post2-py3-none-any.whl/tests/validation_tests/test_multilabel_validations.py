import pandas as pd
import pytest

from azureml.automl.core.shared.exceptions import DataException
from azureml.automl.dnn.nlp.classification.multilabel.utils import change_label_col_format
from azureml.automl.dnn.nlp.validation.multilabel_validator import NLPMultilabelDataValidator

from .conftest import get_multilabel_label_columns_data, get_test_feature_columns_data


@pytest.fixture
def get_labels_in_old_format():
    labels = [
        'a',
        '1',
        'b,c',
        '2',
        ''
    ]
    train_labels = pd.DataFrame({"label": labels})
    valid_labels = pd.DataFrame({"label": labels})
    return train_labels, valid_labels


@pytest.mark.parametrize('can_eval', [True, False])
@pytest.mark.parametrize('all_list', [True, False])
@pytest.mark.parametrize('multi_label', [True, False])
@pytest.mark.parametrize('correct_type', [True, False])
@pytest.mark.parametrize('no_overlap', [True, False])
@pytest.mark.parametrize('not_single_class', [True, False])
def test_multilabel_data_validator_labels(can_eval, all_list, multi_label, correct_type, no_overlap, not_single_class):
    train_features, valid_features = get_test_feature_columns_data(True, True, True, True)
    train_labels, valid_labels = get_multilabel_label_columns_data(
        can_eval,
        all_list,
        multi_label,
        correct_type,
        no_overlap,
        not_single_class
    )
    train_data = pd.concat([train_features, train_labels], axis=1)
    valid_data = pd.concat([valid_features, valid_labels], axis=1)
    should_pass = all([can_eval, all_list, multi_label, correct_type, no_overlap, not_single_class])
    try:
        validator = NLPMultilabelDataValidator()
        validator.validate("label", train_data, valid_data)
        passed_with_valid = True
    except DataException:
        passed_with_valid = False
    try:
        validator = NLPMultilabelDataValidator()
        validator.validate("label", train_data, None)
        passed_without_valid = True
    except DataException:
        passed_without_valid = False
    error_message = f"{can_eval}, {all_list}, {multi_label}, {correct_type}, {no_overlap}, {not_single_class}"
    assert should_pass == passed_with_valid, "with valid set " + error_message
    assert should_pass == passed_without_valid, "without valid set " + error_message


def test_support_for_old_format(get_labels_in_old_format):
    train_features, valid_features = get_test_feature_columns_data(True, True, True, True)
    train_labels, valid_labels = get_labels_in_old_format
    train_data = pd.concat([train_features, train_labels], axis=1)
    valid_data = pd.concat([valid_features, valid_labels], axis=1)
    label_col_name = "label"
    change_label_col_format(train_data, label_col_name)
    change_label_col_format(valid_data, label_col_name)
    assert train_data.loc[4, label_col_name] == "[]"

    validator = NLPMultilabelDataValidator()
    validator.validate("label", train_data, valid_data)

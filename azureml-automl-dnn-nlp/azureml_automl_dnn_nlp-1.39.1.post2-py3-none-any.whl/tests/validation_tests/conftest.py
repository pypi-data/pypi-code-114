import numpy as np
import pandas as pd

from azureml.automl.dnn.nlp.common.constants import DatasetValidationConstants


def get_test_feature_columns_data(same_column, same_order, same_type, no_duplicate_column_name):
    """
    Generate unit test feature data based on the value of parameters for classification tasks.

    :param same_column: whether two datasets share the same set of columns
    :param same_order: whether two datasets' columns share the same order
    :param same_type: whether the same column name correspond to the same data type in two datasets
    :param duplicate_column_name: whether all column names are unique
    :return feature columns for train and validation dataset
    """
    column_names = ["A", "B", "C"]
    column1 = ["A", "B", "C", "D", "E"]
    column2 = [1, 2, 3, 4, 5]
    column3 = ["A", "B", "C", "D", "E"]
    data = [column1, column2, column3]

    train_data = pd.DataFrame(data=np.array(data).T, columns=column_names)
    train_data["B"] = train_data["B"].astype(int)
    valid_data = pd.DataFrame(data=np.array(data).T, columns=column_names)
    if same_type:
        valid_data["B"] = valid_data["B"].astype(int)

    if not same_column:
        valid_data.drop(columns=["A"], inplace=True)
    if not same_order:
        valid_data = valid_data[valid_data.columns[::-1]]
    if not no_duplicate_column_name:
        train_data.columns = ["A", "A", "C"]

    return train_data, valid_data


def get_multilabel_label_columns_data(can_eval, all_list, multi_label, correct_type, no_overlap, not_single_class):
    """
    Generate unit test label data based on the value of parameters for multilabel task

    :param can_eval: whether we can apply eval function onto that column
    :param all_list: after eval, whether all values are list
    :param multi_label: whether at least one sample has not exactly one label
    :param correct_type: whether all labels are integers or strings
    :param no_overlap: whether there is no overlapping between integer labels and strings labels (like 1 and '1')
    :param not_single_class: whether there is more than one class
    :return label columns for train and validation dataset
    """
    labels = [
        "['a']",
        "[1]",
        "['b','c']",
        "[2]",
        "['c']"
    ]
    if not can_eval:
        labels[0] = ["a"]
    if not all_list:
        labels[1] = "1"
    if not multi_label:
        labels[2] = "['b']"
    if not correct_type:
        labels[3] = "[1.0]"
    if not no_overlap:
        labels[4] = "['1']"
    if not not_single_class:
        labels = ["[1]", "['1']", "['1']", "[1]", "[1]"]

    train_labels = pd.DataFrame({"label": labels})
    valid_labels = pd.DataFrame({"label": labels})
    return train_labels, valid_labels


def get_multiclass_label_columns_data(two_or_more_unique_label_classes):
    """
    Generate unit test label data based on the value of parameters for multiclass task

    :param two_or_more_unique_label_classes: if false, then there's only one unique label class
    :return label column for multiclass train dataset
    """
    train_labels = pd.DataFrame({"label": ["XYZ", "ABC", "PQR", "ABC", "XYZ"]})
    if not two_or_more_unique_label_classes:
        train_labels["label"] = "XYZ"
    return train_labels


def get_ner_data(
    extra_white_space,
    not_enough_data,
    no_empty_line,
    extra_empty_line,
    wrong_label,
    consecutive_empty_line,
    empty_line_start,
    empty_token
):
    '''
    Create file content for NER data validation

    :param extra_white_space: whether there would be a line with two while spaces in the middle
    :param not_enough_data: whether the sample size would be less than requirement
    :param no_empty_line: whether there is no empty line at the end of file
    :param extra_empty_line: whether there would be more than one empty lines at the end of file
                             If this parameter is True, no_empty_line will be ignored
    :param wrong_label: whether some labels do not start with 'B-' nor 'I-'
    :param consecutive_empty_line: whether there would be multiple empty lines to separate samples
    :param empty_line_start: whether the file would start with an empty line
    :param empty_token: whether some tokens in the dataset would be empty
    '''
    tokens = ['test_token1', 'test_token2', 'test_token3']
    labels = ['B-label', 'I-label', 'O']
    if empty_token:
        tokens[0] = ''

    sep = '  ' if extra_white_space else ' '
    if wrong_label:
        labels[0] = 'label'

    lines = []
    for token, label in zip(tokens, labels):
        lines.append(sep.join([token, label]) + '\n')

    content = ''.join(lines)  # this is one sample with two tokens
    sep = '\n\n' if consecutive_empty_line else '\n'
    if not not_enough_data:
        content = sep.join([content for _ in range(DatasetValidationConstants.MIN_TRAINING_SAMPLE)])

    if extra_empty_line:
        content += "\n"
    elif no_empty_line:
        content = content[:-1]
    else:
        None

    if empty_line_start:
        content = '\n' + content

    return content

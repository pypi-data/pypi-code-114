import pytest
from unittest.mock import MagicMock, patch, mock_open

from azureml.automl.core.shared.exceptions import DataException
from azureml.automl.dnn.nlp.validation.ner_validator import NLPNERDataValidator

from .conftest import get_ner_data


def open_ner_file(filename, mode=None, encoding=None, errors=None):
    params = []
    for char in filename[9:]:  # starts from 9 to skip 'mock_dir/'
        params.append(char == '1')
    content = get_ner_data(*params)
    file_object = mock_open(read_data=content).return_value
    file_object.__iter__.return_value = content.splitlines(True)
    return file_object


@pytest.mark.parametrize('extra_white_space', [True, False])
@pytest.mark.parametrize('not_enough_data', [True, False])
@pytest.mark.parametrize('no_empty_line', [True, False])
@pytest.mark.parametrize('extra_empty_line', [True, False])
@pytest.mark.parametrize('wrong_label', [True, False])
@pytest.mark.parametrize('consecutive_empty_line', [True, False])
@pytest.mark.parametrize('empty_line_start', [True, False])
@pytest.mark.parametrize('empty_token', [True, False])
def test_ner_validator(
    extra_white_space,
    not_enough_data,
    no_empty_line,
    extra_empty_line,
    wrong_label,
    consecutive_empty_line,
    empty_line_start,
    empty_token
):
    vars = [
        extra_white_space,
        not_enough_data,
        no_empty_line,
        extra_empty_line,
        wrong_label,
        consecutive_empty_line,
        empty_line_start,
        empty_token
    ]
    filename = []
    for var in vars:
        filename.append('1' if var else '0')
    filename = ''.join(filename)

    validator = NLPNERDataValidator()
    open_mock = MagicMock(side_effect=open_ner_file)
    should_pass = not any(vars)
    with patch("builtins.open", new=open_mock):
        passed = True
        try:
            validator.validate("mock_ner", filename, filename)
            validator.validate("mock_ner", filename)
        except DataException:
            passed = False
        assert should_pass == passed, "{}, {}, {}, {}, {}, {}, {}, {}".format(*vars)

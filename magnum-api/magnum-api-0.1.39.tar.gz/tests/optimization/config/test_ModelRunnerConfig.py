import pytest

from magnumapi.commons import json_file
from magnumapi.optimization.config.ModelRunnerConfig import ModelRunnerConfig
from tests.resource_files import create_resources_path
from tests.resources.optimization.config.model_runner_config_str import model_runner_config_str_ref


# arrange
model_runner_config_path = create_resources_path('resources/optimization/config/model_runner_config.json')
model_runner_config_dct = json_file.read(model_runner_config_path)

# act
model_runner_config = ModelRunnerConfig.initialize_config(model_runner_config_dct)


def test_initialize_config():
    # assert
    assert model_runner_config_str_ref == str(model_runner_config)


def test_get_weight():
    # arrange
    objective = 'B_3_1'

    # act
    weight = model_runner_config.get_weight(objective)

    # assert
    assert 0.1 == weight


def test_get_weight_error():
    # arrange
    objective = 'b7'

    # act
    with pytest.raises(KeyError) as context:
        model_runner_config.get_weight(objective)

    # assert
    assert 'Objective name b7 not present in objective configs.' in str(context.value)


def test_get_constraint():
    # arrange
    objective = 'B_3_1'

    # act
    constraint = model_runner_config.get_constraint(objective)

    # assert
    assert 0 == constraint


def test_get_constraint_error():
    # arrange
    objective = 'b7'

    # act
    with pytest.raises(KeyError) as context:
        model_runner_config.get_constraint(objective)

    # assert
    assert 'Objective name b7 not present in objective configs.' in str(context.value)

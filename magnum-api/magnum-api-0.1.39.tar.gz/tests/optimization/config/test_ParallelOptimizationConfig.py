import pytest

from magnumapi.optimization.config.ParallelOptimizationConfig import ParallelOptimizationConfig
from tests.resource_files import create_resources_path
from tests.resources.optimization.parallel.parallel_config_str import config_str

json_path = create_resources_path('resources/optimization/parallel/parallel_config.json')
config = ParallelOptimizationConfig.initialize_config(json_path)


def test_initialize_config():
    # arrange
    # act
    # assert

    assert config_str == str(config)


def test_get_weight():
    # arrange
    objective = 'B_3_1'

    # act
    weight = config.get_weight(objective)

    # assert
    assert 0.1 == weight


def test_get_weight_error():
    # arrange
    objective = 'B_7_1'

    # act
    with pytest.raises(KeyError) as exc_info:
        config.get_weight(objective)

    # assert
    assert 'Objective name B_7_1 not present in objective configs.' in str(exc_info.value)


def test_get_constraint():
    # arrange
    objective = 'B_3_1'

    # act
    constraint = config.get_constraint(objective)

    # assert
    assert 0 == constraint


def test_get_constraint_error():
    # arrange
    objective = 'B_7_1'

    # act
    with pytest.raises(KeyError) as exc_info:
        config.get_constraint(objective)

    # assert
    assert 'Objective name B_7_1 not present in objective configs.' in str(exc_info.value)

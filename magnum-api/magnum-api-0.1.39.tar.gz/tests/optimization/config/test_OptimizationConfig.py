from magnumapi.optimization.config.OptimizationConfig import OptimizationConfig
from tests.resource_files import create_resources_path
from tests.resources.optimization.config.genetic_optimization_config_str import config_str_ref

json_path = create_resources_path('resources/optimization/config/genetic_optimization_config.json')
config = OptimizationConfig.initialize_config(json_path)


def test_initialize_config():
    # arrange
    # act
    # assert

    assert config_str_ref == str(config)

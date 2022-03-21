import yaml

import sonusai
from sonusai import SonusAIError
from sonusai import logger


def get_default_config() -> dict:
    # Load default config
    try:
        with open(file=sonusai.mixture.default_config, mode='r') as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        logger.error(f'Error loading genmixdb default config: {e}')
        raise SonusAIError


def check_truth_setting(truth_setting: dict, default: dict = None) -> None:
    required_keys = [
        'function',
        'config',
        'index',
    ]
    for key in required_keys:
        if key not in truth_setting:
            if default is not None and key in default:
                truth_setting[key] = default[key]
            else:
                logger.error(f'Missing {key} in truth_settings')
                raise SonusAIError


def get_config_from_file(config_name: str) -> dict:
    config = get_default_config()

    try:
        # Load given config
        with open(file=config_name, mode='r') as file:
            given_config = yaml.safe_load(file)

        # Use default config as base and overwrite with given config keys as found
        for key in config:
            if key in given_config:
                config[key] = given_config[key]

        required_keys = [
            'class_labels',
            'class_weights_threshold',
            'dither',
            'feature',
            'frame_size',
            'noises',
            'noise_augmentations',
            'num_classes',
            'seed',
            'target_augmentations',
            'targets',
            'truth_settings',
            'truth_mode',
            'truth_reduction_function',
        ]
        for key in required_keys:
            if key not in config:
                logger.error(f'Missing {key} in config')
                raise SonusAIError

        check_truth_setting(config['truth_settings'])
        return config
    except Exception as e:
        logger.error(f'Error preparing genmixdb config: {e}')
        raise SonusAIError

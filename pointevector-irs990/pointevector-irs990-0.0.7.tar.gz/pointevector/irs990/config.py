from pathlib import Path
from typing_extensions import TypedDict, NotRequired
from typing import Any, Dict, List
from ruamel.yaml import YAML

from pointevector.xml_parser import ParserConfig, validate as validate_parser_config

def _check_for_unknown_keys(cls, config: Dict):
    for key in config:
        if key not in cls.__annotations__:
            raise TypeError(f"Unknown key in {cls} configuration: {key}")

def _check_if_paths_exist(cls, config: Dict):
    for k, v in cls.__annotations__.items():
        if v == Path:
            config[k] = Path(config[k])
            if not config[k].exists():
                raise OSError(f"Could not find path to '{k}'")

def _validate_parser(path: str) -> ParserConfig:
    config_path = Path(path)
    if not config_path.exists():
        raise OSError('Could not find path to parser')

    return validate_parser_config(YAML(typ='safe').load(config_path.read_text()))

class CacheConfig(TypedDict):
    archive_directory: Path
    cache_directory: Path
    company_map: Path
    parser: ParserConfig
    partition_dimension: NotRequired[str]

def _validate_cache(config: Dict) -> CacheConfig:
    _check_for_unknown_keys(CacheConfig, config)
    _check_if_paths_exist(CacheConfig, config)
    if not config['archive_directory'].is_dir():
        raise TypeError('archive_directory must be a directory')
    if not config['cache_directory'].is_dir():
        raise TypeError('cache_directory must be a directory')
    config['parser'] = _validate_parser(config['parser'])
    if 'partition_dimension' in config:
        config['partition_dimension'] = str(config['partition_dimension'])

class Plugin(TypedDict):
    plugin: str
    script: Path
    inputs: NotRequired[Dict[str, Any]]

def _validate_plugin(config: Dict) -> Plugin:
    _check_if_paths_exist(Plugin, config)
    config['plugin'] = str(config['plugin'])
    return config
class Config(TypedDict):
    output: Path
    earliest_year: int
    latest_year: NotRequired[int]
    cache: CacheConfig
    plugins: List[Plugin]
    
def validate(config: Dict) -> Config:
    _check_for_unknown_keys(Config, config)
    config['output'] = Path(config['output'])
    config['earliest_year'] = int(config['earliest_year'])
    if 'latest_year' in config:
        config['latest_year'] = int(config['latest_year'])
    _validate_cache(config['cache'])
    config['plugins'] = [_validate_plugin(plugin) for plugin in config['plugins']]
    return config

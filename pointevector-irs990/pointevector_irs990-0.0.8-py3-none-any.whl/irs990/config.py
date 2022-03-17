from pathlib import Path
from typing_extensions import TypedDict, NotRequired
from typing import Any, Dict, List
from ruamel.yaml import YAML

from pointevector.xml_parser import ParserConfig, validate as validate_parser_config

def _check_for_unknown_keys(cls, config: Dict):
    for key in config:
        if key not in cls.__annotations__:
            raise TypeError(f"Unknown key in {cls} configuration: {key}")

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

    # Archive directory
    config['archive_directory'] = Path(config['archive_directory'])
    if not config['archive_directory'].exists():
        raise OSError('Could not find path to archive_directory')
    if not config['archive_directory'].is_dir():
        raise TypeError('archive_directory must be a directory')
    
    # Cache directory
    config['cache_directory'] = Path(config['cache_directory'])
    if not config['cache_directory'].exists():
        config['cache_directory'].mkdir(parents=True)
    else:
        if not config['cache_directory'].is_dir():
            raise TypeError('cache_directory must be a directory')
    
    # Company map
    config['company_map'] = Path(config['company_map'])
    if not config['company_map'].exists():
        raise OSError('Could not find path to company_map')
    
    # Parser
    config['parser'] = _validate_parser(config['parser'])

    # Partition dimension
    if 'partition_dimension' in config:
        config['partition_dimension'] = str(config['partition_dimension'])

class Plugin(TypedDict):
    plugin: str
    script: Path
    inputs: NotRequired[Dict[str, Any]]

def _validate_plugin(config: Dict) -> Plugin:
    config['plugin'] = str(config['plugin'])
    config['script'] = Path(config['script'])
    if not config['script'].exists():
        raise OSError('Could not find path to script')
    return config
class Config(TypedDict):
    output: Path
    earliest_year: int
    latest_year: NotRequired[int]
    cache: CacheConfig
    plugins: List[Plugin]
    
def validate(config: Dict) -> Config:
    _check_for_unknown_keys(Config, config)

    # Output
    config['output'] = Path(config['output'])
    if not config['output'].exists():
        config['output'].mkdir(parents=True)
    else:
        if not config['output'].is_dir():
            raise TypeError('output must be a directory')
    
    # Earliest year
    config['earliest_year'] = int(config['earliest_year'])

    # Latest year
    if 'latest_year' in config:
        config['latest_year'] = int(config['latest_year'])

    # Cache
    _validate_cache(config['cache'])

    # Plugins
    config['plugins'] = [_validate_plugin(plugin) for plugin in config['plugins']]
    
    return config

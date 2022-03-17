import argparse
import logging
import importlib
from pathlib import Path
from ruamel.yaml import YAML

from pointevector.irs990.index import build as build_index
from pointevector.irs990.cache import build as build_cache
from pointevector.irs990.config import validate

def main():
    # Create argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', '-f', type=Path, default='.config.yaml')
    args, _ = parser.parse_known_args()

    # Validate configuration
    config = validate(YAML(typ='safe').load(Path(args.config).read_text()))

    # Ensure cache index exists
    cache_config = config['cache']
    if not cache_config['cache_directory'].joinpath('index.csv').exists():
        if not cache_config['archive_directory'].joinpath('index.csv').exists():
            logging.warning('Could not find archive index, so building it...')
            build_index(cache_config, cache=False)
        logging.warning('Could not find cache index, so building it...')
        build_cache(cache_config)
        build_index(cache_config)

    # Run plugins
    for plugin in config['plugins']:
        path = plugin['script'].relative_to('.')
        mod = '.'.join([*path.parent.parts, path.stem])
        p = importlib.import_module(mod)
        p.main(config, plugin)

# Execute
main()

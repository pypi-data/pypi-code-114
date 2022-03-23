from argparse import ArgumentParser
from pathlib import Path

from talisman_tools.configure import configure_model, read_json_config


def main():
    parser = ArgumentParser()
    parser.add_argument('configs_paths', nargs='+', type=str, metavar='<config path>')
    parser.add_argument('out_path', type=str, metavar='<model out path>')
    args = parser.parse_args()

    configs = [read_json_config(cfg) for cfg in args.configs_paths]
    model = configure_model(configs)
    model.save(Path(args.out_path))
    print(f"Saved {model} model")


if __name__ == '__main__':
    main()

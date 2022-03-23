from argparse import ArgumentParser
from pathlib import Path

from talisman_tools.configure import read_json_config, wrap_model_from_config
from talisman_tools.plugin import WrapperActionsPlugins
from tp_interfaces.abstract import AbstractDocumentProcessor


def main():
    parser = ArgumentParser()
    parser.add_argument('wrapper_config', type=str, metavar='<config path>')
    parser.add_argument('out_path', type=str, metavar='<model out path>')
    parser.add_argument('models', nargs='+', type=str, metavar='<model name> <model path>')
    args = parser.parse_args()

    config = read_json_config(args.wrapper_config)

    if len(args.models) % 2 != 0:
        raise Exception('Expected <model name> <model path>')

    for i in range(0, len(args.models), 2):
        model_name = args.models[i]
        model_path = Path(args.models[i + 1])
        WrapperActionsPlugins.add_wrapper_action(frozenset((model_name,)), lambda c, path=model_path: AbstractDocumentProcessor.load(path))

    model = wrap_model_from_config(config)

    model.save(Path(args.out_path))
    print(f"Wrapped {model}")


if __name__ == '__main__':
    main()

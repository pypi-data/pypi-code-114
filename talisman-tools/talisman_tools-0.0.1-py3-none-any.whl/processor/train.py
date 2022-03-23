from argparse import ArgumentParser
from pathlib import Path
from typing import Callable, Optional, Tuple

from tdm.datamodel import TalismanDocument

from talisman_tools.configure import read_json_config
from talisman_tools.plugin import ReaderPlugins, TrainerPlugins
from talisman_tools.servers.helper import add_extra_cli_argumants
from tp_interfaces.readers.abstract import AbstractReader


def _read_docs(reader: Callable[[Path], AbstractReader], path: Optional[str]) -> Optional[Tuple[TalismanDocument, ...]]:
    if path is None:
        return None
    return tuple(reader(Path(path)).read())


def main():
    readers = ReaderPlugins.flattened

    parser = ArgumentParser()
    parser.add_argument('reader', metavar='<reader type>', choices=set(readers.keys()))
    parser.add_argument('train_path', type=str, metavar='<train docs path>')
    parser.add_argument('config_path', type=str, metavar='<config.json>')
    parser.add_argument('out_model_path', type=str, metavar='<out model path>')
    parser.add_argument('-dev_path', type=str, metavar='<dev docs path>')
    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    reader = readers[args.reader]

    train_docs = _read_docs(reader, args.train_path)
    dev_docs = _read_docs(reader, args.dev_path)
    config = read_json_config(args.config_path)

    trainer = TrainerPlugins.plugins[config['plugin']][config['model']](config['config'])

    trained_model = trainer.train(train_docs, dev_docs)
    trained_model.save(Path(args.out_model_path))


if __name__ == '__main__':
    main()

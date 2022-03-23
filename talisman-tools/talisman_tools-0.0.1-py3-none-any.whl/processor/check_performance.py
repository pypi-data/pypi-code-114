import time
from argparse import ArgumentParser
from pathlib import Path
from typing import Tuple

from tdm.datamodel import TalismanDocument

from talisman_tools.plugin import ReaderPlugins
from talisman_tools.servers.helper import add_extra_cli_argumants
from tp_interfaces.abstract import AbstractDocumentProcessor


def _get_time(docs: Tuple[TalismanDocument], model: AbstractDocumentProcessor):
    start_time = time.time()
    config_type = model.config_type
    model.process_docs(docs, config_type())
    end_time = time.time()

    return end_time - start_time


def _measure_time(docs: Tuple[TalismanDocument], model: AbstractDocumentProcessor, count: int):
    print('Time:')
    average_time = 0

    for _ in range(count):
        current_time = _get_time(docs, model)
        average_time += current_time
        print(f'\t{current_time}')

    average_time /= count
    print(f'Average: {average_time}\n')


if __name__ == '__main__':
    readers = ReaderPlugins.flattened

    parser = ArgumentParser()
    parser.add_argument('reader', metavar='<reader type>', choices=set(readers.keys()))
    parser.add_argument('docs_path', type=str, metavar='<docs to extract entities path>')
    parser.add_argument('model_path', type=str, metavar='<model path>')
    parser.add_argument('count', type=int, metavar='<launch count>')
    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    docs = tuple(readers[args.reader](Path(args.docs_path)).read())
    count = args.count

    with AbstractDocumentProcessor.load(Path(args.model_path)) as model:
        _measure_time(docs, model, count)

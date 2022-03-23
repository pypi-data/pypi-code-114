from argparse import ArgumentParser
from pathlib import Path

from talisman_tools.configure import load_or_configure
from talisman_tools.plugin import ReaderPlugins, SerializerPlugins
from talisman_tools.servers.helper import add_extra_cli_argumants
from tp_interfaces.helpers.io import read_json

if __name__ == '__main__':
    readers = ReaderPlugins.flattened
    serializers = SerializerPlugins.flattened

    parser = ArgumentParser()
    parser.add_argument('reader', metavar='<reader type>', choices=set(readers.keys()))
    parser.add_argument('docs_path', type=Path, metavar='<docs to be processed>')

    parser.add_argument('-models', nargs='+', type=Path, metavar='<model path>', default=[])
    parser.add_argument('-cfg', nargs='+', type=Path, metavar='<model json config path>', default=[])

    parser.add_argument('-config', type=Path, metavar='<document processing config path>')

    parser.add_argument('serializer', metavar='<serializer type>', choices=set(serializers.keys()))
    parser.add_argument('out_path', type=Path, metavar='<processed docs path>')

    parser.add_argument('-batch', type=int, metavar='<batch size>', default=1000)

    extra_actions = add_extra_cli_argumants(parser)

    args = parser.parse_args()

    for action in extra_actions:
        action(args)

    processor = load_or_configure(args.models, args.cfg)

    reader = readers[args.reader](args.docs_path)
    serializer = serializers[args.serializers]()

    with processor:
        processor_config_type = processor.config_type
        config = processor_config_type.parse_obj(read_json(args.config)) if args.config else processor_config_type()
        serializer.serialize(processor.process_stream(reader.read(), config, args.batch), args.out_path)

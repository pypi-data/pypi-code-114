from argparse import ArgumentParser
from pathlib import Path

from talisman_tools.plugin import ReaderPlugins, SerializerPlugins


def main():
    readers = ReaderPlugins.flattened
    serializers = SerializerPlugins.flattened

    parser = ArgumentParser()
    parser.add_argument('reader', metavar='<reader type>', choices=set(readers.keys()))
    parser.add_argument('docs_path', type=str, metavar='<train docs path>')
    parser.add_argument('output', metavar='<output path>')
    parser.add_argument('-serializer', type=str, metavar='<serializer type>', choices=set(serializers.keys()), default='default')

    args = parser.parse_args()

    reader = readers[args.reader](Path(args.docs_path))
    serializer = serializers[args.serializer]()

    serializer.serialize(reader.read(), Path(args.output))


if __name__ == '__main__':
    main()

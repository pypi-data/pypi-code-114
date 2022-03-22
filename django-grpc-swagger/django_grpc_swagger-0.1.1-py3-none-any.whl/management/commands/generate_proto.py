
import pkg_resources
from grpc_tools import protoc
from django.core.management.base import BaseCommand
from django_grpc_swagger import PACKAGE, serializer_handler


class Command(BaseCommand):

    def run(self, **options):
        protofile = PACKAGE + ".proto"
        content = serializer_handler.generate_proto()
        with open(protofile, "w") as f:
            f.write(content)
        proto_include = pkg_resources.resource_filename('grpc_tools', '_proto')
        # python3 -m grpc_tools.protoc --proto_path=./ --python_out=./ --grpc_python_out=./ ./aa.proto
        args = ['', '--proto_path=./', '--python_out=./',
                '--grpc_python_out=./', protofile]
        protoc.main(args + [f'-I{proto_include}'])

    def handle(self, *args, **options):
        self.run(**options)

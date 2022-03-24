import subprocess

from cleo.commands.command import Command
from poetry.plugins.application_plugin import ApplicationPlugin

from sphinx.cmd.build import main


class BuildDocCommand(Command):

    name = "doc"

    def handle(self) -> int:
        # self.line("My doc command")

        args = [
            "-T",
            "-b",
            "html",
            "-D",
            "language=fr",
            "docs",
            "htmldoc",
        ]
        return main(args)


class BaselineCommand(Command):

    name = "baseline"

    def handle(self) -> int:
        # self.line("My baseline command")

        cmd = ["python", "-m", "pytest", "--mpl-generate-path=tests/baseline", "tests"]
        subprocess.run(cmd)

        return 0


def bld_doc_factory():
    return BuildDocCommand()


def baseline_factory():
    return BaselineCommand()


class BlocksimApplicationPlugin(ApplicationPlugin):
    def activate(self, application):
        application.command_loader.register_factory("doc", bld_doc_factory)
        application.command_loader.register_factory("baseline", baseline_factory)

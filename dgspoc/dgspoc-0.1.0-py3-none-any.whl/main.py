"""Module containing the logic for describe-get-system proof of conception entry-points."""

import sys
import argparse

from dgspoc import version
from dgspoc.config import Data
from dgspoc.utils import Printer
from dgspoc.usage import validate_usage
from dgspoc.usage import show_usage

from dgspoc.operation import do_build_template


def show_dependency(options):
    if options.command == 'dependency':
        lst = [
            'Describe-Get-System Proof of Concept',
            Data.get_app_info(),
            '--------------------',
            'Dependencies:'
        ]

        for pkg in Data.get_dependency().values():
            lst.append('  + Package: {0[package]}'.format(pkg))
            lst.append('             {0[url]}'.format(pkg))

        Printer.print(lst)
        sys.exit(0)


def show_info(options):
    command, operands = options.command, options.operands
    if command == 'info':
        validate_usage(command, operands)

        if len(operands) > 1:
            show_usage(command)

        lst = ['Describe-Get-System Proof of Concept', Data.get_app_info()]

        info_type = operands[0].lower() if operands else ''
        if info_type and info_type in ['all', 'dependency']:
            lst.append('--------------------')
            lst.append('Dependencies:')
            for pkg in Data.get_dependency().values():
                lst.append('  + Package: {0[package]}'.format(pkg))
                lst.append('             {0[url]}'.format(pkg))

        if info_type and info_type in ['all', 'template']:
            lst.append('--------------------',)
            lst.append(Data.get_template_storage_info())

        Printer.print(lst)
        sys.exit(0)


def show_version(options):
    if options.command == 'version':
        print('{} v{}'.format(Cli.prog, version))
        sys.exit(0)


class Cli:
    """describe-get-system proof of concept console CLI application."""
    prog = 'dgs'
    prog_fn = 'describe-get-system'
    commands = ['build', 'check', 'info', 'run', 'test', 'version']

    def __init__(self):
        parser = argparse.ArgumentParser(
            prog=self.prog,
            usage='%(prog)s [options] command operands',
            description='{} proof of concept'.format(self.prog_fn),
        )

        parser.add_argument(
            '-v', '--version', action='version',
            version='%(prog)s v{}'.format(version)
        )

        parser.add_argument(
            '-a', '--author', type=str, default='',
            help="author's name"
        ),

        parser.add_argument(
            '-e', '--email', type=str, default='',
            help="author's email"
        ),

        parser.add_argument(
            '-c', '--company', type=str, default='',
            help="author's company"
        ),

        parser.add_argument(
            '-s', '--save', type=str, dest='filename', default='',
            help="saving to file"
        ),

        parser.add_argument(
            '-i', '--template-id', type=str, dest='tmplid', default='',
            help="template ID"
        ),

        parser.add_argument(
            '-t', '--test-data', type=str, dest='testdata', default='',
            help="test data"
        ),

        parser.add_argument(
            '--adaptor', type=str, default='',
            help="connector adaptor"
        ),

        parser.add_argument(
            '--replaced', action='store_true',
            help='overwrite template ID/file'
        )

        parser.add_argument(
            'command', type=str,
            help='command must be either build, check,'
                 ' info, run, test, or version'
        )
        parser.add_argument(
            'operands', nargs='*', type=str,
            help='operands can be template, unittest, '
                 'pytest, robotframework, script, or data such command-line, '
                 'config-lines, or filename'
        )

        self.parser = parser
        self.options = self.parser.parse_args()
        self.kwargs = dict()

    def validate_command(self):
        """Validate argparse `options.command`.

        Returns
        -------
        bool: show ``self.parser.print_help()`` and call ``sys.exit(1)`` if
        command is neither build, check, info, run,
        test, nor version, otherwise, return True
        """
        self.options.command = self.options.command.lower()

        if self.options.command in self.commands:
            return True
        self.parser.print_help()
        sys.exit(1)

    def run(self):
        """Take CLI arguments, parse it, and process."""
        self.validate_command()

        options = self.options

        show_version(options)
        show_info(options)

        do_build_template(options)


def execute():
    """Execute template console CLI."""
    app = Cli()
    app.run()

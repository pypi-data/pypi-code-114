# -*- coding: utf-8 -*-
# MIT License
#
# Copyright (c) 2022 David E. Lambert
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""Command line interface for tealc.

Code in this module is run when tealc is tun from the command line.
    This package contains no public objects. Documentation for the CLI
    is contained externally in tealc.manual, which is accessible
    via the command line with ``tealc help``.
"""

from pathlib import Path
import pydoc
import argparse

from tealc import StringTension, StringSet, SetFileParser

PKG_DIR = Path(__file__).parent

msg = {
    'string': 'calculate tension for a single string',
    'set': 'calculate tensions for a set of strings',
    'gauge': 'inches, 1/1000 of an inch, or mm with --si flag',
    'mat': 'options: ps, nps, pb, 8020, 8515, ss, fw, pn, bnps, bss, bfw',
    'pitch': 'e.g. A1, Bb2, C#3. C4 is middle C',
    'length': 'scale length in inches, or mm with --si flag',
    'si': 'supply gauge and length units in mm; get tension in kg',
    'title': 'optional title for output chart',
    'file': 'see tealc -h for format'
}

set_usage = """tealc set [-h] [--file FILE] [--title TITLE]
    tealc set [-h] [--length LENGTH] [--gauges [G ...]]
                        [--materials [M ...]] [--pitches [P ...]]
                        [--si] [--title TITLE]"""

parser = argparse.ArgumentParser(prog='tealc')
subparsers = parser.add_subparsers(dest='command')

string_parser = subparsers.add_parser('string', help=msg['string'])
string_parser.add_argument('gauge', type=float, help=msg['gauge'])
string_parser.add_argument('material', metavar='material', help=msg['mat'],
                           choices=['ps', 'nps', 'pb', '8020', '8515', 'ss',
                                    'fw', 'pn', 'bnps', 'bss', 'bfw'])
string_parser.add_argument('pitch', help=msg['pitch'])
string_parser.add_argument('length', type=float, help=msg['length'])
string_parser.add_argument('--si', action='store_true', help=msg['si'])

set_parser = subparsers.add_parser('set', help=msg['set'], usage=set_usage)
set_parser.add_argument('--file', help=msg['file'])
set_parser.add_argument('--length', type=float, help=msg['length'])
set_parser.add_argument('--gauges', nargs='*', metavar='G', help=msg['gauge'])
set_parser.add_argument('--materials', nargs='*', metavar='M', help=msg['mat'])
set_parser.add_argument('--pitches', nargs='*', metavar='P', help=msg['pitch'])
set_parser.add_argument('--si', help=msg['si'], action='store_true')
set_parser.add_argument('--title', help=msg['title'])

help_parser = subparsers.add_parser('help', help='print manual',
                                    add_help=False)


def print_manual():
    """Print the manual."""
    with open(PKG_DIR/'manual.txt', 'r') as m:
        manual = m.read()
    pydoc.pager(manual)


def main(args: list = None):
    """Command line interface for tealc.

    Args:
        args (list[str], optional): Argument list. The default of
            ``None`` will read sys.argv
    """
    parsed_args = parser.parse_args(args)

    if parsed_args.command == 'string':
        tension = StringTension(parsed_args.gauge, parsed_args.material,
                                parsed_args.pitch, parsed_args.length,
                                parsed_args.si)
        if parsed_args.si:
            print('{:.1f} kg'.format(tension.kg))
        else:
            print('{:.1f} lb'.format(tension.lb))

    elif parsed_args.command == 'set':
        if parsed_args.file is None:
            tension = StringSet(parsed_args.length, parsed_args.gauges,
                                parsed_args.materials, parsed_args.pitches,
                                parsed_args.si)
        else:
            sf = SetFileParser(parsed_args.file)
            tension = StringSet(sf.length, sf.gauges,
                                sf.materials, sf.pitches,
                                sf.si)

        if parsed_args.si:
            tension.print(parsed_args.title, print_si=True)
        else:
            tension.print(parsed_args.title)

    elif parsed_args.command == 'help':
        print_manual()

    else:
        parser.print_help()


if __name__ == '__main__':
    main()

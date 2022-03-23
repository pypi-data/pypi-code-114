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

import click

from tealc import StringTension, StringSet, SetFileParser, print_material_codes

PKG_DIR = Path(__file__).parent


@click.group()
@click.version_option()
def cli():
    """Calculate tension estimates for a single string or string set."""
    pass


@click.command()  # tealc string
@click.argument('gauge', type=float)
@click.argument('material', type=str)
@click.argument('pitch', type=str)
@click.argument('length', type=float)
@click.option('--si', is_flag=True,
              help="Supply gauge and length units in mm; get tension in kg.")
def string(gauge, material, pitch, length, si):
    """Calucate tension estimate for a single string.

    \b
    GAUGE       String gauge in 1/1000 inch (10) or inches (.010).
    MATERIAL    String material code, with options:
                ps, nps, pb, 8020, 8515, ss, fw, pn, bnps, bss, bfw.
                (Use "tealc materials" descriptions.)
    PITCH       Scientific pitch notation, A0-E5.
    LENGTH      Scale length of instrument/string in inches.
    """
    tension = StringTension(gauge, material, pitch, length, si)
    if si:
        click.echo('{:.1f} kg'.format(tension.kg))
    else:
        click.echo('{:.1f} lb'.format(tension.lb))


@click.command()  # tealc set
@click.option('-l', '--length', type=float, metavar='LENGTH', required=True,
              help="Scale length of instrument/string in inches.")
@click.option('-s', '--string', 'strings', type=(float, str, str),
              metavar='<GAUGE MATERIAL PITCH>...', multiple=True,
              help="""\b
              GAUGE     String gauge in 1/1000 inch (10) or inches (.010).
              MATERIAL  String material code, with options:
                        ps, nps, pb, 8020, 8515, ss, fw, pn, bnps, bss, bfw.
                        (Use "tealc materials" for descriptions.)
              PITCH     Scientific pitch notation, A0-E5.
              """)
@click.option('--si', is_flag=True,
              help="Supply gauge and length units in mm; get tension in kg.")
@click.option('--title', type=str, help="Optional title for output chart.")
def set(length, strings, si, title):
    """Calculate tension estimates for a string set."""
    gauges = [tup[0] for tup in strings]
    materials = [tup[1] for tup in strings]
    pitches = [tup[2] for tup in strings]
    tension = StringSet(length, gauges, materials, pitches, si)
    tension.print(title, print_si=si)


@click.command()  # tealc file
@click.argument('setfile', type=click.Path(exists=True))
@click.option('--si', is_flag=True, help="Output chart units in mm/kg.")
@click.option('--title', type=str, help="Optional title for output chart.")
def file(setfile, si, title):
    """Calculate string set tension estimates from a file.

    \b
    SETFILE     Path to a plain text file using the format:
                    length = LENGTH
                    GAUGE MATERIAL PITCH
                    [GAUGE MATERIAL PITCH]
                    [...]
                    [si = True or False]
    """
    sf = SetFileParser(setfile)
    tension = StringSet(sf.length, sf.gauges, sf.materials, sf.pitches, sf.si)
    tension.print(title, print_si=si)


@click.command()
def help():
    """Open the tealc manual."""
    with open(PKG_DIR/'manual.txt', 'r') as m:
        manual = m.read()
    click.echo_via_pager(manual)


@click.command()
def materials():
    """Print a chart of string material codes and descriptions."""
    print_material_codes(padding=4)


cli.add_command(string)
cli.add_command(set)
cli.add_command(file)
cli.add_command(help)
cli.add_command(materials)

if __name__ == '__main__':
    cli()

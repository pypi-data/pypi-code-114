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

"""Primary objects for tealc package.

Classes:
    StringTension
    StringSet
    SetFileParser

Functions:
    print_material_codes(padding=0)

Attributes:
    unit_weights (dict): Weights in lb/inch for strings of a given
        construction material and gauge. Used in tension calculations
        when gauge is available in this dict. Data are based on
        published unit weights from a major US-based manufacturer.
    tension_coefs (dict): Coefficients to estimate unit weights for a
        given gauge and material when unavailable from unit_weights.
        Coefficients are derived from per-material models of the form
        weight = coef * gauge_squared + e, using the unit_weights data,
         as well as data from a second major US-based manufacturer.
    frequency_chart (dict): Frequencies in Hz for named pitches in
        scientific pitch notation in the supported range of A0-E5
        (low string on a down-tuned 5-string bass to high course on a
        standard-tuned mandolin/violin).
    material_codes(dict): Short codes for string construction materials
        and corresponding descriptions, e.g. 'ps': 'plain steel'.
    manual (str): A plain text manual for the command-line interface
        to tealc available from __main__.py.
"""

from pathlib import Path
import json
import re

PKG_DIR = Path(__file__).parent

with open(PKG_DIR/'unit_weights.json', 'r') as f:
    unit_weights = json.load(f)

with open(PKG_DIR/'tension_models.json', 'r') as f:
    tension_models = json.load(f)

with open(PKG_DIR/'frequency_chart.json', 'r') as f:
    frequency_chart = json.load(f)

with open(PKG_DIR/'material_codes.json', 'r') as f:
    material_codes = json.load(f)

with open(PKG_DIR/'manual.txt', 'r') as f:
    manual = f.read()

_err_msg = {
    'gauge': 'gauge(s) must be numbers',
    'mat': 'invalid material code(s): see tealc.print_material_codes()',
    'pitch': 'invalid pitch(es): use scientific pitch notation from A0-E5',
    'length': 'length must be a number',
    'si': 'si must be a boolean',
    'arglen': 'gauges, materials, and pitches must be of equal length'
}


def print_material_codes(padding=0):
    """Print valid string material codes and descriptions."""
    just = 4 + padding
    print('code'.rjust(just), 'material', sep='  ',)
    print('----'.rjust(just), '--------', sep='  ')
    for k, v in material_codes.items():
        print(k.rjust(just), v, sep='  ')


class StringTension:
    """Estimate string tension.

    Attributes:
        gauge (float): In inches.
        gauge_mm (float): In millimeters.
        material (str): String construction material code.
        pitch (str): Scientific pitch notation.
        length (float): In inches.
        length_mm (float): In millimeters.
        unit_weight (float): In pounds/inch.
        lb (float): Tension in pounds.
        kg (float): Tension in kilograms (yes, it should be Newtons.)

    Args:
        gauge (float): In inches, 1/1000in,or mm with si=True.
        material (str): Valid material code.
        pitch (str): Scientific pitch notation from A0-E5.
        length (float): Instrument scale length in inches,
            1/1000in, or mm with si=True.
        si (bool, optional): Supply unit in mm. Defaults to False.

    Raises:
        KeyError: On invalid material code or pitch.
    """

    def __init__(self, gauge: float, material: str, pitch: str, length: float,
                 si=False):
        """Class constructor."""
        if si:
            self.gauge = round(gauge / 25.4, 3)
            self.gauge_mm = gauge
            self.length = length / 25.4
            self.length_mm = length
        else:
            if gauge > 2:
                self.gauge = gauge / 1000
                self.gauge_mm = (gauge / 1000) * 25.4
            else:
                self.gauge = gauge
                self.gauge_mm = gauge * 25.4
            self.length = length
            self.length_mm = length * 25.4

        try:
            self.material = material
            assert self.material in material_codes.keys()
        except Exception:
            raise KeyError(_err_msg['mat'])

        try:
            self.pitch = pitch[0].upper() + pitch[1:]  # allow lowercase pitch
            assert self.pitch in frequency_chart.keys()
        except Exception:
            raise KeyError(_err_msg['pitch'])

        self.unit_weight = self.get_unit_weight()
        self.lb = self.tension()
        self.kg = self.tension() / 2.205

    def get_unit_weight(self):
        """Derive unit weight from string properties.

        Returns:
            float: Unit weight in pounds/inch.
        """
        mat = self.material
        if str(self.gauge) not in unit_weights[self.material]:
            unit_weight = (tension_models[mat]['const']
                           + tension_models[mat]['coef'] * self.gauge**2)
        else:
            unit_weight = unit_weights[self.material][str(self.gauge)]

        return unit_weight

    def tension(self):
        """Calculate string tension.

        Returns:
            float: Estimated string tension in lb.
        """
        lb = ((self.unit_weight
               * (2 * frequency_chart[self.pitch] * self.length)**2)
              / 386.4)
        return lb


class StringSet:
    """Estimated individual and total tensions for a set of strings.

    Attributes:
        strings (list): StringTension object for each string in set.
        set_lb (float): Total set tension in pounds.
        set_kg (float): Total set tension in kilograms.

    Args:
        length (float): Instrument scale length in inches, 1/1000in,
            or mm with si=True.
        gauges (list[float]): List of string gauges in inches,
            1/1000in, or mm with si=True.
        materials (list[str]): List of valid string material codes.
        pitches (list[str]): List of pitches in scientific pitch
            notation, from A0-E5.
        si (bool, optional): Supply length and gauges in mm.
            Defaults to False.

    Raises:
        TypeError: On non-numeric length or gauges.
        KeyError: On invalid material codes or pitches.
        ValueError: On non-boolean si.
        AssertionError: On gauges, materials, and pitches lists
            of differing length.
    """

    def __init__(self, length: float, gauges: list,
                 materials: list, pitches: list,
                 si=False):
        """Class constructor."""
        self.si = si

        try:
            assert type(length) in (float, int)
        except Exception:
            raise TypeError(_err_msg['length'])
        finally:
            if self.si:
                self.length = length / 25.4
                self.length_mm = length
            else:
                self.length = length
                self.length_mm = self.length * 25.4

        try:
            assert all(type(g) in (float, int) for g in gauges)
        except Exception:
            raise TypeError(_err_msg['gauge'])
        finally:
            if self.si:
                self.gauges = [g / 25.4 for g in gauges]
                self.gauges_mm = gauges
            else:
                self.gauges = gauges
                self.gauges_mm = [g * 25.4 for g in gauges]

        try:
            self.materials = materials
            assert all(m in material_codes.keys() for m in self.materials)
        except Exception:
            raise KeyError(_err_msg['mat'])

        try:
            self.pitches = pitches
            assert all([p[0].upper() + p[1:] in frequency_chart.keys()
                        for p in self.pitches])
        except Exception:
            raise KeyError(_err_msg['pitch'])

        try:
            assert len(self.gauges) == len(self.materials) == len(self.pitches)
        except Exception:
            raise AssertionError(_err_msg['arglen'])

        n_strings = len(self.gauges)
        setlist = zip(self.gauges, self.materials, self.pitches,
                      [self.length] * n_strings)

        self.strings = [StringTension(*s) for s in setlist]
        self.set_lb = sum(s.lb for s in self.strings)
        self.set_kg = sum(s.kg for s in self.strings)

    def print(self, title: str = None, print_si: bool = False):
        """Print a chart of individual string and set total tensions.

        Args:
            title (str, optional): Chart title. Defaults to None.
            print_si (bool, optional): Whether to print scale units
                in mm and tension units in kg. Defaults to False.
        """
        col_width = 10
        cols = ['Gauge', 'Material', 'Pitch', 'Tension']
        table_width = col_width * len(cols)

        p_str = "s.pitch.rjust(col_width)"
        m_str = "s.material.rjust(col_width)"

        if print_si:
            l_str = 'Scale length: {:.1f}mm '.format(self.length_mm)
            g_str = "'{:.3f}'.format(s.gauge_mm).rjust(col_width)"
            t_str = "'{:.1f} kg'.format(s.kg).rjust(col_width)"
            tot_str = '{:.1f} kg'.format(self.set_kg).rjust(col_width)
        else:
            l_str = 'Scale length: {}in '.format(self.length)
            g_str = "'{:.3f}'.format(s.gauge).rjust(col_width)"
            t_str = "'{:.1f} lb'.format(s.lb).rjust(col_width)"
            tot_str = '{:.1f} lb'.format(self.set_lb).rjust(col_width)

        if title is None:
            print('=' * table_width)
        elif len(title) > table_width:
            print(title[:table_width])
        else:
            print(' {} '.format(title).center(table_width, '='))
        print(l_str)
        print('-' * table_width)
        print(''.join([col.rjust(col_width) for col in cols]))
        print('-' * table_width)
        for s in self.strings:
            print(eval(g_str), eval(m_str), eval(p_str), eval(t_str), sep='')
        print('-' * table_width)
        print(('Total:'.rjust(col_width) + tot_str).rjust(table_width), sep='')
        print(('=' * (col_width + len('Total:'))).rjust(table_width))
        print('')


class SetFileParser:
    """Parse a formatted set file for arguments passable to StringSet().

    A set file has the following format, where properties are as
    described in the Attributes section below.
        length = LENGTH
        GAUGE MATERIAL PITCH
        [GAUGE MATERIAL PITCH]
        [...]
        [si = True or False]

    An example SETFILE for a common set of light gauge ("10's")
    electric guitar strings on a Fender-scale instrument, with nickel
    plated steel wound strings, would look like this:
        length = 25.5
        10 ps e6
        13 ps b3s
        17 ps g3
        26 nps d3
        36 nps a2
        46 nps e2

    The "length = ..." line and at least one "GAUGE MATERIAL PITCH"
    line are required.

    "si = False" is not required, and the SetFileParser.si attribute
    defaults to False if no "si = ..." line is included.

    Attributes:
        length (float): Instrument scale length in inches, 1/1000in,
            or mm with si=True.
        gauges (list[float]): List of string gauges in inches,
            1/1000in, or mm with si=True.
        materials (list[str]): List of valid string material codes.
        pitches (list[str]): List of pitches in scientific pitch
            notation, from A0-E5.
        si (bool, optional): Supply length and gauges in mm.
            Defaults to False.
        lines (list[str]): List of lines in input file.

    Args:
        file (path-like): Path to a properly formatted set file.

    Raises:
        KeyError: On invalid material codes or pitches.
        ValueError: On missing length or string properties
    """

    def __init__(self, file):
        """Class constructor."""
        self.length = None
        self.gauges = []
        self.materials = []
        self.pitches = []
        self.si = False

        with open(file, 'r') as f:
            self.lines = [ln.replace('\n', '') for ln in f.readlines()]

        l_re = re.compile(r'length\s*=\s*(\d+\.*\d*)')
        s_re = re.compile(r'(\d*\.\d+|\d+\.*\d*)\s*(\w+)\s*([a-gA-G][b#]?\d+)')
        si_re = re.compile(r'si\s*=\s*(True|true|1|False|false|0)')

        for line in self.lines:
            l_match = l_re.match(line)
            if l_match is not None:
                self.length = float(l_match.groups()[0])

            s_match = s_re.match(line)
            if s_match is not None:
                gauge, material, pitch = s_match.groups()

                self.gauges.append(float(gauge))

                try:
                    assert material in material_codes.keys()
                except Exception:
                    raise KeyError(_err_msg['mat'])
                finally:
                    self.materials.append(material)

                pitch = pitch[0].upper() + pitch[1:]
                try:
                    assert pitch in frequency_chart.keys()
                except Exception:
                    raise KeyError(_err_msg['pitch'])
                finally:
                    self.pitches.append(pitch)

            si_match = si_re.match(line)
            if si_match is not None:
                if si_match.groups()[0] in ('True', 'true', '1'):
                    self.si = True  # already False, so no "else:"

        if self.length is None:
            msg = 'File must include "length = (number)"'
            raise ValueError(msg)

        if (len(self.gauges) == 0
                or len(self.materials) == 0
                or len(self.pitches) == 0):
            msg = 'File must include at least one GAUGE MATERIAL PITCH line'
            raise ValueError(msg)

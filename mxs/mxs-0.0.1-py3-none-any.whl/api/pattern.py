"""
MXS is the Math eXploration Solver.
Copyright (C) 2022  Brian Farrell

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Contact: brian.farrell@me.com
"""


def get_pv_params():
    pattern = input("What is the pattern?  ")
    char_per_line = input("How many characters on a line?  ")
    target_line = input("What line number are you interested in?  ")
    target_char = input(f"What character on line {target_line} are you interested in?  ")

    return pattern, char_per_line, target_line, target_char


def reveal_position_value(pattern, char_per_line, target_line, target_char):
    char_per_line = int(char_per_line)
    target_line = int(target_line)
    target_char = int(target_char)

    target_char_delta = char_per_line - target_char
    target_position = (target_line * char_per_line) - target_char_delta

    remainder = target_position % len(pattern)
    value = pattern[remainder - 1]

    return target_position, value

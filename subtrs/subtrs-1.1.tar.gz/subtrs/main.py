#!/usr/bin/python3
# -*- coding: utf-8 -*-

# main.py file is part of subtrs.

# Copyright 2022 Dimitris Zlatanidis <d.zlatanidis@gmail.com>
# All rights reserved.

# subtrs is a simple tool that translates video subtitles

# https://gitlab.com/dslackw/subtrs

# subtrs is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.


import sys
import os.path
from colored import fore, style
from googletrans import Translator


TOOL = 'subtrs'
VERSION = 1.1


class Subtitles:
    '''A simple tool that tranlates video subtitles'''

    def __init__(self, args, flags):
        '''Initialization'''
        self.flags = flags
        self.file = args[0]
        self.dest = args[1]
        self.ext = self.file[-4:]
        self.f = ''
        self.color()
        self.translator = Translator()

    def color(self):
        '''Checking color flag'''
        if "--color" in self.flags:
            self.TRS_COLOR = fore.LIGHT_YELLOW
            self.OUT_COLOR = fore.LIGHT_GREEN
            self.IN_COLOR = fore.LIGHT_RED
            self.RESET_COLOR = style.RESET
        else:
            self.TRS_COLOR = ''
            self.OUT_COLOR = ''
            self.IN_COLOR = ''
            self.RESET_COLOR = ''

    def read_subs(self):
        '''Read the subtitle file'''
        try:
            with open(self.file, 'r', encoding='utf-8') as subs:
                self.f = subs.readlines()
        except IOError:
            print(f'The file "{self.file}" does not exist')
            raise SystemExit(1)

    def write_new_subs(self):
        '''Write the new subtitle file'''
        self.Exceptions_dest_lang()
        self.read_subs()
        cap_file = self.file.split('/')[-1]
        new_captions = f'{cap_file[:-4]}_{self.dest}{self.ext}'
        with open(new_captions, 'w') as new_subs:
            for line in self.f:
                if line and not line[0].isdigit():
                    if len(line) > 1 and '--silent' not in self.flags:
                        print(f'{self.IN_COLOR}<<{self.RESET_COLOR} {line}')
                    line = self.translate(line)
                    if len(line) > 1 and '--silent' not in self.flags:
                        print(f'{self.OUT_COLOR}>> '
                              f'{self.TRS_COLOR}{line}{self.RESET_COLOR}')
                new_subs.write(line)
        self.created_file(new_captions)

    def translate(self, line):
        '''Translate line per line'''
        return self.translator.translate(line, dest=self.dest).text + '\n'

    def created_file(self, file):
        '''Message when the file finished'''
        if self.file_exist(file):
            print(f'The file "{file}" created.')
        else:
            print(f'The file "{file}" does not exist.')

    def file_exist(self, file):
        '''Check if the file exists'''
        return os.path.exists(file)

    def Exceptions_dest_lang(self):
        '''Check for destination language'''
        try:
            self.translator.translate('Video', dest=self.dest).text
        except ValueError as Err:
            print(f'Error: {Err} "{self.dest}"')
            raise SystemExit(1)


def usage(status):
    '''CLI help menu'''
    args = ['Usage: subtrs [subtitles_file] [destination lang]',
            ' ',
            '       Simple tool that trlanslates video subtitles',
            ' ',
            '       Support subtitles files [*.sbv, *.vtt, *.srt]',
            '       Destination language [en, de, ru] etc.',
            ' ',
            '       --color    Show translate text language with colour.',
            '       --silent   Silent method, without viewing.',
            '       --version  Show the version and exit.',
            '       --help     Show this message and exit.',
            ]
    for opt in args:
        print(opt)
    raise SystemExit(status)


def args_flags(args):
    '''Manage flags'''
    flags = []
    if '--color' in args:
        args.remove('--color')
        flags.append("--color")
    if '--silent' in args:
        args.remove('--silent')
        flags.append('--silent')
    return flags


def check_usage(args):
    '''Checking usage'''
    file_ext = ['.sbv', '.vtt', '.srt']
    if args == []:
        usage(status=0)
    # Show the version and exit
    if args[0] == '--version':
        print(f'{TOOL} version {VERSION}')
        raise SystemExit(0)
    # Show help menu and exit
    if args[0] == '--help':
        usage(status=0)
    # Check for subtitle extention file
    if args[0][-4:] not in file_ext:
        usage(status=1)
    # Check for max options
    if len(args) < 2 or len(args) > 2:
        usage(status=1)


def main():
    args = sys.argv
    args.pop(0)
    flags = args_flags(args)
    check_usage(args)
    subs = Subtitles(args, flags)
    subs.write_new_subs()

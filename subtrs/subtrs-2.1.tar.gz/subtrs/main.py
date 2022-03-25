#!/usr/bin/python3
# -*- coding: utf-8 -*-


import sys
import os.path
import googletrans
from progress.bar import Bar
from subtrs.cli import usage
from colored import fore, style
from googletrans import Translator
from subtrs.__metadata__ import __prog__, __version__


class Subtitles:
    '''A simple tool that tranlates video subtitles'''

    def __init__(self, args, flags):
        '''Initialization'''
        self.flags = flags
        self.file = args[0]
        self.dest = args[1].split(',')
        self.suffix = self.file[-4:]
        self.subs_file = ''
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
                self.subs_file = subs.readlines()
        except IOError:
            print(f'The file "{self.file}" does not exist')
            sys.exit(1)

    def write_new_subs(self):
        '''Write the new subtitle file'''
        for index, lang in enumerate(self.dest, 1):
            self.Exceptions_dest_lang(lang)
            self.read_subs()
            cap_file = self.file.split('/')[-1]
            new_captions = f'{cap_file[:-4]}_{lang}{self.suffix}'
            if '--progress' not in self.flags:
                print(self.trs_jobs(index, lang), end='\n\n')
            with open(new_captions, 'w') as new_subs:
                bar = Bar(f'{self.trs_jobs(index, lang)}',
                          max=len(self.subs_file),
                          suffix='%(percent)d%% - %(eta)ds')
                for line in self.subs_file:
                    if line and not line[0].isdigit():
                        if len(line) > 1 and '--progress' not in self.flags:
                            self.print_line_in(line)
                        line = self.translate(line, lang)
                        if len(line) > 1 and '--progress' not in self.flags:
                            self.print_line_out(line, lang)
                    new_subs.write(line)
                    if '--progress' in self.flags:
                        bar.next()
                bar.finish()
            self.created_file(new_captions)

    def trs_jobs(self, index, lang):
        '''View the job title'''
        return (f'[{index}/{len(self.dest)}] '
                f'Translate into {googletrans.LANGUAGES.get(lang)}')

    def print_line_in(self, line):
        '''Print line before translated'''
        print(f'[{self.detect_lang(line)}]{self.IN_COLOR}'
              f' <<{self.RESET_COLOR} {line}')

    def print_line_out(self, line, lang):
        '''Print line after traslate'''
        print(f'[{lang}]{self.OUT_COLOR} >> '
              f'{self.TRS_COLOR}{line}{self.RESET_COLOR}')

    def translate(self, line, lang):
        '''Translate line per line'''
        return self.translator.translate(line, dest=lang).text + '\n'

    def detect_lang(self, line):
        '''Identifies the language used'''
        return self.translator.detect(line).lang

    def created_file(self, file):
        '''Message when the file finished'''
        if self.file_exist(file):
            print(f"Subtitle file '{file}' created.")
        else:
            print(f"Subtitle file '{file}' does not exist.")

    def file_exist(self, file):
        '''Check if the file exists'''
        return os.path.exists(file)

    def Exceptions_dest_lang(self, lang):
        '''Check for destination language'''
        try:
            self.translator.translate('Video', dest=lang).text
        except ValueError as Err:
            print(f"Error: {Err} '{lang}'")
            sys.exit(1)


def args_flags(args):
    '''Manage flags'''
    flags = []
    if '--color' in args:
        args.remove('--color')
        flags.append('--color')
    if '--progress' in args:
        args.remove('--progress')
        flags.append('--progress')
    if len(flags) >= 2:
        usage(1)
    return flags


def check_usage(args):
    '''Checking usage'''
    file_ext = ['.sbv', '.vtt', '.srt']

    if args == []:
        usage(status=1)

    # Show the version and exit
    if args[0] == '--version' or args[0] == '-v' and len(args) == 1:
        print(f'{__prog__} version {__version__}')
        sys.exit(0)

    # Show help menu and exit
    if args[0] == '--help' or args[0] == '-h' and len(args) == 1:
        usage(status=0)

    # Show all suported languages
    if args[0] == '--languages' or args[0] == '-l' and len(args) == 1:
        for key, value in googletrans.LANGUAGES.items():
            print(key, value)
        sys.exit(0)

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

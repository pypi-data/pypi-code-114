#!/usr/bin/env python
# encoding: utf-8
'''
ctail -- colored tail

ctail is a simple 'tail -f' alternative which colors given regular expressions matches


@author:     Otger Ballester
            
@license:    MIT License

@contact:    otger.ballester@gmail.com
@deffield    updated: Updated
'''

import sys
import os
import time
import re

from ctail.colors import colours, colour_list, colour_close

__version__ = '0.0.2'
__date__ = '2013-09-25'
__updated__ = '2022-03-25'

DEBUG = True
TESTRUN = 0
PROFILE = 0
BLOCKSIZE = 175
PROG_NAME = 'ctail'
DT_REGEX = r'\d{4}[-.]?\d{2}[-.]?\d{2} \d{2}:\d{2}:\d{2}(?:,\d{3})?'

class CLIError(Exception):
    '''Generic exception to raise and log different fatal errors.'''



def regexes_coloring(what, regexes, regexes_colors):
    for regex in regexes:
        what = re.sub(regex, '{c}\g<0>{cc}'.format(c=regexes_colors[regex], cc=colour_close), what)
    return what

def seek_last_n_lines_position(fp, nlines=10):
    '''
    Return fp positioned at start of last nlines
    Inspired in code found at:  http://stackoverflow.com/questions/136168/get-last-n-lines-of-a-file-with-python-similar-to-tail
    '''
    import os
    fp.seek(0, os.SEEK_END)
    # We look for n+1 '\n' symbols and then go forward len('\n'), so we show last n lines
    missing_lines = nlines + 1

    curr_block_start = fp.tell()
    block_num = 1
    stop_iter = False
    # print(f'End of file: {curr_block_start}')
    while 1:
        curr_block_end = curr_block_start
        # calculate new block end and block size
        if curr_block_end > BLOCKSIZE:
            # We still can go one block back
            curr_block_start = curr_block_end - BLOCKSIZE
        else:
            # Not enough space to go back one full block, so we go to start of the file
            curr_block_start = 0            
            stop_iter = True
        # print(f'Block {block_num:03}: {curr_block_start} + {curr_block_end - curr_block_start}')
        fp.seek(curr_block_start, os.SEEK_SET)
        data = fp.read(curr_block_end - curr_block_start)
        data2 = fp.read(curr_block_end - curr_block_start).replace('\n',colours['BRed']+'!'+colour_close)
        # print(f'data: {data2}')

        lines_in_data = data.count('\n')
        # print(f"Block {block_num:03} found {lines_in_data} '\\n'")
        if lines_in_data >= missing_lines:
            # we have found all missing lines
            buffer_last_found = curr_block_end - curr_block_start + 1
            founds = []
            for _ in range(missing_lines):
                buffer_last_found = data.rfind('\n', 0, buffer_last_found)
                founds.append(buffer_last_found)
            # print(f"buffer found '\\n' positions: {founds}")
            # I compensate because every '\n' on file seems to occupy 2 bytes instead of 1
            # It seems like a very bad idea as it will fail when we have other formats probably
            fp.seek(curr_block_start + buffer_last_found + missing_lines + 1, os.SEEK_SET)
            return fp
        elif stop_iter:
            # file does not contain requested lines, go to start of file
            fp.seek(0,0)
            return fp
        # Still have not found all lines or start of file, iterate
        missing_lines -= lines_in_data
        block_num += 1
    
def main():
    try:    
        import argparse

        parser = argparse.ArgumentParser(
            prog=PROG_NAME,
            formatter_class=argparse.ArgumentDefaultsHelpFormatter)
        parser.add_argument('file_path', help='path of the file')
        parser.add_argument('reg_exes', help='regular expressions to colour on the file', nargs='*')
        
        parser.add_argument('-d', action='store_true', dest='colour_dt', help='color date times in format: yyyy-mm-dd HH:MM:SS')
        parser.add_argument('-l', default=10, dest="nlines", type=int, help="how many last lines show from file")
        parser.add_argument('-f', '--follow', action='store_true', help='output appended data as the file grows')
        args = parser.parse_args()

        file_path = os.path.abspath(os.path.expanduser(args.file_path))

        if not os.path.exists(file_path):
            raise CLIError('File ({0}) does not exist'.format(file_path))
        
        regexes = args.reg_exes
        if args.colour_dt:
            regexes.append(DT_REGEX)

        color_mod = len(colour_list)
        color_regexes = dict((regex, colours[colour_list[ix%color_mod]]) for ix, regex in enumerate(regexes))

        print('-----------------------------------------------------------------')
        print("Applied regexes:")
        for r in regexes:
            print(f"\t {color_regexes[r]}{r}{colour_close}")
        print('-----------------------------------------------------------------')
        fp = open(file_path, 'r')
        fp = seek_last_n_lines_position(fp, args.nlines)
        while True:
            new = fp.readlines()
            if new:
                if regexes:
                    for n in new:
                        sys.stdout.write(regexes_coloring(n, regexes, color_regexes))
                else:
                    for n in new:
                        sys.stdout.write(n)
            else:
                if args.follow is False:
                    break
                time.sleep(0.05)


    except KeyboardInterrupt:
        ##Clean exit when pressing Ctrl + c
        sys.stdout.write('\n')
        return 0
    except Exception as e:
        import traceback
        indent = len(parser.prog) * " "
        sys.stderr.write(parser.prog + ": " + repr(e) + "\n")
        sys.stderr.write(indent + "  for help use --help\n")
        if DEBUG:
            print("\nTraceback:")
            traceback.print_exc()
        return 2

from .utils import *

import sys
import argparse



if __name__ == '__main__':
    
    description =   ''' 
                    Python utility for removing all subdirectories of a directory while
                    preserving all the files located in the subdirectories. The files are
                    renamed according to the relative path from the root_dir to given file.
                    The '\' and '/' in the relative path are replaced by the separator char.
                    '''            
    parser = argparse.ArgumentParser(description=description)
    
    help_string = 'Path to root directory.'
    parser.add_argument('-r', '--root', help=help_string, required=True)
    help_string = 'Separator that is placed into the new file names instead of \'\\\' and \'/\'. Default is \'_\'.'
    parser.add_argument('-s', '--sep', help=help_string, default='_')
    
    args = parser.parse_args()

    if args.root is not None:
        remove(args.root, args.sep)
    
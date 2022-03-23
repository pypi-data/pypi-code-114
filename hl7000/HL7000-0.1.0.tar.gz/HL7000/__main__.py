import sys
import optparse

from .HL7000 import load_folder


def parse_options(args=None, values=None):
    """
    Define and parse `optparse` options for command-line usage.
    """
    usage = """%prog [SOURCE_FOLDER] ["TARGET_FOLDER"]]]"""
    desc = "Load a folder to a target location"

    parser = optparse.OptionParser(usage=usage, description=desc)

    (options, args) = parser.parse_args(args, values)

    if len(args) != 2:
        raise Exception("Input and Output folders required")
    else:
        input_folder = args[0]
        output_folder = args[1]

    return (input_folder, output_folder)

def run():
    options = parse_options()

    # Run
    load_folder(options[0], options[1])
    
if __name__ == '__main__':
    run()
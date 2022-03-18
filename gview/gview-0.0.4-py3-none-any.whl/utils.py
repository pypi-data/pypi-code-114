'''
util functions
'''

import argparse

def argParser():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    run_parser = subparsers.add_parser("run")

    return parser
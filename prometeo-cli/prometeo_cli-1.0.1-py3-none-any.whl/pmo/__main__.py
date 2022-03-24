"""
Entry point script.
"""
# prometeo/__main__.py
import os

from pmo import prometeo, __app_name__
from helpers import Profiler

def check_env_vars():
    env = os.environ.get('PROMETEO_ENVIRONMENT')
    if env == None:
        raise Exception('Please set a working environment')


def main():
    profiler = Profiler()
    profiler.initialize()
    check_env_vars()
    prometeo.app(prog_name=__app_name__)

if __name__ == "__main__":
    main()


'''
run script to start server and celery task queue
'''

from utils import argParser
from G_VAR import R_PATH
import os
import subprocess

def run():
    parser = argParser()
    args = parser.parse_args()

    if args.action == 'run':
        script = os.path.join(R_PATH,'run.sh')
        subprocess.call(script,shell=True)

if __name__ == '__main__':
    run()
# File: autonml_api.py 
# Author(s): Vedant Sanil
# Created: Wed Feb 17 11:49:20 EST 2022 
# Description:
# Acknowledgements:
# Copyright (c) 2022 Carnegie Mellon University
# This code is subject to the license terms contained in the code repo.

import os
import shutil
import subprocess

class AutonML(object):
    def __init__(self, input_dir, output_dir, timeout=2, numcpus=8):
        self.input_dir = os.path.abspath(input_dir)
        self.output_dir = os.path.abspath(output_dir)
        self.timeout = str(timeout)
        self.numcpus = str(numcpus)
        self.problemPath = os.path.join(self.input_dir, 'TRAIN', 'problem_TRAIN', 'problemDoc.json')

    def run(self):
        proc = subprocess.Popen(['autonml_main', self.input_dir, 
                                self.output_dir, self.timeout, self.numcpus,
                                self.problemPath], stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)

        output, error = proc.communicate()
        if proc.returncode != 0:
            print(output)
            raise RuntimeError(error.decode())

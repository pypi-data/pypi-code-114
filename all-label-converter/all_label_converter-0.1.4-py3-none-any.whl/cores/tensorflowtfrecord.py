"""
Author: Fatih Baday <bfatih27@gmail.com>
Purpose: To import and export tensorflow csv type.
"""
# Importing libraries.
import os
import shutil
import logging
import pandas as pd
import all_label_converter.commonformat as cf
import all_label_converter.cores.utils as utils

from all_label_converter.cores.config import Config


class TFRecordExport:
    def __init__(self, objs, folder_path: str):
        self.objs = objs
        self.folder_path = folder_path
        self.start()

    def start(self):



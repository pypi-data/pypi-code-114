#!/usr/bin/env python
# -*- coding: utf-8; buffer-read-only: t -*-

__author__ = "Gregorio Ambrosio"
__contact__ = "gambrosio[at]malaga.eu"
__copyright__ = "Copyright 2022, Gregorio Ambrosio"
__date__ = "2022/03/21"
__license__ = "MIT"

import sqlite3
import os
import numpy as np
import pandas as pd
from robotathome.log import logger

__all__ = ['INE']

# @logger.catch
class INE():
    """INE class with methods for CEMI Data Science Toolbox

    The INE class encapsulates methods to manage INE data

    Attributes:
        rh_path (str, optional):
            root path for robotathome database, usually rh.db
        wspc_path (str, optional):
            workspace path where temporary files are stored
        db_filename (str, optional):
            default database name
        rgbd_path (str, optional):
           path that completes rh_path, where rgbd files are stored
        scene_path (str, optional):
           path that completes rh_path, where scene files are stored
    """

    def __init__(self
                 ):
        """ INE constructor method """
        pass

    def __del__(self):
        """ INE destructor method"""
        pass



    """
    Framework
    """

    """
    Stuff
    """

    """
    Lab
    """

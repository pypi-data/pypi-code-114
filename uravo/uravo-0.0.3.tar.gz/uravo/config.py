#!/usr/bin/env python3

import configparser
import os

config = configparser.ConfigParser()
if (os.path.exists("/etc/uravo.conf")):
    config.read("/etc/uravo.conf")


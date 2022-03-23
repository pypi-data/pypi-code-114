#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Create data apps

.. currentmodule:: databutton
.. moduleauthor:: Databutton <support@databutton.com>
"""

from .version import __version__, __release__  # noqa
from .decorators.streamlit import streamlit, _streamlit_apps  # making them a first level citizen, might not be what we want?

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author:    thepoy
# @Email:     thepoy@163.com
# @File Name: __init__.py
# @Created:   2021-05-27 09:34:57
# @Modified:  2022-03-25 11:01:12

from colort.colort import DisplayStyle

__version__ = "0.7"

display_style = DisplayStyle()

__all__ = [
    "DisplayStyle",
    "display_style",
]

#! /usr/bin/env python
# Copyright 2020 Uwe Schmitt <uwe.schmitt@id.ethz.ch>

import os
import sys

import spyder_kernels.console.kernel as kernel
import spyder_kernels.utils.nsview as nsview

import emzed


def set_cwd(self, dirname):
    if sys.platform == "win32":
        dirname = dirname.replace("\\\\", "\\")
    os.chdir(dirname)


kernel.SpyderKernel.set_cwd = set_cwd


def get_size(item, _orig=nsview.get_size):
    if isinstance(item, emzed.Table):
        return "{} row x {} columns".format(len(item), len(item.col_names))
    return _orig(item)


nsview.get_size = get_size


def is_supported(
    value, check_all=False, filters=None, iterate=False, _orig=nsview.is_supported
):
    return isinstance(value, (emzed.Table, emzed.PeakMap)) or (
        _orig(value, check_all, filters, iterate)
    )


nsview.is_supported = is_supported


def get_type_string(item, _orig=nsview.get_type_string):
    if isinstance(item, emzed.Table):
        return "Table"
    if isinstance(item, emzed.PeakMap):
        return "PeakMap"
    return _orig(item)


nsview.get_type_string = get_type_string


def value_to_display(value, minmax=False, level=0, _orig=nsview.value_to_display):
    if isinstance(value, emzed.Table):
        return ", ".join(value.col_names)
    return _orig(value, minmax, level)


nsview.value_to_display = value_to_display


if __name__ == "__main__":
    from spyder_kernels.console import start

    start.main()

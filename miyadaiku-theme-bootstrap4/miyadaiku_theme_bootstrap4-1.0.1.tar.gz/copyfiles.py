#!/usr/bin/env python3

import pathlib
from miyadaiku import setuputils

DIR = pathlib.Path(__file__).resolve().parent

srcdir = DIR / 'node_modules/bootstrap/dist'
destdir = DIR / 'miyadaiku_theme_bootstrap4/externals'
copy_files = [
    [srcdir/ 'css/', ['bootstrap.css', 'bootstrap.min.css', ], destdir / 'css/'],
    [srcdir / 'js/', ['bootstrap.css', '*.js', ], destdir / 'js/']
]

setuputils.copyfiles(copy_files)

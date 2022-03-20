#!/usr/bin/env python

"""Tests for `siphon` package."""

import re
from siphon import __version__


def test_valid_version():
    assert re.search(r'(\d+.\d+.\d+)$', __version__) is not None

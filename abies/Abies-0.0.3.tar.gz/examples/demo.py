#!/usr/bin/env python3
"""Some Documentation"""

from pathlib import Path

# import sys
import os

# import framework
# import dff
# import vdff

from abies.framework import Framework
from abies import library


if __name__ == "__main__":

    os.environ["SYSTEMC_DISABLE_COPYRIGHT_MESSAGE"] = "1"

    log_dir = Path("logs")
    f = Framework(log_dir)
    f.log_level = "debug"

    library.dff.register_with(f, "vdff")

    netlist = [
        ("vdff", "dff1"),
        ("vdff", "dff2"),
    ]

    f.trace = True

    f.initialize(netlist)
    f.run(100)

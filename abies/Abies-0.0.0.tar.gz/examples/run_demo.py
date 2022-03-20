#!/usr/bin/env python3

import subprocess
import sys
from pathlib import Path

demo_location = Path(__file__).parent / "demo.py"

demo_cmd = [demo_location]

if __name__ == "__main__":
    demo_cmd.extend(sys.argv[1:])

    subprocess.run(demo_cmd, check=True)

    demo_cmd.append("SKIPINITANDJUSTRUN")
    subprocess.run(demo_cmd)

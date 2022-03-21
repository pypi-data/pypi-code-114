"""Launch the actual Rust binary."""

from importlib.metadata import files
import sys
from subprocess import run


def main():
    args = sys.argv[1:]
    # Find the executable in the installed package:
    for f in files("sciagraph-report"):
        if f.name.lower() in ("sciagraph-report", "sciagraph-report.exe"):
            path = f.locate()
            break
    result = run([path] + args)
    sys.exit(result.returncode)


if __name__ == "__main__":
    main()

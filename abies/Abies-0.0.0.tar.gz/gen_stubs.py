#!/usr/bin/env python3
""" Some Docstring """

import subprocess

stubgen_cmd = [
    "pybind11-stubgen",
    "--output-dir",
    "src",
    "--no-setup-py",
    # "--skip-signature-downgrade",
    # "--ignore-invalid",
    # "signature",
    "--root-module-suffix",
    "",
]

if __name__ == "__main__":
    # pkg_name = sys.argv[1]
    pkg_names = [
        "abies.framework._framework",
        "abies.library.dff._dff",
        "abies.library.vdff._vdff",
    ]

    stubgen_cmd.extend(pkg_names)

    # for pkg_name in pkg_names:
    subprocess.run(stubgen_cmd, check=True)

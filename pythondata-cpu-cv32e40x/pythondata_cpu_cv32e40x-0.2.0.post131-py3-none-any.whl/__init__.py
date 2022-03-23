import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post131"
version_tuple = (0, 2, 0, 131)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post131")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post5"
data_version_tuple = (0, 2, 0, 5)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post5")
except ImportError:
    pass
data_git_hash = "37000963f8b4983ad2e35bfe3cc4d3e72977dd97"
data_git_describe = "0.2.0-5-g3700096"
data_git_msg = """\
commit 37000963f8b4983ad2e35bfe3cc4d3e72977dd97
Merge: 96f09e5 4cdfb99
Author: silabs-oysteink <66771756+silabs-oysteink@users.noreply.github.com>
Date:   Wed Mar 23 10:33:12 2022 +0100

    Merge pull request #481 from Silabs-ArjanB/ArjanB_mpie
    
    Fixed mpie R/W attribute

"""

# Tool version info
tool_version_str = "0.0.post126"
tool_version_tuple = (0, 0, 126)
try:
    from packaging.version import Version as V
    ptool_version = V("0.0.post126")
except ImportError:
    pass


def data_file(f):
    """Get absolute path for file inside pythondata_cpu_cv32e40x."""
    fn = os.path.join(data_location, f)
    fn = os.path.abspath(fn)
    if not os.path.exists(fn):
        raise IOError("File {f} doesn't exist in pythondata_cpu_cv32e40x".format(f))
    return fn

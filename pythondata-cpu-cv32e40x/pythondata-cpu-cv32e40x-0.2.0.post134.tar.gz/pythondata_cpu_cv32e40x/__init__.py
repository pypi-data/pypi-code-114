import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post134"
version_tuple = (0, 2, 0, 134)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post134")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post8"
data_version_tuple = (0, 2, 0, 8)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post8")
except ImportError:
    pass
data_git_hash = "8738b718649a0535a83f59d6b72523282a6fb4a6"
data_git_describe = "0.2.0-8-g8738b71"
data_git_msg = """\
commit 8738b718649a0535a83f59d6b72523282a6fb4a6
Merge: 3700096 9d14b87
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Mar 23 15:01:09 2022 +0100

    Merge pull request #482 from silabs-halfdan/doc_rvfi_sleep_signals
    
    Added sleep signals to rvfi documentation

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

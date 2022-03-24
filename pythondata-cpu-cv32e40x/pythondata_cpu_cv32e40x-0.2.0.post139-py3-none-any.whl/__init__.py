import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post139"
version_tuple = (0, 2, 0, 139)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post139")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post13"
data_version_tuple = (0, 2, 0, 13)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post13")
except ImportError:
    pass
data_git_hash = "243bb9cde7a2815effeb3a7aa3991fe3b7fd8a63"
data_git_describe = "0.2.0-13-g243bb9c"
data_git_msg = """\
commit 243bb9cde7a2815effeb3a7aa3991fe3b7fd8a63
Merge: 8738b71 2e66627
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Mar 24 09:28:00 2022 +0100

    Merge pull request #485 from silabs-oysteink/silabs-oysteink_clic-1
    
    CLIC: Spec chapter 5.1

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

import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post142"
version_tuple = (0, 2, 0, 142)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post142")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post16"
data_version_tuple = (0, 2, 0, 16)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post16")
except ImportError:
    pass
data_git_hash = "d74b7324dc22383679e16275e143a1f3ec551bec"
data_git_describe = "0.2.0-16-gd74b732"
data_git_msg = """\
commit d74b7324dc22383679e16275e143a1f3ec551bec
Merge: 243bb9c aca5b42
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Thu Mar 24 14:24:30 2022 +0100

    Merge pull request #486 from silabs-oysteink/silabs-oysteink_clic-2
    
    CLIC: Spec chapter 5.3

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

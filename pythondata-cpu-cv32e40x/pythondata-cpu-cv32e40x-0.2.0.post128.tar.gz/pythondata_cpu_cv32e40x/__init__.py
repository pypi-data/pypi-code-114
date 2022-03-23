import os.path
__dir__ = os.path.split(os.path.abspath(os.path.realpath(__file__)))[0]
data_location = os.path.join(__dir__, "system_verilog")
src = "https://github.com/openhwgroup/cv32e40x"

# Module version
version_str = "0.2.0.post128"
version_tuple = (0, 2, 0, 128)
try:
    from packaging.version import Version as V
    pversion = V("0.2.0.post128")
except ImportError:
    pass

# Data version info
data_version_str = "0.2.0.post2"
data_version_tuple = (0, 2, 0, 2)
try:
    from packaging.version import Version as V
    pdata_version = V("0.2.0.post2")
except ImportError:
    pass
data_git_hash = "96f09e52e955aedf1e10df2ed6163bc09182f150"
data_git_describe = "0.2.0-2-g96f09e5"
data_git_msg = """\
commit 96f09e52e955aedf1e10df2ed6163bc09182f150
Merge: 902ea67 e0365b1
Author: Arjan Bink <40633348+Silabs-ArjanB@users.noreply.github.com>
Date:   Wed Mar 23 09:56:14 2022 +0100

    Merge pull request #480 from silabs-oysteink/silabs-oysteink_csr-types
    
    Updated typedefs for CSR registers to match new fields in the user manual

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

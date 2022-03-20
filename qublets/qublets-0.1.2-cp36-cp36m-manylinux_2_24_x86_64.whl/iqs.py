""" Internal IQS wrapper """

from os import path
import sys

# pylint: disable-next=wrong-import-position
repo_root = path.dirname(path.dirname(path.abspath(__file__)))
lib_path = path.join(repo_root, "intel-qs", "build", "lib")
sys.path.insert(0, lib_path)
import intelqs_py as _iqs


def cpp_method(*args, **kwargs):
  raise Exception("Method only exists in C++. See qublets/iqs.py to enable")


# List of methods in C++ that are not exposed to Python.
# If you'd like to use any, add the given config line to
# intel-qs/pybind11/intelqs_py.cpp locally and rebuild.
# TODO(dyordan1): Push this upstream into intel-qs

# In py::class_< QubitRegister<ComplexDP> >:
# .def("GetGlobalAmplitude", &QubitRegister<ComplexDP>::GetGlobalAmplitude)
if 'GetGlobalAmplitude' not in dir(_iqs.QubitRegister):
  _iqs.QubitRegister.GetGlobalAmplitude = cpp_method

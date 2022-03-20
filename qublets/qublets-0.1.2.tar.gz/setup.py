""" Pip package setup """

import glob
from os import path, makedirs, environ
import pybind11
from shutil import copytree, rmtree
import subprocess
import sys

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext


class CMakeExtension(Extension):

  def __init__(self, name, sources):
    Extension.__init__(self, name, sources=sources)


class CMakeBuild(build_ext):

  def build_extension(self, ext):
    extdir = path.abspath(path.dirname(self.get_ext_fullpath(ext.name)))
    extdir = path.join(extdir, "intel-qs", "build", "lib")

    if not path.exists(self.build_temp):
      makedirs(self.build_temp)

    cmake_command = [
        "cmake", f"-DPYTHON_EXECUTABLE={sys.executable}", f"-DCMAKE_PREFIX_PATH={pybind11.get_cmake_dir()}",
        "-DIqsPython=ON", "-DIqsNative=ON", "../../intel-qs"
    ]
    print(cmake_command)
    env = environ.copy()
    env["CXX"] = "g++"
    subprocess.check_call(cmake_command, cwd=self.build_temp, env=env)
    subprocess.check_call(["make", "-j", "8"], cwd=self.build_temp, env=env)

    rmtree(extdir, ignore_errors=True)
    copytree(path.join(self.build_temp, "lib"), extdir)


cmake_dir = glob.glob(path.join("intel-qs", "cmake", "**"), recursive=True)
src_dir = glob.glob(path.join("intel-qs", "src", "**"), recursive=True)
inc_dir = glob.glob(path.join("intel-qs", "include", "**"), recursive=True)
pybind_dir = glob.glob(path.join("intel-qs", "pybind11", "**"), recursive=True)
tutorials_dir = glob.glob(path.join("intel-qs", "tutorials", "**"),
                          recursive=True)
benchmarks_dir = glob.glob(path.join("intel-qs", "benchmarks", "**"),
                           recursive=True)
other = [
    path.join("intel-qs", "CMakeLists.txt"),
    path.join("intel-qs", "LICENSE.md")
]
iqs_files = cmake_dir + src_dir + inc_dir + pybind_dir + tutorials_dir + benchmarks_dir + other

long_description = ""
with open('README.md') as f:
    long_description = f.read()

setup(name="qublets",
      version="0.1.2",
      description="A quantum computing library for the rest of us",
      author="Dobromir Yordanov",
      author_email="dobri.domain@gmail.com",
      long_description=long_description,
      long_description_content_type="text/markdown",
      license="",
      url="https://github.com/dyordan1/qublets",
      packages=["qublets"],
      ext_modules=[CMakeExtension("qublets", iqs_files)],
      cmdclass={"build_ext": CMakeBuild},
      python_requires=">=3.6",
      install_requires=["dataclasses"])

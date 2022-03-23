from setuptools import setup, find_packages
from pybind11.setup_helpers import Pybind11Extension, build_ext

__version__ = '0.1.3'


xylo_v1_mod = Pybind11Extension('xylosim.v1',
                    define_macros = [('VERSION', __version__)],
                    sources = ['src/v1/cpp/v1.cpp',
                               'src/v1/cpp/XyloIAFNeuron.cpp',
                               'src/v1/cpp/XyloLayer.cpp'])

xylo_v2_mod = Pybind11Extension('xylosim.v2',
                    define_macros = [('VERSION', __version__)],
                    sources = ['src/v2/cpp/v2.cpp',
                               'src/v2/cpp/XyloIAFNeuron.cpp',
                               'src/v2/cpp/XyloLayer.cpp'])

setup (name = 'xylosim',
       version = __version__,
       description = 'C++ based simulator for quantized spiking neural network accelarators.',
       author = 'Philipp Weidel',
       author_email = 'philipp.weidel@synsense.ai',
       url = '',
       long_description = '''
                          C++ based simulator for quantized spiking neural network accelarators such as the Xylo chip developed by Synsense.
                          ''',
       packages=['xylosim', 'xylosim.v1', 'xylosim.v2'],
       package_dir={'xylosim':'xylosim',
                    'xylosim.v1':'src/v1',
                    'xylosim.v2':'src/v2'},
       install_requires = ['pybind11'],
       ext_modules = [xylo_v1_mod, xylo_v2_mod],
       cmdclass={"build_ext": build_ext},
       )

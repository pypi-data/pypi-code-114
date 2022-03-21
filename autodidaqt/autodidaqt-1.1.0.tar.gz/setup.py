# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autodidaqt',
 'autodidaqt.examples',
 'autodidaqt.experiment',
 'autodidaqt.instrument',
 'autodidaqt.instrument.identify',
 'autodidaqt.panels',
 'autodidaqt.reactive_utils',
 'autodidaqt.remote',
 'autodidaqt.resources.templates.common.local',
 'autodidaqt.resources.templates.empty',
 'autodidaqt.runner',
 'autodidaqt.ui']

package_data = \
{'': ['*'],
 'autodidaqt': ['resources/*',
                'resources/fonts/*',
                'resources/img/*',
                'resources/templates/common/*']}

install_requires = \
['PyQt5>=5.13.0,<5.14.0',
 'Quamash>=0.6.1,<0.7.0',
 'appdirs>=1.4.4,<1.5.0',
 'asyncqt>=0.8.0,<0.9.0',
 'autodidaqt-common>=0.1.0,<0.2.0',
 'dask>=2021,<2022',
 'dataclasses_json>=0.5.0,<0.6.0',
 'fsspec>=2021,<2022',
 'instrumentkit>=0.5,<0.6',
 'loguru>=0.3.2,<0.4.0',
 'matplotlib>=3.1.1,<4.0.0',
 'numpy>=1.20,<2.0',
 'pandas>=1.2.4,<2.0.0',
 'partd>=1.2.0,<2.0.0',
 'pymeasure>=0.9.0,<0.10.0',
 'pynng>=0.7.1,<0.8.0',
 'pyqt-led>=0.0.6,<0.1.0',
 'pyqtgraph>=0.12.1,<0.13.0',
 'pyrsistent>=0.17.3,<0.18.0',
 'python-dotenv>=0.10.3,<0.11.0',
 'python-ivi>=0.14.9,<0.15.0',
 'pyvisa-sim>=0.4.0,<0.5.0',
 'pyvisa>=1.11.0,<2.0.0',
 'qtsass>=0.3.0,<0.4.0',
 'rx>=3.0.1,<4.0.0',
 'scipy>=1.7.0,<2.0.0',
 'slackclient>=2.1.0,<3.0.0',
 'toolz>=0.11.1,<0.12.0',
 'xarray>=0.18.2,<0.19.0',
 'zarr>=2.8.3,<3.0.0']

setup_kwargs = {
    'name': 'autodidaqt',
    'version': '1.1.0',
    'description': 'AutodiDAQt is a simple data acquisition framework. For science.',
    'long_description': '==========\nautodidaqt\n==========\n\n|test_status| |coverage| |docs_status| \n\n|example|\n\n.. |docs_status| image:: https://readthedocs.org/projects/autodidaqt/badge/?version=latest&style=flat\n   :target: https://autodidaqt.readthedocs.io/en/latest/\n.. |coverage| image:: https://codecov.io/gh/chstan/autodidaqt/branch/master/graph/badge.svg?token=8M5ON9HZL2\n   :target: https://codecov.io/gh/chstan/autodidaqt\n.. |example| image:: docs/source/_static/autodidaqt-example.gif\n.. |test_status| image:: https://github.com/chstan/autodidaqt/workflows/CI%20with%20pytest/badge.svg?branch=master\n   :target: https://github.com/chstan/autodidaqt/actions\n\n\nautodidaqt := DAQ + UI generation + Reactivity + Instruments\n\nYou should be spending your time designing and running experiments,\nnot your DAQ software.\n\nautodidaqt is a nuts and bolts included framework for scientific data acquisition (DAQ),\ndesigned for rapid prototyping and the challenging DAQ environment of angle resolved\nphotoemission spectroscopy. If you specify how to sequence motions and data collection,\nautodidaqt can manage the user interface, talking to and managing instruments,\nplotting interim data, data collation, and IO for you.\n\nautodidaqt also has logging and notification support built in and can let you know\nover email or Slack when your experiment finishes (successfully or not!).\n\nIf autodidaqt doesn\'t do exactly what you need, get in contact with us or\ncheck out the examples. There\'s a good chance that if it isn\'t built in,\nautodidaqt is flexible enough to support your use case.\n\n\nRequirements\n============\n\n* Python 3.7 over\n* NoArch\n\nFeatures\n========\n\nAutomated DAQ\n-------------\n\nautodidaqt wraps instruments and data sources in a uniform interface, if you specify how\nto sequence motion and acquisition, autodidaqt handles async collection, IO, and visualizing\nyour data as it is acquired.\n\nUI Generation\n-------------\n\nautodidaqt using PyQt and Qt5 to generate UIs for your experiments. It also\nprovides simple bindings (autodidaqt.ui) that make making managing the day to day\nof working on PyQt simpler, if you need to do UI scripting of your own.\n\nIt also ships with a window manager that you can register your windows against,\nmaking it seamless to add extra functionality to your experiments.\n\nThe autodidaqt UI bindings are wrapped to publish as RxPY observables, making it easier\nto integrate your PyQT UI into a coherent asynchronous application.\n\nInstallation\n============\n\n::\n\n  $ pip install autodidaqt\n\nInstallation from Source\n========================\n\n1. Clone this repository\n2. Install `make` if you are on a Windows system\n3. Install `poetry` (the alternative Python package manager)\n4. Run `make install` from the directory containing this README\n\nUsage\n=====\n\nFor usage examples, explore the scripts in the examples folder. You can run them with\n\n::\n\n  $ python -m autodidaqt.examples.[example_name]\n\n\nreplacing [example_name] with one of:\n\n1. minimal_app\n2. plot_data\n3. simple_actors\n4. ui_panels\n5. wrapping_instruments\n6. scanning_experiment\n7. scanning_experiment_revisited\n8. scanning_interlocks\n9. scanning_custom_plots\n10. scanning_setup_and_teardown\n11. scanning_properties_and_profiles\n12. manuscript_fig4\n\nYou can also get a list of all the available examples by running\n\n::\n\n  $ python -m autodidaqt.examples\n\n\nExamples for "remote control", including a "virtual nanoXPS lab" \nare available in integration_tests folder of AutodiDAQt receiver in \nits companion repository.\n',
    'author': 'chstan',
    'author_email': 'chstansbury@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/chstan/autodidaqt-common',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)

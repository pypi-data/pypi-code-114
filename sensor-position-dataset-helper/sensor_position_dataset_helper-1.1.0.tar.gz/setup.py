# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['sensor_position_dataset_helper']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.13,<4.0.0',
 'c3d>=0.3.0,<0.4.0',
 'imucal>=2.0.0,<3.0.0',
 'joblib>=1.0.0,<2.0.0',
 'nilspodlib>=3.1,<4.0',
 'numpy>=1.20.0,<2.0.0',
 'pandas>=1.2.2,<2.0.0',
 'scipy>=1,<2',
 'tpcp>=0.3.0,<0.4.0',
 'typing-extensions>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'sensor-position-dataset-helper',
    'version': '1.1.0',
    'description': 'A helper for the SensorPositionDateset (recorded 2019, published 2021)',
    'long_description': '[![PyPI](https://img.shields.io/pypi/v/sensor_position_dataset_helper)](https://pypi.org/project/sensor_position_dataset_helper/)\n![PyPI - Downloads](https://img.shields.io/pypi/dm/sensor_position_dataset_helper)\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n\n# SensorPositionComparison Helper\n\nThis is a helper module to extract and handle the data of the [SensorPositionComparison Dataset](TODO: Add updated link).\n\nIf you use the dataset and this module, please cite:\nTODO: Add citation once published\n\n## Installation and Usage\n\nInstall the project via `pip` or `poetry`:\n\n```\npip install sensor_position_dataset_helper\npoetry add sensor_position_dataset_helper\n```\n\n## Dataset Handling\n\nYou also need to download the actual Dataset from [here](https://zenodo.org/record/5747173).\nIf you are member of the matlab, you can also get a git-lfs version from \n[our internal server](https://mad-srv.informatik.uni-erlangen.de/MadLab/data/sensorpositoncomparison).\n\nThen you need to tell this library about the position of the dataset.\nNote that the path should point to the top-level repo folder of the dataset.\nThis can either be done globally:\n```python\nfrom sensor_position_dataset_helper import set_data_folder\n\nset_data_folder("PATH/TO/THE_DATASET")\n```\n\nOr on a-per function basis\n\n```python\nfrom sensor_position_dataset_helper import get_all_subjects\n\nget_all_subjects(data_folder="PATH/TO/THE_DATASET")\n```\n\nIf you are using the tpcp-dataset objects, you need to provide the path in the init.\n\n```python\nfrom sensor_position_dataset_helper.tpcp_dataset import SensorPositionDatasetSegmentation\n\ndataset = SensorPositionDatasetSegmentation(dataset_path="PATH/TO/THE_DATASET")\n```\n\n## Code Examples\n\nFor simple operations we suggest to use the provided functions.\nFor a list of functions see the `sensor_position_dataset_helper/helper.py` file.\n\nIn this example we load the gait test data of a 4x10 slow gait test of one participant:\n\n```python\nfrom sensor_position_dataset_helper import get_all_subjects, get_metadata_subject, get_imu_test, get_mocap_test\n\nDATA_FOLDER = "PATH/TO/THE_DATASET"\nprint(list(get_all_subjects(data_folder=DATA_FOLDER)))\n# [\'4d91\', \'5047\', \'5237\', \'54a9\', \'6dbe_2\', \'6e2e\', \'80b8\', \'8873\', \'8d60\', \'9b4b\', \'c9bb\', \'cb3d\', \'cdfc\', \'e54d\']\n\nprint(list(get_metadata_subject("54a9", data_folder=DATA_FOLDER)["imu_tests"].keys()))\n# [\'fast_10\', \'fast_20\', \'long\', \'normal_10\', \'normal_20\', \'slow_10\', \'slow_20\']\n\n# Finally get the data.\n# Note, this thorws a couple of warnings during the data loading, do to the use of custom sensor firmware.\n# These warnings can be ignored.\nimu_data = get_imu_test("54a9", "slow_10", data_folder=DATA_FOLDER)\n\nmocap_traj = get_mocap_test("54a9", "slow_10", data_folder=DATA_FOLDER)\n```\n\nFor advanced usage we recommend the use of the `tpcp` datasets.\nThey provide an object oriented way to access the data and abstract a lot of the complexity that comes with loading the\ndata.\nFor general information about object oriented datasets and why they are cool, check out our \n[`tpcp` library](https://github.com/mad-lab-fau/tpcp).\n\nHere we load the same data as above, but using the dataset object:\n```python\nfrom sensor_position_dataset_helper.tpcp_dataset import SensorPositionDatasetMocap\n\nDATA_FOLDER = "PATH/TO/THE_DATASET"\nds = SensorPositionDatasetMocap(data_folder=DATA_FOLDER)\nprint(ds)\n# SensorPositionDatasetMocap [98 groups/rows]\n#\n#      participant       test\n#   0         4d91    fast_10\n#   1         4d91    fast_20\n#   2         4d91       long\n#   3         4d91  normal_10\n#   4         4d91  normal_20\n#   ..         ...        ...\n#   93        e54d       long\n#   94        e54d  normal_10\n#   95        e54d  normal_20\n#   96        e54d    slow_10\n#   97        e54d    slow_20\n#   \n#   [98 rows x 2 columns]\n#\n\nprint(ds.get_subset(participant="54a9"))\n# SensorPositionDatasetMocap [7 groups/rows]\n#\n#     participant       test\n#   0        54a9    fast_10\n#   1        54a9    fast_20\n#   2        54a9       long\n#   3        54a9  normal_10\n#   4        54a9  normal_20\n#   5        54a9    slow_10\n#   6        54a9    slow_20\n#\n\ndata_point = ds.get_subset(participant="54a9", test="slow_10")\n\n# The data is not loaded until here.\n# Only when accessing the `.data` or the `marker_position_` attribute the data is loaded.\nimu_data = data_point.data\nmocap_traj = data_point.marker_position_\n```\n\n## Managing Dataset Revisions\n\nTo ensure reproducibility, you should save the version of the dataset that was used for a certain analysis.\nIf you are part of the MaD-Lab and using the internal git-versioned version of the dataset we provide some helpers.\n\nIf you are using the version from Zenodo, we unfortunally have no easy way to verify the version and integrity of the\nextracted data on disk.\nTherefore, make sure to document the version of the Zenodo dataset and verify the md5 hasshum of the zip-file you \ndownloaded from Zenodo.\n\nFor the git version you can use the helper as follows:\n\n```python\nfrom sensor_position_dataset_helper import ensure_git_revision\n\nensure_git_revision(data_folder="PATH/TO/THE_DATASET", version="EXPECTED GIT HASH")\n```\n\nThis will produce an error, if the dataset version you are using is not the one you expect, or if the dataset repo has \nuncommitted changes.\nThis will prevent bugs, because you accidentally use the wrong dataset version and will directly document the correct \nversion.\n',
    'author': 'Arne Küderle',
    'author_email': 'arne.kuederle@fau.de',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mad-lab-fau/sensor_position_dataset_helper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1,<3.9',
}


setup(**setup_kwargs)

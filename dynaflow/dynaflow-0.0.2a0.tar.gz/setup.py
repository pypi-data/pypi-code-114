# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dynaflow']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4,<9.0.0', 'mlflow>=1.24.0,<2.0.0', 'pynamodb>=5.2.1,<6.0.0']

entry_points = \
{'console_scripts': ['dynaflow = dynaflow.cli:dynaflow'],
 'mlflow.model_registry_store': ['dynamodb = '
                                 'dynaflow.model_registry:DynamodbModelStore'],
 'mlflow.tracking_store': ['dynamodb = '
                           'dynaflow.tracking_store:DynamodbTrackingStore']}

setup_kwargs = {
    'name': 'dynaflow',
    'version': '0.0.2a0',
    'description': 'AWS Dynamodb backend tracking store for MLFlow',
    'long_description': '# Dynaflow\n\nDynaflow implements a serverless AWS dynamodb tracking store and model registry for MLFlow. It\nallows to directly log runs and models to AWS Dynamodb using your AWS credentials. Further\nauthorisation can be implemented using Dynamodb fine-grained access control.\n\n## Setup\nDynaflow includes a simple CLI that helps to easily provision the Dynamodb tables. To deploy the\ntables, run\n\n```\ndynaflow deploy\n```\n\nwhich will deploy two AWS Dynamodb tables. To delete the tables, run\n\n```\ndynaflow destroy\n```\n\n\n# Configuration\nTo use the deployed Dynamodb tables as the backend to your tracking store and model registry,\nuse a tracking store uri of the following format:\n\n`dynamodb:<region>:<tracking-table-name>:<model-table-name>`\n\nwhere <tracking-table-name> is the name of the dynamodb table you want to use as tracking backend,\n<model-table-name>  is the name of the table used for the model registry and <region> is the region\nin which the tables reside.\n\nE.g. when using the python client, you can configure the client to use the dynamodb tracking\nbackend by running the following statement:\n\n`mlflow.set_tracking_uri("dynamodb:eu-central-1:mlflow-tracking-store:mlflow-model-registry")`\n\nTo use a table named "mlflow-tracking-store" for tracking and a table named "mlflow-model-registry" as\nthe model registry backend. Note that these are also the default names you get when running `dynaflow deploy`.\n\nIf you want to log your artifacts to s3 by default, you can set the environment variable `DYNAFLOW_ARTIFACT_BUCKET`:\n```\nexport DYNAFLOW_ARTIFACT_BUCKET=<artifact-bucket-name>\n```\n\nWhen running a tracking server, set the dynamodb tracking backend using the following command:\n\n`\nmlflow server\n    --backend-store-uri dynamodb:<region>:<tracking-table-name>:<model-table-name>\n    --default-artifact-root s3://<artifact-bucket-name>/\n``\n',
    'author': 'ArrichM',
    'author_email': 'maximilianjakob.arrich@student.unisg.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ArrichM/dynaflow',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

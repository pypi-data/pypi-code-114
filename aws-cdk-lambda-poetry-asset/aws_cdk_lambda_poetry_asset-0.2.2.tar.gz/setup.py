# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['aws_cdk_lambda_poetry_asset']

package_data = \
{'': ['*']}

install_requires = \
['aws-cdk-lib>=2.0.0,<3.0.0', 'docker>=5.0.3,<6.0.0']

setup_kwargs = {
    'name': 'aws-cdk-lambda-poetry-asset',
    'version': '0.2.2',
    'description': 'AWS CDK construct for packaging lambda functions with dependencies',
    'long_description': '[![pipeline status](https://gitlab.com/josef.stach/aws-cdk-lambda-asset/badges/master/pipeline.svg)](https://gitlab.com/josef.stach/aws-cdk-lambda-asset/commits/master)\n[![coverage report](https://gitlab.com/josef.stach/aws-cdk-lambda-asset/badges/master/coverage.svg)](https://gitlab.com/josef.stach/aws-cdk-lambda-asset/commits/master)\n\n# AWS CDK Lambda Poetry Asset\n\n## About\nThis is the cdk v2 version of the original asset, which is available at [gitlab](https://gitlab.com/josef.stach/aws-cdk-lambda-asset).\n\n\nAWS CDK currently supports 3 kinds of "Assets":\n\n* [InlineCode](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.InlineCode.html) - useful for one-line-lambdas\n* [AssetCode](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.AssetCode.html) - one-file lambdas without dependencies\n* [S3Code](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-lambda.S3Code.html) - existing lambda packages already uploaded in an S3 bucket\n\nThere is, however, no support for more complex lambda function which require third party dependencies.\nThis repository presents one possible approach to lambda packaging.\n\nThe construct is aware of libraries bundled in the AWS lambda runtime and automatically removes those for you to save space.\n\nIt also counts with compiled C dependencies such as NumPy and takes care of library stripping.\n\nBy setting the `create_file_if_exists` to `False` you can use it with a caching system, like Github Actions `actions/cache@v3`. It will only run the build if the file doesnt exist at the output path already.\n## Usage\nSuppose your project\'s directory structure looks like this:\n```\nmy-project\n├── business_logic\n│\xa0\xa0 └── backend.py\n└── functions\n    └── my_lambda.py\n```\n\nThen your stack would be:\n\n```python\nfrom pathlib import Path\nfrom aws_cdk import aws_lambda\nfrom aws_cdk_lambda_poetry_asset.zip_asset_code import ZipAssetCode\n\nclass MyStack(core.Stack):\n\n    def __init__(self, app: core.App, id: str, **kwargs) -> None:\n        super().__init__(app, id, **kwargs)\n        work_dir = Path(__file__).parents[1]\n        aws_lambda.Function(\n            scope=self,\n            id=\'MyLambda\',\n            code=ZipAssetCode(\n                work_dir=work_dir,\n                include=[\'functions\', \'business_logic\'],\n                file_name=\'my-lambda.zip\',\n                create_file_if_exists=False\n            )\n            handler=\'functions/my_lambda.lambda_handler\',\n            runtime=aws_lambda.Runtime.PYTHON_3_9\n        )\n```\n\n### Poetry file hash\n## License\nThis code is released under MIT license.\n\n## Setup\n\n#### [Install poetry](https://github.com/sdispater/poetry#installation)\n```commandline\npip install poetry\n```\n\n#### Install dependencies\n```commandline\npoetry update\n```\n\n#### Run tests\nStart docker first.\n```commandline\npoetry run pytest --cov-report term-missing --cov=aws_cdk_lambda_poetry_asset tests\n```\n',
    'author': 'Jesse Peters',
    'author_email': 'jesse@resist.bot',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jesse-peters/aws-cdk-lambda-asset',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

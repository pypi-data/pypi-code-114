# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['magnus_extension_aws_secrets_manager']

package_data = \
{'': ['*']}

install_requires = \
['magnus', 'magnus_extension_aws_config']

entry_points = \
{'magnus.integration.BaseIntegration': ['local-container-secrets-aws-secrets-manager '
                                        '= '
                                        'magnus_extension_aws_secrets_manager.integration:LocalContainerComputeAWSSecrets'],
 'magnus.secrets.BaseSecrets': ['aws-secrets-manager = '
                                'magnus_extension_aws_secrets_manager.aws_secrets_manager:AWSSecretsManager']}

setup_kwargs = {
    'name': 'magnus-extension-aws-secrets-manager',
    'version': '0.1.0',
    'description': 'Description you want to give',
    'long_description': "# AWS Secrets manager\n\nThis package is an extension to [magnus](https://github.com/AstraZeneca/magnus-core).\n\n## Provides \n\nProvides functionality to use AWS secrets manager to provide secrets\n\n## Installation instructions\n\n```pip install magnus_extension_secrets_aws_secrets_manager```\n\n## Set up required to use the extension\n\nAccess to AWS environment either via:\n\n- AWS profile, generally stored in ~/.aws/credentials\n- AWS credentials available as environment variables\n\nIf you are using environmental variables for AWS credentials, please set:\n\n- AWS_ACCESS_KEY_ID: AWS access key\n- AWS_SECRET_ACCESS_KEY: AWS access secret\n- AWS_SESSION_TOKEN: The session token, useful to assume other roles\n\nA AWS secrets store that you want to use to store the the secrets.\n\n## Config parameters\n\nThe full configuration of the AWS secrets manager is:\n\n```yaml\nsecrets:\n  type: 'aws-secrets-manager'\n  config:\n    secret_arn: The secret ARN to retrieve the secrets from.\n    region: # Region if we are using\n    aws_profile: #The profile to use or default\n    use_credentials: # Defaults to False\n```\n\n### **secret_arn**:\n\nThe arn of the secret that you want to use. Internally, we use boto3 to access the secrets.\n\nThe below parameters are inherited from AWS Configuration.\n\n### **aws_profile**:\n\nThe profile to use for acquiring boto3 sessions. \n\nDefaults to None, which is used if its role based access or in case of credentials present as environmental variables.\n\n### **region**:\n\nThe region to use for acquiring boto3 sessions.\n\nDefaults to *eu-west-1*.\n\n\n### **aws_credentials_file**:\n\nThe file containing the aws credentials.\n\nDefaults to ```~/.aws/credentials```.\n\n### **use_credentials**:\n\nSet it to ```True``` to provide AWS credentials via environmental variables.\n\nDefaults to ```False```.\n\n### ***role_arn***:\n\nThe role to assume after getting the boto3 session.\n\n**This is required if you are using ```use_credentials```.**\n",
    'author': 'Vijay Vammi',
    'author_email': 'vijay.vammi@astrazeneca.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AstraZeneca/magnus-extensions/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)

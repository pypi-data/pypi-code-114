# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['datadog_lambda']

package_data = \
{'': ['*']}

install_requires = \
['datadog>=0.41.0,<0.42.0', 'ddtrace>=0.58.1,<0.59.0', 'wrapt>=1.11.2,<2.0.0']

extras_require = \
{':python_version < "3.8"': ['typing_extensions>=4.0,<5.0',
                             'importlib_metadata>=1.0,<2.0'],
 u'dev': ['nose2>=0.9.1,<0.10.0',
          'httpretty>=0.9.7,<0.10.0',
          'boto3>=1.10.33,<2.0.0',
          'requests>=2.22.0,<3.0.0',
          'flake8>=3.7.9,<4.0.0']}

setup_kwargs = {
    'name': 'datadog-lambda',
    'version': '3.53.0',
    'description': 'The Datadog AWS Lambda Library',
    'long_description': '# datadog-lambda-python\n\n![build](https://github.com/DataDog/datadog-lambda-python/workflows/build/badge.svg)\n[![PyPI](https://img.shields.io/pypi/v/datadog-lambda)](https://pypi.org/project/datadog-lambda/)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/datadog-lambda)\n[![Slack](https://chat.datadoghq.com/badge.svg?bg=632CA6)](https://chat.datadoghq.com/)\n[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](https://github.com/DataDog/datadog-lambda-python/blob/main/LICENSE)\n\nDatadog Lambda Library for Python (3.6, 3.7, 3.8, and 3.9) enables enhanced Lambda metrics, distributed tracing, and custom metric submission from AWS Lambda functions.\n\n**IMPORTANT NOTE:** AWS Lambda is expected to receive a [breaking change](https://aws.amazon.com/blogs/compute/upcoming-changes-to-the-python-sdk-in-aws-lambda/) on **March 31, 2021**. If you are using Datadog Python Lambda layer version 7 or below, please upgrade to the latest.\n\n## Installation\n\nFollow the [installation instructions](https://docs.datadoghq.com/serverless/installation/python/), and view your function\'s enhanced metrics, traces and logs in Datadog.\n\n## Custom Metrics\n\nOnce [installed](#installation), you should be able to submit custom metrics from your Lambda function.\n\nCheck out the instructions for [submitting custom metrics from AWS Lambda functions](https://docs.datadoghq.com/integrations/amazon_lambda/?tab=python#custom-metrics).\n\n## Tracing\n\nOnce [installed](#installation), you should be able to view your function\'s traces in Datadog, and your function\'s logs should be automatically connected to the traces.\n\nFor additional details on trace collection, take a look at [collecting traces from AWS Lambda functions](https://docs.datadoghq.com/integrations/amazon_lambda/?tab=python#trace-collection).\n\nFor additional details on trace and log connection, see [connecting logs and traces](https://docs.datadoghq.com/tracing/connect_logs_and_traces/python/).\n\nFor additional details on the tracer, check out the [official documentation for Datadog trace client](http://pypi.datadoghq.com/trace/docs/index.html).\n\n## Enhanced Metrics\n\nOnce [installed](#installation), you should be able to view enhanced metrics for your Lambda function in Datadog.\n\nCheck out the official documentation on [Datadog Lambda enhanced metrics](https://docs.datadoghq.com/integrations/amazon_lambda/?tab=python#real-time-enhanced-lambda-metrics).\n\n## Advanced Configurations\n\n### Handler Wrapper\n\nIn order to instrument individual invocations, the Datadog Lambda library needs to wrap around your Lambda handler function. This is usually achieved by setting your function\'s handler to the Datadog handler function (`datadog_lambda.handler.handler`) and setting the environment variable `DD_LAMBDA_HANDLER` with your original handler function to be called by the Datadog handler.\n\nIf this method doesn\'t work for you, instead of setting the handler and the `DD_LAMBDA_HANDLER` environment variable, you can apply the Datadog Lambda library wrapper in your function code like below:\n\n```python\nfrom datadog_lambda.wrapper import datadog_lambda_wrapper\n\n@datadog_lambda_wrapper\ndef my_lambda_handle(event, context):\n    # your function code\n```\n\n## Environment Variables\n\n### DD_FLUSH_TO_LOG\n\nSet to `true` (recommended) to send custom metrics asynchronously (with no added latency to your Lambda function executions) through CloudWatch Logs with the help of [Datadog Forwarder](https://github.com/DataDog/datadog-serverless-functions/tree/main/aws/logs_monitoring). Defaults to `false`. If set to `false`, you also need to set `DD_API_KEY` and `DD_SITE`.\n\n### DD_API_KEY\n\nIf `DD_FLUSH_TO_LOG` is set to `false` (not recommended), the Datadog API Key must be defined by setting one of the following environment variables:\n\n- DD_API_KEY - the Datadog API Key in plain-text, NOT recommended\n- DD_KMS_API_KEY - the KMS-encrypted API Key, requires the `kms:Decrypt` permission\n- DD_API_KEY_SECRET_ARN - the Secret ARN to fetch API Key from the Secrets Manager, requires the `secretsmanager:GetSecretValue` permission (and `kms:Decrypt` if using a customer managed CMK)\n- DD_API_KEY_SSM_NAME - the Parameter Name to fetch API Key from the Systems Manager Parameter Store, requires the `ssm:GetParameter` permission (and `kms:Decrypt` if using a SecureString with a customer managed CMK)\n\nYou can also supply or override the API key at runtime (not recommended):\n\n```python\n# Override DD API Key after importing datadog_lambda packages\nfrom datadog import api\napi._api_key = "MY_API_KEY"\n```\n\n### DD_SITE\n\nIf `DD_FLUSH_TO_LOG` is set to `false` (not recommended), you must set `DD_SITE`. Possible values are `datadoghq.com`, `datadoghq.eu`, `us3.datadoghq.com`, `us5.datadoghq.com`, and `ddog-gov.com`. The default is `datadoghq.com`.\n\n### DD_LOGS_INJECTION\n\nInject Datadog trace id into logs for [correlation](https://docs.datadoghq.com/tracing/connect_logs_and_traces/python/) if you are using a `logging.Formatter` in the default `LambdaLoggerHandler` by the Lambda runtime. Defaults to `true`.\n\n### DD_LOG_LEVEL\n\nSet to `debug` enable debug logs from the Datadog Lambda Library. Defaults to `info`.\n\n### DD_ENHANCED_METRICS\n\nGenerate enhanced Datadog Lambda integration metrics, such as, `aws.lambda.enhanced.invocations` and `aws.lambda.enhanced.errors`. Defaults to `true`.\n\n### DD_LAMBDA_HANDLER\n\nYour original Lambda handler.\n\n### DD_TRACE_ENABLED\n\nInitialize the Datadog tracer when set to `true`. Defaults to `false`.\n\n### DD_MERGE_XRAY_TRACES\n\nSet to `true` to merge the X-Ray trace and the Datadog trace, when using both the X-Ray and Datadog tracing. Defaults to `false`.\n\n### DD_TRACE_MANAGED_SERVICES (experimental)\n\nInferred Spans are spans that Datadog can create based on incoming event metadata.\nSet `DD_TRACE_MANAGED_SERVICES` to `true` to infer spans based on Lambda events.\nInferring upstream spans is only supported if you are using the [Datadog Lambda Extension](https://docs.datadoghq.com/serverless/libraries_integrations/extension/).\nDefaults to `true`.\nInfers spans for:\n\n- API Gateway REST events\n- API Gateway WebSocket events\n- HTTP API events\n- SQS\n- SNS (SNS messaged delivered via SQS are also supported)\n- Kinesis Streams (if data is a JSON string or base64 encoded JSON string)\n- EventBridge (custom events, where Details is a JSON string)\n- S3\n- DynamoDB\n\n## Opening Issues\n\nIf you encounter a bug with this package, we want to hear about it. Before opening a new issue, search the existing issues to avoid duplicates.\n\nWhen opening an issue, include the Datadog Lambda Library version, Python version, and stack trace if available. In addition, include the steps to reproduce when appropriate.\n\nYou can also open an issue for a feature request.\n\n## Contributing\n\nIf you find an issue with this package and have a fix, please feel free to open a pull request following the [procedures](CONTRIBUTING.md).\n\n## Community\n\nFor product feedback and questions, join the `#serverless` channel in the [Datadog community on Slack](https://chat.datadoghq.com/).\n\n## License\n\nUnless explicitly stated otherwise all files in this repository are licensed under the Apache License Version 2.0.\n\nThis product includes software developed at Datadog (https://www.datadoghq.com/). Copyright 2019 Datadog, Inc.\n',
    'author': 'Datadog, Inc.',
    'author_email': 'dev@datadoghq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DataDog/datadog-lambda-python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6.0,<4',
}


setup(**setup_kwargs)

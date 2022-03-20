# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kubecrd']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=6.0', 'apischema>=0.15.0', 'kubernetes>=23.3.0,<24.0.0']

setup_kwargs = {
    'name': 'kubecrd',
    'version': '0.1.0',
    'description': 'Create Kubernetes CRD using Python dataclasses',
    'long_description': "========\nKube CRD\n========\n\nThe primary purpose of this project is to simplify working with Kubernetes\nCustom Resources. To achieve that it provides a base class,\n``kubecrd.OpenAPISchemaBase`` that can convert regular Python\ndataclassses into Kubernetes Custom Resource Definitions.\n\n\n  >>> from dataclasses import dataclass, field\n  >>> from uuid import UUID\n  >>> from kubecrd import OpenAPISchemaBase\n  >>> from apischema import schema\n\n  >>> @dataclass\n  ... class Resource(OpenAPISchemaBase):\n  ...     __group__ = 'example.com'\n  ...     __version__ = 'v1alpha1'\n  ...\n  ...     name: str\n  ...     tags: list[str] = field(\n  ...         default_factory=list,\n  ...         metadata=schema(\n  ...            description='regroup multiple resources',\n  ...            unique=False,\n  ...         ),\n  ...     )\n\n  >>> print(Resource.crd_schema())\n  apiVersion: apiextensions.k8s.io/v1\n  kind: CustomResourceDefinition\n  metadata:\n    name: resources.example.com\n  spec:\n    group: example.com\n    names:\n      kind: Resource\n      plural: resources\n      singular: resource\n    scope: Namespaced\n    versions:\n    - name: v1alpha1\n      schema:\n        openAPIV3Schema:\n          properties:\n            spec:\n              properties:\n                name:\n                  type: string\n                tags:\n                  default: []\n                  description: regroup multiple resources\n                  items:\n                    type: string\n                  type: array\n                  uniqueItems: false\n              required:\n              - name\n              type: object\n          type: object\n      served: true\n      storage: true\n  <BLANKLINE>\n\n\nIt is also possible to install the CRD in a cluster using a Kubernetes Client\nobject::\n\n  from from kubernetes import client, config\n  config.load_kube_config()\n  k8s_client = client.ApiClient()\n  Resource.install(k8s_client)\n\nYou can then find the resource in the cluster::\n\n  » kubectl get crds/resources.example.com\n  NAME                    CREATED AT\n  resources.example.com   2022-03-20T03:58:25Z\n\n  $ kubectl api-resources | grep example.com\n  resources     example.com/v1alpha1                  true         Resource\n\nInstallation of resource is idempotent, so re-installing an already installed\nresource doesn't raise any exceptions if ``exist_ok=True`` is passed in::\n\n  Resource.install(k8s_client, exist_ok=True)\n",
    'author': 'Abhilash Raj',
    'author_email': 'raj.abhilash1@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/maxking/kubcrd',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4',
}


setup(**setup_kwargs)

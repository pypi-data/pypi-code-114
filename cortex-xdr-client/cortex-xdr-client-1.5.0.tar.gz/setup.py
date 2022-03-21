# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': '.'}

packages = \
['cortex_xdr_client', 'cortex_xdr_client.api', 'cortex_xdr_client.api.models']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.8.2,<2.0.0', 'requests>=2.26.0,<3.0.0']

setup_kwargs = {
    'name': 'cortex-xdr-client',
    'version': '1.5.0',
    'description': 'API client for Cortex XDR Prevent',
    'long_description': '# cortex-xdr-client\n\nA python-based API client for [Cortex XDR API](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api).\n\nCurrently, it supports the following Cortex XDR **Prevent & Pro** APIs:\n\n\n#### Incidents API:\n- [Get Incidents](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-incidents.html)\n- [Get Extra Incident Data](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-extra-incident-data.html)\n\n\n#### Alerts API:\n- [Get Alerts](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/incident-management/get-alerts.html)\n\n\n#### Endpoints API:\n- [Get All Endpoints](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/endpoint-management/get-all-endpoints.html)\n- [Get Endpoint](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/endpoint-management/get-endpoints.html)\n- [Isolate Endpoints](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/isolate-endpoints.html)\n- [Scan Endpoints](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/scan-endpoints.html)\n- [Retrieve File](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/response-actions/retrieve-file.html)\n\n#### XQL API:\n- [Start XQL](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/xql-apis/start-xql-query.html)\n- [Get XQL Results](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/xql-apis/get-xql-query-results.html)\n- [Get XQL Result Stream](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/xql-apis/get-xql-query-exported-data.html)\n\n#### Scripts API:\n- [Get Scripts](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-scripts.html)\n- [Get Script Metadata](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-metadata.html)\n- [Get Script Execution Status](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-status.html)\n- [Get Script Execution Results](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-results.html)\n- [Get Script Execution Result Files](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/get-script-execution-result-files.html)\n- [Run Script](https://docs.paloaltonetworks.com/cortex/cortex-xdr/cortex-xdr-api/cortex-xdr-apis/script-execution/run-script.html)\n\n\n## Contributing\nSee [CONTRIBUTING.md](./CONTRIBUTING.md) for details.\n',
    'author': 'ebarti',
    'author_email': 'me@eloibarti.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ebarti/cortex-xdr-client',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)

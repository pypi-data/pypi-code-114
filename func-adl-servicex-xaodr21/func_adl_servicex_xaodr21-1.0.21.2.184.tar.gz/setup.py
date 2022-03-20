# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['func_adl_servicex_xaodr21',
 'func_adl_servicex_xaodr21.ROOT',
 'func_adl_servicex_xaodr21.ROOT.Detail',
 'func_adl_servicex_xaodr21.ROOT.Detail.TSchemaRuleSet',
 'func_adl_servicex_xaodr21.ROOT.Fit',
 'func_adl_servicex_xaodr21.ROOT.Math',
 'func_adl_servicex_xaodr21.std',
 'func_adl_servicex_xaodr21.templates',
 'func_adl_servicex_xaodr21.xAOD',
 'func_adl_servicex_xaodr21.xAOD.EventInfo_v1',
 'func_adl_servicex_xaodr21.xAOD.TruthEvent_v1',
 'func_adl_servicex_xaodr21.xAOD.TruthParticle_v1']

package_data = \
{'': ['*']}

install_requires = \
['func_adl_servicex>=2.0-beta.1,<3.0']

setup_kwargs = {
    'name': 'func-adl-servicex-xaodr21',
    'version': '1.0.21.2.184',
    'description': 'func-adl typed datasets for Servicex for xAOD R21 21.2.184',
    'long_description': None,
    'author': 'Gordon Watts',
    'author_email': 'gwatts@uw.edu',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<3.10',
}


setup(**setup_kwargs)

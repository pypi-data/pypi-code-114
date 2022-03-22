# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nautobot_plugin_chatops_panorama',
 'nautobot_plugin_chatops_panorama.api',
 'nautobot_plugin_chatops_panorama.migrations',
 'nautobot_plugin_chatops_panorama.tests',
 'nautobot_plugin_chatops_panorama.utils']

package_data = \
{'': ['*'], 'nautobot_plugin_chatops_panorama': ['static/nautobot_palo/*']}

install_requires = \
['defusedxml',
 'ipaddr',
 'nautobot-chatops',
 'netmiko',
 'netutils',
 'pan-os-python>=1.3.0,<2.0.0',
 'requests']

extras_require = \
{':extra == "nautobot"': ['nautobot>=1,<2']}

entry_points = \
{'nautobot.workers': ['panorama = '
                      'nautobot_plugin_chatops_panorama.worker:panorama']}

setup_kwargs = {
    'name': 'nautobot-plugin-chatops-panorama',
    'version': '1.1.0',
    'description': 'Nautobot Chatops plugin for Panorama',
    'long_description': '# Nautobot Panorama ChatOps\n\nThis is a plugin for [Nautobot](https://github.com/nautobot/nautobot) that extends ChatOps support to Palo Alto Panorama systems. The plugin adds some useful commands into your ChatOps environment that enhance an administrator\'s and end user\'s day to day using of Panorama. This framework allows for the quick extension of new ChatOps commands for Panorama.\n\nNote: While this plugin requires Nautobot and the base Nautobot ChatOps plugin, it does _not_ require the Panorama or Palo Alto inventory to be in Nautobot. It is effectively Nautobot-independent, except for using it as a backend to run the chat bot itself.\n\n## Usage\n\nThe supported commands are listed below. We welcome any new command or feature requests by submitting an issue or PR.\n\n| /panorama Command    | Description                                                                |\n| -------------------- | -------------------------------------------------------------------------- |\n| capture-traffic      | Run a packet capture on PANOS Device for specified IP traffic.             |\n| export-device-rules  | Generate a downloadable list of firewall rules with details in CSV format. |\n| get-device-rules     | Return a list of all firewall rules on a given device with details.        |\n| get-version          | Obtain software version information for Panorama.                          |\n| install-software     | Install software to specified Palo Alto device.                            |\n| upload-software      | Upload software to specified Palo Alto device.                             |\n| validate-rule-exists | Verify that a specific ACL rule exists within a device, via Panorama.      |\n\n## Prerequisites\n\nThis plugin requires the [Nautobot ChatOps Plugin](https://github.com/nautobot/nautobot-plugin-chatops) to be installed and configured before using. You can find detailed setup and configuration instructions [here](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/README.md).\n\n## Installation\n\nThe plugin is available as a Python package in pypi and can be installed with pip:\n\n```shell\npip install nautobot-plugin-chatops-panorama\n```\n\n> The plugin is compatible with Nautobot 1.1.0 and higher\n\nTo ensure Nautobot Panorama ChatOps is automatically re-installed during future upgrades, create a file named `local_requirements.txt` (if not already existing) in the Nautobot root directory (alongside `requirements.txt`) and list the `nautobot-plugin-chatops-panorama` package:\n\n```no-highlight\n# echo nautobot-plugin-chatops-panorama >> local_requirements.txt\n```\n\nOnce installed, the plugin needs to be enabled in your `nautobot_config.py`\n\n```python\n# In your configuration.py\nPLUGINS = ["nautobot_chatops", "nautobot_plugin_chatops_panorama"]\n```\n\nIn addition, add/update the below `PLUGINS_CONFIG` section to `nautobot_config.py`.\n\n> It is only necessary to add the sections from the below snippet for the chat platform you will be using (Slack, Webex, etc.).\n\n```python\n# Also in nautobot_config.py\nPLUGINS_CONFIG = {\n    "nautobot_chatops": {\n        # Slack\n        "enable_slack": os.environ.get("ENABLE_SLACK", False),\n        "slack_api_token": os.environ.get("SLACK_API_TOKEN"),\n        "slack_signing_secret": os.environ.get("SLACK_SIGNING_SECRET"),\n        "slack_slash_command_prefix": os.environ.get("SLACK_SLASH_COMMAND_PREFIX", "/"),\n        # Webex\n        "enable_webex": os.environ.get("ENABLE_WEBEX", False),\n        "webex_token": os.environ.get("WEBEX_TOKEN"),\n        "webex_signing_secret": os.environ.get("WEBEX_SIGNING_SECRET"),\n        # Mattermost\n        "enable_mattermost": os.environ.get("ENABLE_MATTERMOST", False),\n        "mattermost_api_token": os.environ.get("MATTERMOST_API_TOKEN"),\n        "mattermost_url": os.environ.get("MATTERMOST_URL"),\n        # MS Teams\n        "enable_ms_teams": os.environ.get("ENABLE_MS_TEAMS", False),\n        "microsoft_app_id": os.environ.get("MICROSOFT_APP_ID"),\n        "microsoft_app_password": os.environ.get("MICROSOFT_APP_PASSWORD"),\n    },\n    "nautobot_plugin_chatops_panorama": {\n        "panorama_host": os.environ.get("PANORAMA_HOST"),\n        "panorama_user": os.environ.get("PANORAMA_USER"),\n        "panorama_password": os.environ.get("PANORAMA_PASSWORD"),\n    },\n}\n```\n\n### Environment Variables\n\nYou will need to set the following environment variables for your Nautobot instance, then restart the services for them to take effect.\n\n- PANORAMA_HOST - This is the management DNS/IP address used to reach your Panorama instance.\n- PANORAMA_USER - A user account with API access to Panorama.\n- PANORAMA_PASSWORD - The password that goes with the above user account.\n\n```bash\nexport PANORAMA_HOST="{{ Panorama DNS/URL }}"\nexport PANORAMA_USER="{{ Panorama account username }}"\nexport PANORAMA_PASSWORD="{{ Panorama account password }}"\n```\n\nIf the base Nautobot Chatops plugin is not already installed, the following environment variables are required for the chat platform in use. The [Platform-specific Setup](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup/chat_setup.md#platform-specific-setup) document describes how to retrieve the tokens and secrets for each chat platform that will need to be used in the environment variables.\n\n> It is only necessary to create the environment variables shown below for the chat platform you will be using. To make the environment variables persistent, add them to the ~/.bash_profile for the user running Nautobot.\n\n```bash\n# Slack\nexport ENABLE_SLACK="true"\nexport SLACK_API_TOKEN="foobar"\nexport SLACK_SIGNING_SECRET="foobar"\n# Webex\nexport ENABLE_WEBEX="true"\nexport WEBEX_TOKEN="foobar"\nexport WEBEX_SIGNING_SECRET="foobar"\n# Mattermost\nexport ENABLE_MATTERMOST="false"\nexport MATTERMOST_API_TOKEN="foobar"\nexport MATTERMOST_URL="foobar"\n# Microsoft Teams\nexport ENABLE_MS_TEAMS="false"\nexport MICROSOFT_APP_ID="foobar"\nexport MICROSOFT_APP_PASSWORD="foobar"\n```\n\n> When deploying as Docker containers, all of the above environment variables should be defined in the file `development/creds.env`. An example credentials file `creds.env.example` is available in the `development` folder.\n\n## Access Control\n\nJust like with the regular `/nautobot` command from the base Nautobot ChatOps plugin, the `/panorama` command supports access control through the Access Grants menu in Nautobot. See section [Grant Access to the Chatbot](https://github.com/nautobot/nautobot-plugin-chatops/blob/develop/docs/chat_setup/chat_setup.md#grant-access-to-the-chatbot) in the installation guide for the base Nautobot ChatOps plugin for setting this up.\n\n## Questions\n\nFor any questions or comments, please check the [FAQ](FAQ.md) first and feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).\nSign up [here](http://slack.networktocode.com/)\n\n## Screenshots\n\n![Help](docs/img/screenshot1.png)\n\n![Validate Rule Exists Success](docs/img/screenshot2.png)\n\n![Validate Rule Exists Failure](docs/img/screenshot3.png)\n\n![Upload Software](docs/img/screenshot4.png)\n\n![Capture Traffic Filter](docs/img/screenshot5.png)\n\n![Capture Traffic](docs/img/screenshot6.png)\n',
    'author': 'Network to Code, LLC',
    'author_email': 'opensource@networktocode.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/networktocode-llc/nautobot-plugin-chatops-panorama',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

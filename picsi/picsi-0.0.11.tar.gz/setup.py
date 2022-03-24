# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['picsi', 'picsi.commands', 'picsi.vendored']

package_data = \
{'': ['*'], 'picsi': ['scripts/*']}

install_requires = \
['halo>=0.0.31,<0.0.32',
 'requests>=2.27.1,<3.0.0',
 'tomli-w>=1.0.0,<2.0.0',
 'tomli>=2.0.0,<3.0.0',
 'typer[all]>=0.4.0,<0.5.0']

entry_points = \
{'console_scripts': ['picsi = picsi.picsi:app']}

setup_kwargs = {
    'name': 'picsi',
    'version': '0.0.11',
    'description': 'CSI collection on Raspberry Pi',
    'long_description': '# picsi\n\nNexmon CSI utilities for Raspberry Pi\n\n***In development &bull; Not ready for testing yet.***\n\n## Features\n\n- [x] ⚡ **Superfast** installs with pre-compiled binaries\n- [x] ⌛ Compiles from source when binaries are not available\n- [x] 🚀 Easy Start/Stop CSI collection with `picsi up` or `picsi down`\n- [x] ✨ Restore original firmware and connect to WiFi with `picsi disable`\n- [ ] 💾 Saves CSI to .pcap files\n- [ ] 📡 Forward CSI packets to other devices for faster collection\n- [ ] 📁 Manage your CSI collection configuration with Profiles\n\n## Install \n\nOn a Raspberry Pi 3B+ or 4B, run:  \n\n```bash\nsudo apt install python3-pip  # install pip for python3\npip3 install picsi            # install picsi \nsource ~/.profile             # update $PATH\n\npicsi install\n```\n\n\n`picsi` will download the appropriate firmware and binaries for\nyour system and install them, or compile from source if they\nare not available pre-compiled.\n\n\n## Docs\n\nPicsi (pronounced pixie?) is a Python tool to install Nexmon CSI on Raspberry Pis.\nIt needs Python version `>= 3.7`, although using the latest version is recommended.\n\nThe best features of picsi, in my opinion, are:\n\n#### Installing Nexmon CSI from pre-compiled binaries.\n\nCompiling Nexmon_CSI on the Pi takes about an hour, and downloads about 1.5 GB of data.\nAnd it needs your attention for the entire duration because you need to reboot the Pi \nmultiple times, and keep a look out for errors.\n\nPicsi downloads appropriate pre-compiled nexmon_csi firmware and binaries (nexutil, makecsiparams) \nfor your kernel from https://github.com/nexmonster/nexcsi-bin.git (repository not available yet), \nand installs them. If binaries are not available, it installs from source, including automatic \nunattended reboots, and logs errors and progress.\n\n#### Forwards CSI packets to an IP\n\nPicsi can forward CSI packets to a different computer on your network, which is potentially\nfaster than the Pi, and can collect more packets than tcpdump on the Pi can.\n\nBut additionally, an app on your phone/laptop can listen to the packets,\nand plot the CSI in realtime or process it.\n\n#### Profiles!\n\nManage your csi collection configuration in profiles!\n\nwrite\n```toml\n[profiles.CustomProfileName]\n    channel = 36\n    bandwidth = 80\n\n    coremask = 1\n    ssmask = 1\n\n    forward = false\n    forward_ip = \'192.168.1.25\'\n\n    duration = 30\n\n    macids = [\'ab:cd:ef:12:34\']\n```\n\nin profiles.toml, and you can start csi collection with\n\n`picsi up CustomProfileName`.\n\nThis collects CSI on channel 36, bandwidth 80 from macids for 30 seconds,\nand forwards that CSI to 192.168.1.25. After 30 seconds, CSI collection is stopped\nand original wifi firmware is restored.\n\nYou can also create a set of profiles, and make picsi loop CSI collection over them.\n\nOnly basic CSI collection via profiles will be added first, and other profile features will\nbe added later.\n\n## Help page\n```\nUsage: picsi {{ COMMAND | help }} [--option] [--option argument]\n       COMMAND := {{ install | uninstall | up | down | save | forward | rebuild | help }}\n       OPTION  := {{ --url | --branch | --nexmon-url | --nexmon-branch | --apt-upgrade |\n                    --no-source | --no-binaries | --binary-url }}\n\nExamples: picsi help\n          picsi install\n          picsi install --url \\"$NEX_REPO_URL\\" --no-source\n\nCOMMAND\n\n    i | install\n        Installs Nexmon_CSI.\n    U | uninstall\n        Uninstalls Nexmon_CSI. Note: Upppercase U.\n    e | Enable\n        Enables CSI collection. WiFi will be disabled.\n    d | disable\n        Disables CSI collection and enables WiFi.\n    s | save\n        Save CSI to pcap file\n    f | forward | fw\n        Forward CSI packets to another IP\n    r | rebuild\n        Rebuilds the Nexmon_CSI from source.\n    h | help\n        Shows this help page.\n\nOPTION\n\n    --url\n        URL for the Nexmon_CSI repository to git clone.\n        The default value is \'https://github.com/nexmonster/nexmon_csi.git\'\n    \n    --branch\n        The git branch name in the cloned repository to\n        use. The default value is \'master\'.\n        A commit hash or git object hash would work too.\n\n    --nexmon-url\n        URL for the Nexmon base repository to git clone.\n        The default value is \'https://github.com/seemoo-lab/nexmon.git\',\n\n    --nexmon-branch\n        The git branch in the cloned repository to\n        use. The default is value \'master\'.\n        A commit hash, or git object hash would work too.\n    \n    --apt-upgrade\n        Runs apt upgrade before installing. Not recommended.\n        Running apt upgrade might upgrade your kernel.\n\n    --no-source\n        Prevent Nex from compiling Nexmon_CSI from source. If this flag\n        is not present, Nex will fall back to compiling Nexmon_CSI from\n        source when pre-compiled binaries are not available.\n\n    --no-binaries\n        Nex tries to use pre-compiled binaries when available,\n        and will fall back to compiling Nexmon_CSI from source when not.\n        Supply this flag to prevent use of pre-compiled binaries.\n\n    --binary-url\n        URL for the repository with precompiled binaries.\n        Default URL is \'https://github.com/nexmonster/nexcsi-bin.git\'.\n\nNotes:\n    WiFi will be unavailable for use when Nexmon_CSI is being used.\n    Use an Ethernet cable or a second WiFi adapter if you\'re using SSH.\n```',
    'author': 'Aravind Reddy Voggu',
    'author_email': 'zerodividedby0@gmail.com',
    'maintainer': 'Aravind Reddy Voggu',
    'maintainer_email': 'zerodividedby0@gmail.com',
    'url': 'https://github.com/nexmonster/picsi.git',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

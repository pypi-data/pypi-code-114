# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['das', 'das.parsers']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.7.1,<0.8.0', 'netaddr>=0.8.0,<0.9.0', 'tinydb>=4.6.1,<5.0.0']

entry_points = \
{'console_scripts': ['das = das.divideandscan:main',
                     'divideandscan = das.divideandscan:main']}

setup_kwargs = {
    'name': 'divideandscan',
    'version': '0.2.6',
    'description': 'Divide full port scan results and use it for targeted Nmap runs',
    'long_description': '<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/113610876-632a4300-9656-11eb-9583-d07f4e34d774.png" width="350px" alt="DivideAndScan">\n</p>\n\n<p align="center">\n  <strong>Divide <strike>Et Impera</strike> And Scan (and also merge the scan results)</strong>\n</p>\n\n<p align="center">\n  <a href="https://github.com/snovvcrash/DivideAndScan/blob/main/pyproject.toml#L3"><img src="https://img.shields.io/badge/version-0.2.6-success" alt="version" /></a>\n  <a href="https://github.com/snovvcrash/DivideAndScan/search?l=python"><img src="https://img.shields.io/badge/python-3.9-blue?logo=python&logoColor=white" alt="python" /></a>\n  <a href="https://www.codacy.com/gh/snovvcrash/DivideAndScan/dashboard?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=snovvcrash/DivideAndScan&amp;utm_campaign=Badge_Grade"><img src="https://app.codacy.com/project/badge/Grade/35f0bdfece9846d7aab3888b01642813" alt="codacy" /></a>\n  <a href="https://github.com/snovvcrash/DivideAndScan/actions/workflows/publish-to-pypi.yml"><img src="https://github.com/snovvcrash/DivideAndScan/actions/workflows/publish-to-pypi.yml/badge.svg" alt="pypi" /></a>\n  <a href="https://github.com/snovvcrash/DivideAndScan/actions/workflows/publish-to-docker-hub.yml"><img src="https://github.com/snovvcrash/DivideAndScan/actions/workflows/publish-to-docker-hub.yml/badge.svg" alt="docker" /></a>\n</p>\n\n---\n\n**D**ivide**A**nd**S**can is used to efficiently automate port scanning routine by splitting it into 3 phases:\n\n1. Discover open ports for a bunch of targets.\n2. Run Nmap individually for each target with version grabbing and NSE actions.\n3. Merge the results into a single Nmap report (different formats available).\n\nFor the 1st phase a *fast port scanner*\\* is intended to be used, whose output is parsed and stored in a single file database ([TinyDB](https://github.com/msiemens/tinydb)). Next, during the 2nd phase individual Nmap scans are launched for each target with its set of open ports (multiprocessing is supported) according to the database data. Finally, in the 3rd phase separate Nmap outputs are merged into a single report in different formats (XML / HTML / simple text / grepable) with [nMap_Merger](https://github.com/CBHue/nMap_Merger).\n\nPotential use cases:\n\n* Pentest engagements / red teaming with a large scope to enumerate.\n* Cybersecurity wargames / training CTF labs.\n* OSCP certification exam.\n\n\\* Available port scanners:\n\n* [Nmap](https://github.com/nmap/nmap)\n* [Masscan](https://github.com/robertdavidgraham/masscan)\n* [RustScan](https://github.com/RustScan/RustScan)\n* [Naabu](https://github.com/projectdiscovery/naabu)\n* [NimScan](https://github.com/elddy/NimScan)\n\n> **DISCLAIMER.** All information contained in this repository is provided for educational and research purposes only. The author is not responsible for any illegal use of this tool.\n\n## How It Works\n\n![how-it-works.png](https://user-images.githubusercontent.com/23141800/113610892-67566080-9656-11eb-8520-8fa2dcaf3463.png)\n\n## How to Install\n\n### Prerequisites\n\nTo successfully *divide and scan* we need to get some good port scanning tools.\n\n📑 **Note:** if you don\'t feel like messing with dependecies on your host OS, skip to the [Docker](#using-from-docker) part.\n\n#### Nmap\n\n```bash\nsudo apt install nmap xsltproc -y\nsudo nmap --script-updatedb\n```\n\n#### Masscan\n\n```bash\ncd /tmp\nwget https://github.com/robertdavidgraham/masscan/archive/refs/heads/master.zip -O masscan-master.zip\nunzip masscan-master.zip\ncd masscan-master\nmake\nsudo make install\ncd && rm -rf /tmp/masscan-master*\n```\n\n#### RustScan\n\n```bash\ncd /tmp\n\nwget https://api.github.com/repos/RustScan/RustScan/releases/latest -qO- \\\n| grep "browser_download_url.*amd64.deb" \\\n| cut -d: -f2,3 \\\n| tr -d \\" \\\n| wget -qO rustscan.deb -i-\n\nsudo dpkg -i rustscan.deb\ncd && rm /tmp/rustscan.deb\n\nsudo wget https://gist.github.com/snovvcrash/8b85b900bd928493cd1ae33b2df318d8/raw/fe8628396616c4bf7a3e25f2c9d1acc2f36af0c0/rustscan-ports-top1000.toml -O /root/.rustscan.toml\n```\n\n#### Naabu\n\n```bash\nsudo mkdir /opt/projectdiscovery\nsudo chown $USER:$USER /opt/projectdiscovery\ncd /opt/projectdiscovery\n\nwget https://api.github.com/repos/projectdiscovery/naabu/releases/latest -qO- \\\n| grep "browser_download_url.*linux_amd64.zip" \\\n| cut -d: -f2,3 \\\n| tr -d \\" \\\n| wget -qO naabu.zip -i-\n\nunzip naabu.zip\nchmod +x naabu\ncd && rm /opt/projectdiscovery/naabu.zip\n\nsudo ln -s /opt/projectdiscovery/naabu /usr/local/bin/naabu\n```\n\n#### NimScan\n\n```bash\nsudo mkdir /opt/nimscan\nsudo chown $USER:$USER /opt/nimscan\ncd /opt/nimscan\n\nwget https://api.github.com/repos/elddy/NimScan/releases/latest -qO- \\\n| grep \'browser_download_url.*NimScan"\' \\\n| cut -d: -f2,3 \\\n| tr -d \\" \\\n| wget -qO nimscan -i-\n\nchmod +x nimscan\ncd\n\nsudo ln -s /opt/nimscan/nimscan /usr/local/bin/nimscan\n```\n\n### Installation\n\nDivideAndScan is available on PyPI as `divideandscan`, though I recommend installing it from GitHub with [pipx](https://github.com/pipxproject/pipx) in order to always have the bleeding-edge version:\n\n```console\n~$ pipx install -f "git+https://github.com/snovvcrash/DivideAndScan.git"\n~$ das\n```\n\nFor debbugging purposes you can set up a dev environment with [poetry](https://github.com/python-poetry/poetry):\n\n```console\n~$ git clone https://github.com/snovvcrash/DivideAndScan\n~$ cd DivideAndScan\n~$ poetry install\n~$ poetry run das\n```\n\n📑 **Note:** DivideAndScan uses sudo to run all the port scanners, so it will ask for the password when scanning commands are invoked.\n\n### Using from Docker\n\nYou can run DivideAndScan in a Docker container as follows:\n\n```console\n~$ docker run -it --rm --name das -v ~/.das:/root/.das -v `pwd`:/app snovvcrash/divideandscan\n```\n\nSince the tool requires some input data and produces some output data, you should specify your current working directory as the mount point at `/app` within the container. You may want to set an alias to make the base command shorter:\n\n```console\n~$ alias das=\'docker run -it --rm --name das -v ~/.das:/root/.das -v `pwd`:/app snovvcrash/divideandscan\'\n~$ das\n```\n\n## How to Use\n\n![how-to-use.png](https://user-images.githubusercontent.com/23141800/113610915-6fae9b80-9656-11eb-8b1a-db503dd43861.png)\n\n### 1. Filling the DB\n\n<table>\n<tr>\n<td>\n\nProvide the `add` module a command for a fast port scanner to discover open ports in a desired range.\n\n⚠️ **Warning:** please, make sure that you understand what you\'re doing, because nearly all port scanning tools [can damage the system being tested](https://github.com/RustScan/RustScan/wiki/Usage#%EF%B8%8F-warning) if used improperly.\n\n```console\n# Masscan\n~$ das add masscan \'--rate 1000 -iL hosts.txt -p1-65535 --open\'\n# RustScan\n~$ das add rustscan \'-b 1000 -t 2000 -u 5000 -a hosts.txt -r 1-65535 -g --no-config\'\n# Naabu\n~$ das add naabu \'-rate 1000 -iL hosts.txt -p - -silent -s s\'\n# NimScan\n~$ das add nimscan \'192.168.1.0/24 -vi -p:1-65535 -f:500\'\n# Nmap, -v flag is always required for correct parsing!\n~$ das add nmap \'-v -n -Pn --min-rate 1000 -T4 -iL hosts.txt -p1-65535 --open\'\n```\n\nWhen the module starts its work, a directory `~/.das/db` is created where the database file and raw scan results will be put when the module routine finishes.\n\n</td>\n</tr>\n</table>\n\n### 2. Targeted Scanning\n\n<table>\n<tr>\n<td>\n\nLaunch targeted Nmap scans with the `scan` module. You can adjust the scan surface with either `-hosts` or `-ports` option:\n\n```console\n# Scan by hosts\n~$ das scan -hosts all -oA report1\n~$ das scan -hosts 192.168.1.0/24,10.10.13.37 -oA report1\n~$ das scan -hosts hosts.txt -oA report1\n# Scan by ports\n~$ das scan -ports all -oA report2\n~$ das scan -ports 22,80,443,445 -oA report2\n~$ das scan -ports ports.txt -oA report2\n```\n\nTo start Nmap simultaneously in multiple processes, specify the `-parallel` switch and set number of workers with the `-proc` option (if no value is provided, it will default to the number of processors on the machine):\n\n```console\n~$ das scan -hosts all -oA report -parallel [-proc 4]\n```\n\nThe output format is selected with `-oX`, `-oN`, `-oG` and `-oA` options for XML+HTML formats, simple text format, grepable format and all formats respectively. When the module completes its work, a directory `~/.das/nmap_<DB_NAME>` is created containig Nmap raw scan reports.\n\nAlso, you can inspect the contents of the database with `-show` option before actually launching the scans:\n\n```console\n~$ das scan -hosts all -show\n```\n\n</td>\n</tr>\n</table>\n\n### 3 (Optional). Merging the Reports\n\n<table>\n<tr>\n<td>\n\nIn order to generate a report independently of the `scan` module, you should use the `report` module. It will search for Nmap raw scan reports in the `~/.das/nmap_<DB_NAME>` directory and process and merge them based on either `-hosts` or `-ports` option:\n\n```console\n# Merge outputs by hosts\n~$ das report -hosts all -oA report1\n~$ das report -hosts 192.168.1.0/24,10.10.13.37 -oA report1\n~$ das report -hosts hosts.txt -oA report1\n# Merge outputs by ports\n~$ das report -ports all -oA report2\n~$ das report -ports 22,80,443,445 -oA report2\n~$ das report -ports ports.txt -oA report2\n```\n\n📑 **Note:** keep in mind that the `report` module does **not** search the DB when processing the `-hosts` or `-ports` options, but looks for Nmap raw reports directly in `~/.das/nmap_<DB_NAME>` directory instead; it means that `-hosts 127.0.0.1` argument value will be successfully resolved only if `~/.das/nmap_<DB_NAME>/127-0-0-1.*` files exist, and `-ports 80` argument value will be successfully resolved only if `~/.das/nmap_<DB_NAME>/port80.*` files exist.\n\n</td>\n</tr>\n</table>\n\n<details>\n<summary><strong>🔥 Example 🔥</strong></summary>\n\nLet\'s enumerate open ports for all live machines on [Hack The Box](https://www.hackthebox.eu/home/machines).\n\n1. Add mappings "host ⇄ open ports" to the database with Masscan. For demonstration purposes I will exclude dynamic port range to avoid unnecessary stuff by using `-p1-49151`. On the second screenshot I\'m reviewing scan results by hosts and by ports:\n\n```console\n~$ das -db htb add -rm masscan \'-e tun0 --rate 1000 -iL hosts.txt -p1-49151 --open\'\n```\n\n<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/117919590-f578d300-b2f5-11eb-8afb-f8e3ed851e62.png" alt="example-1.png">\n</p>\n\n```console\n~$ das -db htb scan -hosts all -show\n~$ das -db htb scan -ports all -show\n```\n\n<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/117919602-fa3d8700-b2f5-11eb-8d4a-f2edb0272e2e.png" alt="example-2.png">\n</p>\n\n2. Launch Nmap processes for each target to enumerate only ports that we\'re interested in (the open ports). On the second screenshot I\'m doing the same but starting Nmap processes simultaneously:\n\n```console\n~$ das -db htb scan -hosts all -oA report\n```\n\n<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/117919624-03c6ef00-b2f6-11eb-9539-64a5a6ced1cf.png" alt="example-3.png">\n</p>\n\n```console\n~$ das -db htb scan -hosts all -oA report -nmap \'-Pn -sVC -O\' -parallel\n```\n\n<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/117919633-0a556680-b2f6-11eb-8cbe-78d1e9ce16f1.png" alt="example-4.png">\n</p>\n\n3. As a result we now have a single report in all familiar Nmap formats (simple text, grepable, XML) as well as a pretty HTML report.\n\n<p align="center">\n  <img src="https://user-images.githubusercontent.com/23141800/117919635-0c1f2a00-b2f6-11eb-933f-ee812e6f6bd0.png" alt="example-5.png">\n</p>\n\n</details>\n\n## Bring Your Own Scanner!\n\nYou can pair your favourite port scanner with DivideAndScan by implementing a single **parse** method for its output in `das/parsers/DUMMY_SCANNER.py` (see [example](/das/parsers/masscan.py) for masscan):\n\n```python\nfrom das.parsers import IAddPortscanOutput\n\n\nclass AddPortscanOutput(IAddPortscanOutput):\n    """Child class for processing DUMMY_SCANNER output."""\n\n    def parse(self):\n        """\n        DUMMY_SCANNER raw output parser.\n\n        :return: a pair of values (portscan raw output filename, number of hosts added to DB)\n        :rtype: tuple\n        """\n        hosts = set()\n        for line in self.portscan_raw:\n            # DUMMY_SCANNER parser implementation\n            pass\n\n        return (self.portscan_out, len(hosts))\n```\n\n## Help\n\n```\nusage: das [-h] {add,scan,report,help} ...\n\n -----------------------------------------------------------------------------------------------\n|  ________  .__      .__    .___        _____              .____________                       |\n|  \\______ \\ |__|__  _|__| __| _/____   /  _  \\   ____    __| _/   _____/ ____ _____    ____    |\n|   |    |  \\|  \\  \\/ /  |/ __ |/ __ \\ /  /_\\  \\ /    \\  / __ |\\_____  \\_/ ___\\\\__  \\  /    \\   |\n|   |    `   \\  |\\   /|  / /_/ \\  ___//    |    \\   |  \\/ /_/ |/        \\  \\___ / __ \\|   |  \\  |\n|  /_______  /__| \\_/ |__\\____ |\\___  >____|__  /___|  /\\____ /_______  /\\___  >____  /___|  /  |\n|          \\/                 \\/    \\/        \\/     \\/      \\/       \\/     \\/     \\/     \\/   |\n|  {@snovvcrash}            {https://github.com/snovvcrash/DivideAndScan}             {vX.Y.Z}  |\n -----------------------------------------------------------------------------------------------\n\npositional arguments:\n  {add,scan,report,help}\n    add                 run a full port scan and add the output to DB\n    scan                run targeted Nmap scans against hosts and ports from DB\n    report              merge separate Nmap outputs into a single report in different formats\n    help                show builtin --help dialog of a selected port scanner\n\noptional arguments:\n  -h, --help            show this help message and exit\n\nPsst, hey buddy... Wanna do some organized p0r7 5c4nn1n6?\n```\n\n## ToDo\n\n* [x] <strike>Add [projectdiscovery/naabu](https://github.com/projectdiscovery/naabu) parser</strike>\n* [x] <strike>Add [elddy/NimScan](https://github.com/elddy/NimScan) parser</strike>\n* [ ] Add [ZMap](https://github.com/zmap/zmap) parser\n* [ ] Add armada (?) parser\n* [ ] Store hostnames (if there\'re any) next to their IP values\n\n## Support\n\nIf this tool has been useful for you, feel free to buy me a <strike>beer</strike> coffee!\n\n[![beer.png](https://user-images.githubusercontent.com/23141800/113611163-d03dd880-9656-11eb-9279-e5e2689b0c1b.png)](https://buymeacoff.ee/snovvcrash)\n',
    'author': 'Sam Freeside',
    'author_email': 'snovvcrash@protonmail.ch',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/snovvcrash/DivideAndScan',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

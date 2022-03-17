# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['z2', 'z2.network', 'z2.process', 'z2.strings', 'z2.utils']

package_data = \
{'': ['*']}

install_requires = \
['ciscoconfparse>=1.6.0', 'loguru==0.6.0', 'sh>=1.14', 'toml==0.10.2']

setup_kwargs = {
    'name': 'z2',
    'version': '0.0.26',
    'description': 'A set of tools',
    'long_description': '\n\n# Table of Contents\n\n1. [Background](#L1-background)\n2. [Log variables / output messages](#L2-log-things)\n3. [Run a command with realtime stdout](#L2-run-cmd01)\n4. [Run a command with blocked stdout](#L2-run-cmd02)\n5. [Print with Color](#L2-color)\n6. [Handle network interface addresses](#L2-network-addresses)\n\n# Background <a name="L1-background" />\n\nQ: What exactly is this module called [`z2`][1]?\n\nA: Various code bites to keep my python code DRY.\n\n## Log variables / output messages <a name="L2-log-things" />\n\n```python\n## LogIt() is implemented by loguru.\n##  loguru is a complete python logging rewrite.\n##\n##  See https://github.com/Delgan/loguru\n\nfrom z2.utils import LogIt\n\nLogIt().info("You forgot to eat your corn flakes")\n```\n\n## Run a command with streaming realtime stdout <a name="L2-zrun-cmd01" />\n\nThere are a couple of `zrun` recipies to consider...\n\n1. Run three pings and see output in realtime.\n\n- `realtime=True` allows you to watch individual pings as they happen...\n- add all stdout to a list\n\n```python\nfrom z2.process import zrun\n\n## Call z2.process.zrun()...\n## - Watch individual pings as they happen... like you ran it in bash / zsh / ??\n## - add all output to a list\noutput = list(zrun("ping -c3 172.16.1.1", print_stdout=True, realtime=True))\n\nprint(output)\n```\n\n2. Run non-stop pings and act on individual pings.\n\n- `realtime=True` allows you to watch individual pings as they happen...\n- add all stdout to a list\n\n```python\nfrom datetime import datetime\nimport errno\n\nfrom z2.process import zrun\n\ndef act_on_ping(condition=None, now=datetime.now()):\n    assert isinstance(condition, str)\n\n    if condition=="foo":\n        # Do something...\n        pass\n\n    # Much more here...\n\n\n## Call z2.process.zrun()...\n## - Watch individual pings as they happen... like you ran it in bash / zsh / ??\n## - add all output to a list\n\nfor ii in zrun("ping -c5 -O 172.16.1.1", print_stdout=True, realtime=True):\n\n    if isinstance(ii, str):\n        output.append(ii)\n\n    if isinstance(ii, str) and "no answer" in ii.lower():\n        # Lost a ping -> "no answer yet for icmp_seq=1"\n        #     do something here\n        act_on_ping(condition="ping_timeout")\n\n    elif isinstance(ii, int) and ii==errno.EWOULDBLOCK:\n        # This is normal while waiting on ping stdout...\n        print("    errno.EWOULDBLOCK")\n        pass\n\nprint(output)\n```\n\n## Run a command with blocked stdout <a name="L2-zrun-cmd02" />\n\n1. Run three pings with blocked stdout\n\n- `realtime=False` blocks stdout\n- results are returned in a `list()`\n\n```python\nfrom z2.process import zrun\n\n## Call z2.process.zrun()...\n## - stdout is blocked during cmd execution\n## - return all output as a list of strings\noutput = list(zrun("ping -c3 172.16.1.1", print_stdout=True, realtime=False))\n\nprint(output)\n```\n\n## Print with Color <a name="L2-color" />\n\n```python\nfrom z2.strings import C\n\n# Print with green, orange\nprint(C.GREEN + "Hello" + C.YELLOW + " World" + C.ENDC)\n```\n\n## Handle network interface addresses <a name="L2-network-addresses" />\n\nMost network interfaces take an IPv4 or IPv6 address format with a network\nmask or a mask-length.  However, when you try to store both address and\nmask in Python stdlib, you hit a problem.  `IPv4Address()` does not process a\nmask, and `IPv4Network()` does not store "host-bits".  Consider the following:\n\n```python\n\n>>> # IPv4Address() and IPv4Network() are from python stdlib.\n>>> from ipaddress import IPv4Address, IPv4Network\n>>> intfAddr = IPv4Address("1.1.1.200/24")\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "/opt/python37/lib/python3.7/ipaddress.py", line 1300, in __init__\n    raise AddressValueError("Unexpected \'/\' in %r" % address)\nipaddress.AddressValueError: Unexpected \'/\' in \'1.1.1.200/24\'\n>>>\n>>>\n>>> ### IPv4Network() does not store "host bits", only "network bits".\n>>> ### As such, IPv4Network() is **useless** to hold network devices\'\n>>> ### real-life needs (to store the interface address and mask).\n>>>\n>>> intfAddr = IPv4Network("1.1.1.200/24")\nTraceback (most recent call last):\n  File "<stdin>", line 1, in <module>\n  File "/opt/python37/lib/python3.7/ipaddress.py", line 1536, in __init__\n    raise ValueError(\'%s has host bits set\' % self)\nValueError: 1.1.1.200/24 has host bits set\n>>> intfAddr = IPv4Network("1.1.1.200/24", strict=False)\n>>> intfAddr\nIPv4Network(\'1.1.1.0/24\')\n>>> ### Above ^^^^^^ we see that IPv4Network() strips .200 from the\n>>> ### address.\n\nKeeping the interface address and mask is supported out of the box with\nz2.IPv4Obj(). See below...\n\n>>> from z2 import IPv4Obj\n>>> intfAddr = IPv4Obj("1.1.1.200/24")\n>>>\n>>> intfAddr\n<IPv4Obj 1.1.1.200/24>\n>>>\n```\n\n  [1]: https://github.com/mpenning/z2\n',
    'author': 'Mike Pennington',
    'author_email': 'mike@pennington.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mpenning/z2/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6',
}


setup(**setup_kwargs)

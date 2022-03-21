# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['me_backup']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML',
 'click>=8.0.1,<9.0.0',
 'python-crontab>=2.5.1,<3.0.0',
 'wakeonlan>=2.0.1,<3.0.0']

setup_kwargs = {
    'name': 'me-backup',
    'version': '0.1.23',
    'description': 'Simple linux backup controled by a YAML file.',
    'long_description': "# me-backup\n\n# Install\n\nBaixar o pacote do PIP.\n```shell\n    $ sudo python -m pip install me-backup\n```\n\nPara testar a instalação, rode o comando de help:\n```\n    $ sudo python -m me_backup --help   \n    Usage: python -m me_backup [OPTIONS] COMMAND [ARGS]...\n\n    Options:\n    --help  Show this message and exit.\n\n    Commands:\n    install  Create needed files (run with sudo).\n```\n\nCaso não exista nenhuma instalação anterior em `/etc/me-backup`, simplesmente chame o módulo dentro da instalação de python do sistema usando sudo. Isso irá abrir um formulário para instação dos recursos.\n\nNeste caso, é exigido uso de privilégio, porque o pacote irá realizar alterações na pasta `/etc/me-backup` e no cron do usuário informado na instalação em `/var/spool/cron/`.\n\n```shell\n    $ sudo python -m me_backup install\n    \n    Me-backup never runned, this follow steps will create the tool folder and config file into /etc/me-backup! (need sudo)\n    Default User: [lucas] \n    Users shell rc: [/home/lucas/.zshrc]\n    Task file: [/etc/me-backup/tasks.yaml] \n    Log path: [/etc/me-backup/mebk.log] \n    Log level: [INFO] \n    Default host: [127.0.0.1]               \n    Default crontab path: [/var/spool/lucas]\n```\n\nPronto! Rodando o help novamente, outros comandos para uso serão listados.\n\n```shell\n    $ sudo python -m me_backup --help\n    \n    Usage: python -m me_backup [OPTIONS] COMMAND [ARGS]...\n\n    Options:\n    --help  Show this message and exit.\n\n    Commands:\n    generate_yaml  Create a tasks.yaml model file.\n    print_rsync    Return the rsync command\n    run_now        Run the backup tasks right now.\n    schedule       Schedule the tasks to run using your time configurations.\n```\n\nDentro da pasta `/etc/me-backup` o arquivo `tasks.yaml` será criado. Nele existe uma tarefa de modelo pré-configurada:\n\n```yaml\n    tasks:\n    - name: backup home\n        slug: bkp_home\n        src: /home/lucas/Arduino\n        remote_src: False\n        dst: /mnt/storage/backup/TESTE/dst1/Arduino\n        remote_dst: False\n        copy_config:\n        type: sync\n        wake_on_lan:\n        enabled: False\n        mac_address: 'd8:9c:67:07:87:e3'\n        frequency:\n        shortcut: daily\n        exclude:\n        extensions:\n            - txt\n        folder:\n            - .ssh\n```",
    'author': 'Lucas',
    'author_email': 'lucasbmello96@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/lbmello/me-backup',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

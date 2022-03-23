# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dnevnik4python']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'fake-useragent>=0.1.11,<0.2.0',
 'lxml>=4.8.0,<5.0.0',
 'pytz>=2022.1,<2023.0',
 'requests>=2.27.1,<3.0.0']

setup_kwargs = {
    'name': 'dnevnik4python',
    'version': '0.0.8',
    'description': 'Wrapper for python that simplifies work with dnevnik.ru',
    'long_description': '# dnevnik4python\n\nDnevnik4python - это библиотека для Python позволяющая удобно работать с электронным дневником dnevnik.ru\n\nГлавное отличие от оффициального API это то, что не требуется заключать договор и регистрировать приложение  \n\n- Простая с работа с Дневником\n- Получение оценок, д/з, расписания уроков \n\n## Пример\n\n```python\nfrom dnevnik4python import Diary\nfrom datetime import datetime\n\nlogin = "login"\npassword = "password"\n\n# войти в аккаунт\nd = Diary(login, password)\n\n# получить дневник на сегодня\nprint(d.get_diary(datetime.now()))\n# получить дневник на 2 дня вперед\nprint(d.get_diary(datetime.now(), 2))\n# получить дневник за прошлые 2 дня\nprint(d.get_diary(datetime.now(), -2))\n# получить дневник по указанным датам\nprint(d.get_diary(datetime(year = 2020, month = 4, day = 1), datetime(year = 2020, month = 4, day = 4)))\n```\n\n## Установка\n### *Linux/macOS*\n```\npip3 install dnevnik4python\n```\n### *Windows*\n```\npip install dnevnik4python\n```\n\n## Планы на будущее\n- Сделать библиотеку более удобной в использовании\n\n## По всем вопросам\nhttps://t.me/arzt_arsch\n',
    'author': 'hrog-zip',
    'author_email': '65674012+hrog-zip@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/hrog-zip/dnevnik4python',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

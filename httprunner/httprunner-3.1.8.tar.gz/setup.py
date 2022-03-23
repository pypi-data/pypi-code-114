# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['httprunner',
 'httprunner.app',
 'httprunner.app.routers',
 'httprunner.builtin',
 'httprunner.ext',
 'httprunner.ext.har2case',
 'httprunner.ext.locust',
 'httprunner.ext.uploader']

package_data = \
{'': ['*']}

install_requires = \
['Brotli>=1.0.9,<2.0.0',
 'black>=19.10b0,<20.0',
 'jinja2>=3.0.3,<4.0.0',
 'jmespath>=0.9.5,<0.10.0',
 'loguru>=0.4.1,<0.5.0',
 'pydantic>=1.8,<1.9',
 'pytest-html>=3.1.1,<4.0.0',
 'pytest>=7.1.1,<8.0.0',
 'pyyaml>=5.4.1,<6.0.0',
 'requests>=2.22.0,<3.0.0',
 'sentry-sdk>=0.14.4,<0.15.0']

extras_require = \
{'allure': ['allure-pytest>=2.8.16,<3.0.0'],
 'locust': ['locust>=1.0.3,<2.0.0'],
 'upload': ['requests-toolbelt>=0.9.1,<0.10.0', 'filetype>=1.0.7,<2.0.0']}

entry_points = \
{'console_scripts': ['har2case = httprunner.cli:main_har2case_alias',
                     'hmake = httprunner.cli:main_make_alias',
                     'hrun = httprunner.cli:main_hrun_alias',
                     'httprunner = httprunner.cli:main',
                     'locusts = httprunner.ext.locust:main_locusts']}

setup_kwargs = {
    'name': 'httprunner',
    'version': '3.1.8',
    'description': 'One-stop solution for HTTP(S) testing.',
    'long_description': '\n# HttpRunner\n\n[![downloads](https://pepy.tech/badge/httprunner)](https://pepy.tech/project/httprunner)\n[![unittest](https://github.com/httprunner/httprunner/workflows/unittest/badge.svg\n)](https://github.com/httprunner/httprunner/actions)\n[![integration-test](https://github.com/httprunner/httprunner/workflows/integration_test/badge.svg\n)](https://github.com/httprunner/httprunner/actions)\n[![codecov](https://codecov.io/gh/httprunner/httprunner/branch/master/graph/badge.svg)](https://codecov.io/gh/httprunner/httprunner)\n[![pypi version](https://img.shields.io/pypi/v/httprunner.svg)](https://pypi.python.org/pypi/httprunner)\n[![pyversions](https://img.shields.io/pypi/pyversions/httprunner.svg)](https://pypi.python.org/pypi/httprunner)\n[![TesterHome](https://img.shields.io/badge/TTF-TesterHome-2955C5.svg)](https://testerhome.com/github_statistics)\n\n*HttpRunner* is a simple & elegant, yet powerful HTTP(S) testing framework. Enjoy! ✨ 🚀 ✨\n\n> 欢迎参加 HttpRunner [用户调研问卷][survey]，你的反馈将帮助 HttpRunner 更好地成长！\n\n## Design Philosophy\n\n- Convention over configuration\n- ROI matters\n- Embrace open source, leverage [`requests`][requests], [`pytest`][pytest], [`pydantic`][pydantic], [`allure`][allure] and [`locust`][locust].\n\n## Key Features\n\n- [x] Inherit all powerful features of [`requests`][requests], just have fun to handle HTTP(S) in human way.\n- [x] Define testcase in YAML or JSON format, run with [`pytest`][pytest] in concise and elegant manner.\n- [x] Record and generate testcases with [`HAR`][HAR] support.\n- [x] Supports `variables`/`extract`/`validate`/`hooks` mechanisms to create extremely complex test scenarios.\n- [x] With `debugtalk.py` plugin, any function can be used in any part of your testcase.\n- [x] With [`jmespath`][jmespath], extract and validate json response has never been easier.\n- [x] With [`pytest`][pytest], hundreds of plugins are readily available.\n- [x] With [`allure`][allure], test report can be pretty nice and powerful.\n- [x] With reuse of [`locust`][locust], you can run performance test without extra work.\n- [x] CLI command supported, perfect combination with `CI/CD`.\n\n## Sponsors\n\nThank you to all our sponsors! ✨🍰✨ ([become a sponsor](sponsors.md))\n\n### 金牌赞助商（Gold Sponsor）\n\n[<img src="assets/hogwarts.jpeg" alt="霍格沃兹测试开发学社" width="400">](https://ceshiren.com/)\n\n> [霍格沃兹测试开发学社](http://qrcode.testing-studio.com/f?from=httprunner&url=https://ceshiren.com)是业界领先的测试开发技术高端教育品牌，隶属于[测吧（北京）科技有限公司](http://qrcode.testing-studio.com/f?from=httprunner&url=https://www.testing-studio.com) 。学院课程由一线大厂测试经理与资深测试开发专家参与研发，实战驱动。课程涵盖 web/app 自动化测试、接口测试、性能测试、安全测试、持续集成/持续交付/DevOps，测试左移&右移、精准测试、测试平台开发、测试管理等内容，帮助测试工程师实现测试开发技术转型。通过优秀的学社制度（奖学金、内推返学费、行业竞赛等多种方式）来实现学员、学社及用人企业的三方共赢。\n\n> [进入测试开发技术能力测评!](http://qrcode.testing-studio.com/f?from=httprunner&url=https://ceshiren.com/t/topic/14940)\n\n### 开源服务赞助商（Open Source Sponsor）\n\n[<img src="assets/sentry-logo-black.svg" alt="Sentry" width="150">](https://sentry.io/_/open-source/)\n\nHttpRunner is in Sentry Sponsored plan.\n\n## Subscribe\n\n关注 HttpRunner 的微信公众号，第一时间获得最新资讯。\n\n<img src="assets/qrcode.jpg" alt="HttpRunner" width="200">\n\n如果你期望加入 HttpRunner 核心用户群，请填写[用户调研问卷][survey]并留下你的联系方式，作者将拉你进群。\n\n[requests]: http://docs.python-requests.org/en/master/\n[pytest]: https://docs.pytest.org/\n[pydantic]: https://pydantic-docs.helpmanual.io/\n[locust]: http://locust.io/\n[jmespath]: https://jmespath.org/\n[allure]: https://docs.qameta.io/allure/\n[HAR]: http://httparchive.org/\n[survey]: https://wj.qq.com/s2/9699514/0d19/\n',
    'author': 'debugtalk',
    'author_email': 'debugtalk@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/httprunner/httprunner',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)

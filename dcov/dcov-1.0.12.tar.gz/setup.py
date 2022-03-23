# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['dcov', 'dcov.violationsreporters']

package_data = \
{'': ['*'], 'dcov': ['templates/*']}

install_requires = \
['Jinja2>=2.7.1',
 'Pygments>=2.9.0,<3.0.0',
 'chardet>=3.0.0',
 'pluggy>=0.13.1,<2']

extras_require = \
{':python_version < "3.8"': ['setuptools>=17.0.0'],
 'toml': ['tomli>=1.2.1,<2.0.0']}

entry_points = \
{'console_scripts': ['dcov = dcov.diff_cover_tool:main',
                     'dcov-quality = dcov.diff_quality_tool:main']}

setup_kwargs = {
    'name': 'dcov',
    'version': '1.0.12',
    'description': '1.0.12',
    'long_description': '增量覆盖率工具 DCOV\n===================\n\n## 介绍\n\ndcov 是一个 `通过 git 统计不同 branch 之间差异，并生成报告` 的工具， 它主要有以下功能:\n\n1. 统计两个 branch 之间的差异，生成 `差异报告`\n\n```\n# dcov --compare-branch HEAD^ \nDiff changes between HEAD^ and HEAD\nchanged files: 11, changed lines: 185\n\ndcov/diff_cover_tool.py (1 lines): 231\ndcov/git_diff.py (1 lines): 102\ndcov/report_generator.py (12 lines): 23-25, 27-28, 35, 103-105, 111, 178, 188\ndcov/templates/console_coverage_report.txt (6 lines): 1-2, 4, 13, 19, 22\ndcov/templates/console_quality_report.txt (5 lines): 1, 5, 17, 23, 26\ndcov/templates/html_coverage_report.html (1 lines): 9\ndcov/templates/markdown_coverage_report.md (7 lines): 1-3, 8, 10, 12-13\ndcov/violationsreporters/violations_reporter.py (38 lines): 5, 28, 30, 32-33, 37, 68, 74-75, 77, 192-193, 218-223, 225-226, 228, 230, 232-245, 248, 251\npyproject.toml (2 lines): 3-4\nREADME.md (73 lines): 4-76\ntests/data/cobe.xml (39 lines): 1-39\n```\n\n2. 根据标准的 `cobertura` 或则 `clover` 格式的单元测试覆盖率报告，生成增量覆盖率, 下面这个例子是我用 `phpunit` 单元测试覆盖率报告 cobe.xml 生成增量覆盖率报告，可以看到工具会生成每个文件对应的覆盖率情况，以及没有覆盖的代码所在的行号\n\n```\n# dcov --compare-branch HEAD^ --coverage_xml tests/data/cobe.xml\n--------------------------\nDiff Coverage Report\nDiff: HEAD^ HEAD, staged and unstaged changes\n--------------------------\ndcov/diff_cover_tool.py (0.0%): Missing lines 231\ndcov/git_diff.py (0.0%): Missing lines 102\ndcov/report_generator.py (0.0%): Missing lines 23-25,27-28,35,103-105,111,178,188\ndcov/templates/console_coverage_report.txt (0.0%): Missing lines 1-2,4,13,19,22\ndcov/templates/console_quality_report.txt (0.0%): Missing lines 1,5,17,23,26\ndcov/templates/html_coverage_report.html (0.0%): Missing lines 9\ndcov/templates/markdown_coverage_report.md (0.0%): Missing lines 1-3,8,10,12-13\ndcov/violationsreporters/violations_reporter.py (2.6%): Missing lines 5,28,30,32-33,37,68,74,77,192-193,218-223,225-226,228,230,232-245,248,251\npyproject.toml (0.0%): Missing lines 3-4\nREADME.md (0.0%): Missing lines 4-76\ntests/data/cobe.xml (0.0%): Missing lines 1-39\n--------------------------\nTotal:   185 lines\nMissing: 184 lines\nCoverage: 0%\n--------------------------\n```\n\n## 前提\n\n本工具需要系统安装 `git` 工具\n\n## 安装\n\n直接通过 `pip` 安装\n\n```\npip install dcov\ndcov --version\n```\n\n通过 `dcov --help` 查看常用的功能\n\n```\n# 黑白名单, 如我不想把 app/ 和 scripts/ 目录下的文件加入覆盖率计算\ndcov --compare-branch @~15 --exclude */app/* */scripts/*\n\n# 忽略空白差异\ndcov --compare-branch @~15 --ignore-whitespace\n\n# 生成覆盖率报告,支持 html json markdown 格式, 以下是生成 html 格式报告\ndcov --compare-branch @~15 --coverage_xml coverage_unit_test.xml --exclude */app/* */scripts/* --html-report this_is_our_html_report.html\n```\n\n## 贡献代码\n\n开发需要使用到 `poetry` 工具\n\n```\npip install poetry\n```\n\n在 fork 本仓库 [dcov](https://github.com/xiak/dcov), 在您本人仓库开发后再提交 `PR` 合并回本仓库\n\n```\ngit clone https://github.com/xxxxxxx/dcov.git\ncd dcov\npoetry run dcov --version\n```\n\n## 感谢\n\n本工具原作者为 [Bachmann1234](https://github.com/Bachmann1234/diff_cover)\n\ndcov 在原工具基础上加入一些新特性，以及修改了原来的覆盖率计算方法。\n',
    'author': 'See Contributors',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/xiak/dcov',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'entry_points': entry_points,
    'python_requires': '>=3.6.2,<4.0.0',
}


setup(**setup_kwargs)

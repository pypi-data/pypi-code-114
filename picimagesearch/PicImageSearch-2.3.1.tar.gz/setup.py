# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['PicImageSearch', 'PicImageSearch.Utils']

package_data = \
{'': ['*']}

install_requires = \
['aiofiles>=0.8.0,<0.9.0',
 'beautifulsoup4>=4.10.0,<5.0.0',
 'httpx>=0.22.0,<0.23.0',
 'loguru>=0.6.0,<0.7.0',
 'pathlib2>=2.3.7,<3.0.0']

setup_kwargs = {
    'name': 'picimagesearch',
    'version': '2.3.1',
    'description': 'PicImageSearch APIs for Python 3.x 适用于 Python 3 以图搜源整合API',
    'long_description': "# PicImageSearch\n![release](https://img.shields.io/github/v/release/kitUIN/PicImageSearch)\n![issues](https://img.shields.io/github/issues/kitUIN/PicImageSearch)\n![stars](https://img.shields.io/github/stars/kitUIN/PicImageSearch)\n![forks](https://img.shields.io/github/forks/kitUIN/PicImageSearch)  \n\n聚合整合图片识别api,用于以图搜源(以图搜图，以图搜番)，支持SauceNAO,tracemoe,iqdb,ascii2d,google(谷歌识图),baidu(百度识图)等\n# [文档](https://www.kituin.fun/wiki/picimagesearch/)\n\n## 支持\n- [x] [SauceNAO](https://saucenao.com/)\n- [x] [TraceMoe](https://trace.moe/) (6月30日更新新的api)\n- [x] [Iqdb](http://iqdb.org/)\n- [x] [Ascii2D](https://ascii2d.net/)\n- [x] [Google谷歌识图](https://www.google.com/imghp)  \n- [x] [BaiDu百度识图](https://graph.baidu.com/)\n- [x] 异步\n## 关于异步用法\n使用方法相似且较为简单  \n不懂异步的请百度学习异步后再使用  \n详细见测试文件夹内异步测试文件  \n```python \nasync with NetWork() as client:  # 可以设置代理 NetWork(proxies='http://127.0.0.1:10809')\n   saucenao = AsyncSauceNAO(client=client)  # client不能少\n   res = await saucenao.search('https://pixiv.cat/77702503-1.jpg')\n    # 下面操作与同步方法一致\n```\n### 安装\n- 此包需要 Python 3.6 或更新版本。\n- `pip install PicImageSearch`\n- 或者\n- `pip install PicImageSearch -i https://pypi.tuna.tsinghua.edu.cn/simple`\n\n",
    'author': 'kitUIN',
    'author_email': 'kulujun@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/kitUIN/PicImageSearch',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)

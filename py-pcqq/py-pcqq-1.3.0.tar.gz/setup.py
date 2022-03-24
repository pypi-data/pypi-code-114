from setuptools import setup, find_packages



packages = find_packages()

setup(
    name='py-pcqq',
    version='1.3.0',
    url='https://github.com/DawnNights/py-pcqq',
    author='DawnNights',
    author_email='2224825532@qq.com',
    packages=packages,
    description=u'一个使用pcqq协议的简易python qqbot库',
    long_description='''

简介
----

PY-PCQQ 是一个基于 **QQ轻聊版 7.9** 客户端协议的 Python 异步 QQ
机器人支持库，它会对 QQ
服务端发出的协议包进行解析和处理，并以插件化的形式，分发给消息所对应的命令处理器。

除了起到解析消息的作用，PY-PCQQ 还通过
装饰器、异步、回调等方式实现了一套简洁易用的会话机制和插件机制，以便于用户快速上手。

PY-PCQQ 在其底层与 QQ 服务端实现交互的部分使用的是标准库
``asyncio.open_connection`` 所创建的异步 TCP
连接，这意味着在本协议库提供的内容多为异步操作，在调用相关函数或方法时应注意加上
**await** 关键字。

本项目基本仅由 Python3
的标准库所实现，但若是在没有图形界面的系统中使用扫码登录，需要自行安装第三方库
``pillow`` 使得程序能在终端环境中打印登录二维码。值得一提的是，在
Android 手机等移动设备中，你也可以通过
`pydroid3 <https://apkdownloadforandroid.com/ru.iiec.pydroid3/>`__
这样的应用来安装运行本协议库，例如:
`在手机上玩转QQ机器人？ <https://b23.tv/ZVHP0lK>`__

最后要说的是，这个项目仅仅只是本废物空闲之余的兴趣之作，存在着大量不成熟与不完善的地方。如果对
QQ 机器人开发有所需求，可以移步至更加强大与稳定的
`mirai <https://github.com/mamoe/mirai>`__ 或
`go-cqhttp <https://github.com/Mrs4s/go-cqhttp/>`__ 等项目。

已实现功能
----------

登录
^^^^

-  ☒ 账号密码登录
-  ☒ 二维码登录
-  ☒ 本地Token重连

发送消息
^^^^^^^^

-  ☒ At
-  ☒ 文本
-  ☒ 表情
-  ☒ xml卡片
-  ☒ 图片

接收消息
^^^^^^^^

-  ☒ At
-  ☒ 文本
-  ☒ 图片
-  ☒ 表情

接收事件
^^^^^^^^

-  ☒ 群消息
-  ☒ 好友消息
-  ☒ 进群事件
-  ☒ 退群事件
-  ☒ 禁言事件

其它操作
^^^^^^^^

-  ☒ 修改群成员Card
-  ☒ 设置群成员禁言

文档
----

暂时咕咕中，请自行查看项目中的 ``example.py`` 查看案例

'''
    
)

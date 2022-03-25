#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : demo.py
# @Time         : 2021/11/11 下午3:20
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :

from appzoo import *


def easy_run(app_dir: str, port=8000, access_log=True, prefix='/'):
    app = App()
    app.add_apps(app_dir, prefix=prefix)
    app.run(port=port, access_log=access_log)



if __name__ == '__main__':
    easy_run('a.py', prefix='/')
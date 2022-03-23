#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : mi.
# @File         : iapp
# @Time         : 2020/10/22 11:01 上午
# @Author       : yuanjie
# @Email        : yuanjie@xiaomi.com
# @Software     : PyCharm
# @Description  : 

from meutils.pipe import *

from starlette.status import *
from starlette.responses import *
from starlette.requests import Request
from starlette.staticfiles import StaticFiles

from fastapi import FastAPI, Form, Depends, File, UploadFile


class App(object):

    def __init__(self, verbose=True):
        self.app = FastAPI()
        self.verbose = verbose  # 是否返回请求体
        self.get = self.app.get
        self.post = self.app.post

    def run(self, app=None, host="0.0.0.0", port=8000, workers=1, access_log=True, debug=False, **kwargs):
        """

        :param app:   app字符串可开启热更新 debug/reload
        :param host:
        :param port:
        :param workers:
        :param access_log:
        :param debug: reload
        :param kwargs:
        :return:
        """

        import uvicorn
        """
        https://www.cnblogs.com/poloyy/p/15549265.html 
        https://blog.csdn.net/qq_33801641/article/details/121313494
        """
        uvicorn.config.LOGGING_CONFIG['formatters']['access'][
            'fmt'] = '%(asctime)s - %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'

        if debug == False:
            access_log = False

        uvicorn.run(
            app if app else self.app,
            host=host, port=port, workers=workers, access_log=access_log, debug=debug, **kwargs
        )

    def add_route(self, path='/xxx', func=lambda x='demo': x, method="GET", **kwargs):

        handler = self._handler(func, method, **kwargs)
        self.app.api_route(path=path, methods=[method])(handler)

    def add_apps(self, app_dir='apps', **kwargs):
        """加载当前app_dir文件夹下的所有app, 入口函数都是main"""
        routes = []
        for p in Path(app_dir).rglob('*.py'):
            if not p.stem.startswith('_'):  # 过滤_开头的py
                route = str(p)[:-3]
                func = importlib.import_module(route.replace('/', '.')).main
                self.add_route(route, func, method='POST', **kwargs)

                routes.append(route)

        logger.info(f"Add Routes: {routes}")

        self.add_route(f'/__{app_dir}', lambda: routes, method='GET', **kwargs)
        return routes

    def _handler(self, func, method='GET', result_key='data', **kwargs):
        """

        :param func:
        :param method:
            get -> request: Request
            post -> kwargs: dict
        :param result_key:
        :return:
        """
        if method == 'GET':
            async def handler(request: Request):
                input = dict(request.query_params)
                return self._try_func(input, func, result_key, **kwargs)

        elif method == 'POST':
            async def handler(kwargs_: dict):  # todo 表单 request.form()
                input = kwargs_
                return self._try_func(input, func, result_key, **kwargs)

        else:
            async def handler():
                return {'Warning': 'method not in {"GET", "POST"}'}

        return handler

    def _try_func(self, kwargs, func, result_key='data', **kwargs_):
        input = kwargs
        output = OrderedDict()

        if self.verbose:
            output['requestParams'] = input

        try:
            output['success'] = 1
            output[result_key] = func(**input)

        except Exception as error:
            output['success'] = 0
            output['error'] = error
            output['errorPlus'] = traceback.format_exc().strip()

        finally:
            output.update(kwargs_)

        return output

    def app_file_name(self, file=__file__):
        return Path(file).stem


if __name__ == '__main__':
    import uvicorn

    app = App()
    app.add_route('/get', lambda **kwargs: kwargs, method="GET", result_key="GetResult")
    app.add_route('/post', lambda **kwargs: kwargs, method="POST", result_key="PostResult")

    # app.run(port=9000, debug=False, reload=False, access_log=True)
    # app.run(f"{app.app_file_name(__file__)}", port=9000, debug=False, reload=False)

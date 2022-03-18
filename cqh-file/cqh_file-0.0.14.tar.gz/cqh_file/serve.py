import json
import hashlib
from tornado import web
import base64
import os
from cqh_file.utils import get_base64, get_md5


class HandlerList(web.RequestHandler):

    def post(self):
        """
        获取获取所有文件名以及md5
        """
        target_dir = self.settings['dir']
        info_d = {}
        for name in os.listdir(target_dir):
            file_path = os.path.join(target_dir, name)
            if os.path.isfile(file_path):
                info_d[name] = get_md5(file_path)
        self.write(json.dumps(info_d, ensure_ascii=False, indent=2))


class HandlerDownload(web.RequestHandler):
    def web_write(self, d):
        self.write(json.dumps(d, ensure_ascii=False, indent=2))

    def post(self):
        d = json.loads(self.request.body)
        name = d['name']
        target_dir = self.settings['dir']
        file_path = os.path.join(target_dir, name)
        ret = {
            "code": 0,
            "data": None,
            "msg": ""
        }
        if not os.path.exists(file_path):
            ret['code'] = 1
            ret['msg'] = "not exists"
            self.web_write(ret)
            return
        if not os.path.isfile(file_path):
            ret.update({"code": 2, 'msg': "is not file"})
            self.web_write(ret)
            return
        ret['data'] = get_base64(file_path)
        self.web_write(ret)


def create_app(port, dir, timeout):
    from tornado import web, ioloop
    app = web.Application(handlers=[
        ("/list", HandlerList),
        ("/download", HandlerDownload),
    ], dir=dir)
    server = app.listen(port, xheaders=True)
    loop: ioloop.IOLoop = ioloop.IOLoop.current()
    loop.start()

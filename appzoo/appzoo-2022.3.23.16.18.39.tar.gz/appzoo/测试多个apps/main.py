#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Project      : nesc.
# @File         : demo.py
# @Time         : 2021/11/11 下午3:20
# @Author       : yuanjie
# @WeChat       : 313303303
# @Software     : PyCharm
# @Description  :

from appzoo import App
from meutils.pipe import *

app = App(False)
app.add_apps()


#########################个性化#########################
@app.post('/xx')
def func():
    return 'OK'

print('xxx')

#########################个性化#########################

app_ = app.app



if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=8501)

    import uvicorn

    uvicorn.config.LOGGING_CONFIG['formatters']['access'][
        'fmt'] = '%(asctime)s - %(levelprefix)s %(client_addr)s - "%(request_line)s" %(status_code)s'

    # debug
    app.run(f"{app.app_file_name(__file__)}:app_", port=9000, debug=True, access_log=False)

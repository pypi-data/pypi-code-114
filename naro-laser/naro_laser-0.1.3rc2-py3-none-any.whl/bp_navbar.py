# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary
"""bp_navbar.py"""
import json
import random
import time
import logging

from datetime import datetime
from flask import (
    Blueprint, flash, g, redirect,
    render_template, request, url_for, Response
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db
from flaskr import my_globals as g  # 22.0107 충돌 아냐?
from flaskr import __about__
from flaskr import shared


def print2(*s):
    print(__name__, 'debug:', *s)


lg = logging.getLogger('mylog')
lg.setLevel(logging.DEBUG)
lg.info('logger test, ' + time.asctime())

# lg = logging.getLogger('th_func2')
# lg.propagate = 0
# lg.setLevel(logging.DEBUG)
# lg.critical('---')
# lg.info(time.asctime())

bp = Blueprint('navbar', __name__)


@bp.route('/')  # __init__.py 도 참고하라.
@bp.route('/navbar')
@bp.route('/navbar/index')
def index():
    return render_template(
        '/navbar/index.html',
        title='My Navbar Index',
        message=g.hostname)


@bp.route('/navbar/status')
def status():
    about = [__about__.__title__, __about__.__build_date__, __about__.__version__]

    s1 = render_template(
        '/navbar/status.html',
        s_hostname=g.hostname,
        s_time=str(g.adc_time),
        s_time_diff=str(g.adc_time_diff),
        s_adc=str(g.adc_data),
        s_adc_mean=str(g.adc_data_mean),
        s_config=str(g.cnfg),
        s_status=str(g.status),
        s_env=str(g.env),
        s_peri=str(g.peri),
        s_about=str(about),

    )
    return s1


@bp.route('/navbar/hello')
def hello():
    s1 = render_template('/navbar/hello.html')
    return s1


@bp.route('/navbar/config', methods=['GET', 'POST'])
def config():
    """병아리, 닭 문제가 발생한다"""
    if request.method == 'POST':
        dic = request.form.to_dict()
    elif request.method == 'GET':
        dic = request.args.to_dict()
    else:
        dic = {}
        pass

    if dic:  # 폼에서 가져온 데이터가 있다면
        print2('GET/POST dic:', dic)
        lg.info('GET/POST request, ' + str(dic))

        if 'cmd_cnfgfile' in dic:
            if dic['cmd_cnfgfile'] == 'Save':
                print2('Save')
                shared.config_from_to_file(cmd='save', cnfg=g.cnfg)
            elif dic['cmd_cnfgfile'] == 'Load':
                print2('Load')
                shared.config_from_to_file(cmd='load', cnfg=g.cnfg)
            elif dic['cmd_cnfgfile'] == 'Delete':
                print2('Delete')
                shared.config_from_to_file(cmd='delete', cnfg=g.cnfg)
            else:
                print2('unknown command key')
        else:
            if 'sample_period' in dic:
                g.cnfg['sample']['period'] = float(dic['sample_period'])
            if 'sample_size' in dic:
                g.cnfg['sample']['size'] = int(dic['sample_size'])
            if 'log_max' in dic:
                g.cnfg['log']['max'] = int(dic['log_max'])
            if 'proc_method' in dic:
                g.cnfg['proc']['method'] = dic['proc_method']
            if 'sse_period' in dic:
                g.cnfg['sse']['period'] = float(dic['sse_period'])
            else:
                print2('unknown config key')

    return render_template(
        '/navbar/config.html',
        sample_period=g.cnfg['sample']['period'],
        sample_size=g.cnfg['sample']['size'],
        log_max=g.cnfg['log']['max'],
        proc_method=g.cnfg['proc']['method'],
        sse_period=g.cnfg['sse']['period'],
    )


@bp.route('/navbar/config-test', methods=['GET', 'POST'])
def config_test():
    """UI Control test"""
    return render_template(
        '/navbar/config-test.html',
    )


@bp.route('/navbar/miniweb', methods=['GET', 'POST'])
def miniweb():
    """mini web test"""
    return 'hello, miniweb'

    # return render_template(
    #     '/navbar/config-test.html',
    # )


@bp.route('/navbar/chart')
def chart():
    return render_template('/navbar/chart.html')


@bp.route('/chart-data')
def chart_data():
    def get_data():
        while True:
            now = datetime.now().strftime('%H:%M:%S-%f')  # OR
            # now = g.adc_time[0]
            # value = random.random()*100 # OR
            value = g.adc_data[0]
            json_data = json.dumps({'time': now, 'value': value, 'temp': g.status['cpu_temp']})
            yield f"data:{json_data}\n\n"
            time.sleep(g.cnfg['sse']['period'])  #

    return Response(get_data(), mimetype='text/event-stream')

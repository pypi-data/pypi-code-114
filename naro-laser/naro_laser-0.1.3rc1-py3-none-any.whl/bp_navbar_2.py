# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary






"""bp_navbar_2.py"""
import json
import random
import time
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

import logging

lg = logging.getLogger('mylog')
lg.setLevel(logging.DEBUG)
lg.info('logger test, ' + time.asctime())

bp = Blueprint('navbar_2', __name__)


@bp.route('/')  # __init__.py 도 참고하라.
@bp.route('/navbar_2')
@bp.route('/navbar_2/index')
def index():
    return render_template(
        '/navbar_2/index.html',
        title='My Navbar_2 Index',
        message=g.hostname)


@bp.route('/navbar_2/status')
def status():
    about = [__about__.__title__, __about__.__build_date__, __about__.__version__]

    s1 = render_template(
        '/navbar_2/status.html',
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


@bp.route('/navbar_2/hello')
def hello():
    s1 = render_template('/navbar_2/hello.html')
    return s1


@bp.route('/navbar_2/data', methods=['GET', 'POST'])
def data():
    """IPC, socket"""
    s1 = f'adc_data:{g.adc_data}'
    d1 = g.ipc

    return d1


@bp.route('/navbar_2/config', methods=['GET', 'POST'])
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
        lg.info('GET/POST request, ' + str(g.cnfg))

        g.cnfg['sample']['period'] = float(dic['sample_period'])
        g.cnfg['sample']['size'] = int(dic['sample_size'])
        g.cnfg['log']['max'] = int(dic['log_max'])
        g.cnfg['proc']['method'] = dic['proc_method']

    return render_template(
        '/navbar_2/config.html',
        sample_period=g.cnfg['sample']['period'],
        sample_size=g.cnfg['sample']['size'],
        log_max=g.cnfg['log']['max'],
        proc_method=g.cnfg['proc']['method']
    )


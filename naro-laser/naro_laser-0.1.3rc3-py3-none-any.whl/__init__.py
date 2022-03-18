# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

# 가장 먼저 실행되는 곳

print('\n\n======================')
print('<-', __name__, 'pkg init')
print('======================')

import logging
import os
import time
import socket

from flask import Flask

from flaskr import my_logging
from flaskr import my_thread3

# 플라스크 인스턴스 생성 전에 새 쓰레드 실행한다.
my_thread3.create_threads()


def create_app(test_config=None):
    """create app
    튜토리얼을 따라 입력하다
    템플릿으로 보아서는 안된다 직접 작성한 코드로 보아야 한다
    초기화 작업을 여기에 직접 넣는 것이 논리적이다
    """
    print('create_app() start')

    app = Flask(__name__, instance_relative_config=True)

    '''다음 함수는 연구가 더 필요하다
    from_file()에서 얻어지 데이터는 이 함수로 전달된다고 한다
    무슨 말인지... '''
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
        MY_TEST='test-21.09-nash'
    )

    # print('config:', app.config.keys())
    # logging.info(app.config.keys())

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    '''
    for added function, nash
    '''
    # Added for DB
    from . import db
    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    # app.add_url_rule('/', endpoint='index')   # 루트에서 제거한다. 21.10
    app.add_url_rule('/blog', endpoint='index')

    # from . import bp_dashboard      # 오래전부터 사용되지 않는다. 22.01
    # app.register_blueprint(bp_dashboard.bp)
    # app.add_url_rule('/dashboard', endpoint='index')

    from . import bp_navbar
    app.register_blueprint(bp_navbar.bp)
    app.add_url_rule('/navbar', endpoint='index')
    # app.add_url_rule('/', endpoint='index')
    # 루트 자격을 추가한다. 21.10,
    # bp_navbar.py 에 있으므로 위 작업은 필요없다.

    from . import bp_navbar_2
    app.register_blueprint(bp_navbar_2.bp)
    app.add_url_rule('/navbar_2', endpoint='index')

    print('create_app() end')
    return app

# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary
"""설정
작업 기록
21.09, 로깅설정을 json 파일로부터 읽어들이는 방식으로 변경
21.1004,
    스트림 핸들러 부분: 설정파일로부터
    파일 핸들러 부분: 소스파일 내에서 작성하기로 변경
"""
print('<-', __name__)

import logging
import logging.config
import json
import socket
import time


# if True:
def init_logger_old():
    """파일 기반 방식이다. 그런데 불편하다. 제거하자. 21.11
    """
    # sys.path.append('flaskr') # testing...
    # print(sys.path)
    # with open('.//flaskr//log_config.json', 'rt') as f:    # pycharm: OK

    print('\n\n*** logging config start')
    with open('config_log.json', 'rt') as f:  # pkg???
        config = json.load(f)
        print('--- logging config load')
    logging.config.dictConfig(config)
    # pprint.pprint(config)
    print('*** logging config end')

    '''로그 파일 폴더 및 이름'''
    prefix = './/log//'
    # prefix += time.strftime('%Y.%m%d.%H%M-')
    # prefix += time.strftime('%d.%H%M-')
    prefix += time.strftime('00-')  # 임시로...
    prefix += socket.gethostname()

    sf1 = '%(name)s:%(levelname)s:%(message)s'
    sf2 = '%(asctime)s:%(name)s:%(levelname)s:%(message)s'

    lg = logging.getLogger()
    f_h = logging.FileHandler(prefix + '-root.log', 'w')
    f_h.setFormatter(logging.Formatter(sf2))
    lg.addHandler(f_h)

    lg = logging.getLogger('th_func2')
    f_h = logging.FileHandler(prefix + '-th_func2.log', 'w')
    f_h.setFormatter(logging.Formatter(sf1))
    lg.addHandler(f_h)

    lg = logging.getLogger('th_func3')
    f_h = logging.FileHandler(prefix + '-th_func3.log', 'w')
    f_h.setFormatter(logging.Formatter(sf1))
    lg.addHandler(f_h)

    lg = logging.getLogger('hardware')
    f_h = logging.FileHandler(prefix + '-hardware.log', 'w')
    f_h.setFormatter(logging.Formatter(sf1))
    lg.addHandler(f_h)

    # logger test
    '''아래 테스트 결과는 이상하다
    이모듈에서는 정상인데 
    다른 모듈에서 로거를 호출하면 파일로그는 정상, 스트림로그는 불량이 된다 21.10'''

    lg = logging.getLogger('root')
    # logger_test(lg)

    # lg = logging.getLogger('my')
    # logger_test(lg)

    # lg = logging.getLogger('th_func2')
    # logger_test(lg)

    # lg = logging.getLogger('th_func3')
    # logger_test(lg)
    #
    # lg = logging.getLogger('hardware')
    # logger_test(lg)


def init_logger():
    """
        첫 로그파일을 원하는 위치에 생성한다.
    """

    def logger_test(logger, msg=None):
        logger.critical('=== logger output test start ===')
        txt = 'Hello, sample text...!!!'
        logger.error(txt)
        logger.warning(txt)
        logger.info(txt)
        logger.debug(txt)
        logger.info(time.asctime())
        logger.critical('=== logger setup test end ===')

    '''로그 파일 폴더 및 이름'''
    prefix = './/log//'
    prefix += time.strftime('0000-')  # 임시로...
    prefix += socket.gethostname()

    sf1 = '%(name)s:%(levelname)s:%(message)s'
    sf2_time = '%(asctime)s:%(name)s:%(levelname)5s: %(message)s'

    lg = logging.getLogger('mylog')
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(prefix + '-mylog.log', 'w')
    s_h.setFormatter(logging.Formatter(sf2_time))
    f_h.setFormatter(logging.Formatter(sf2_time))
    # lg.addHandler(s_h)
    lg.addHandler(f_h)
    lg.setLevel(logging.DEBUG)

    lg = logging.getLogger('th_func2')
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(prefix + '-th_func2.log', 'w')
    s_h.setFormatter(logging.Formatter(sf2_time))
    f_h.setFormatter(logging.Formatter(sf2_time))
    # lg.addHandler(s_h)    # 로그데이터이므로 화면출력에서는 제외
    lg.addHandler(f_h)
    lg.setLevel(logging.DEBUG)

    '''
    lg = logging.getLogger('th_func3')
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(prefix + '-th_func3.log', 'w')
    s_h.setFormatter(logging.Formatter(sf2_time))
    f_h.setFormatter(logging.Formatter(sf2_time))
    # lg.addHandler(s_h)    #
    lg.addHandler(f_h)
    lg.setLevel(logging.DEBUG)'''

    lg = logging.getLogger('hardware')
    s_h = logging.StreamHandler()
    f_h = logging.FileHandler(prefix + '-hardware.log', 'w')
    s_h.setFormatter(logging.Formatter(sf2_time))
    f_h.setFormatter(logging.Formatter(sf2_time))
    # lg.addHandler(s_h)    # 문제가 있으면 로그파일에서 확인하자
    lg.addHandler(f_h)
    lg.setLevel(logging.DEBUG)

    # logger test
    '''
    아래 테스트 결과는 이상하다
    이모듈에서는 정상인데 
    다른 모듈에서 로거를 호출하면 파일로그는 정상, 스트림로그는 불량이 된다 21.10
    한곳에서 스트림핸들러 파일핸들러 추가하고 레벨 정하니 된다 21.11
    '''
    if not True:
        lg = logging.getLogger('mylog')
        logger_test(lg)

        lg = logging.getLogger('th_func2')
        logger_test(lg)

        lg = logging.getLogger('th_func3')
        logger_test(lg)

        lg = logging.getLogger('hardware')
        logger_test(lg)


'''전략이 자주 왔다갔다 하고있다'''

init_logger()

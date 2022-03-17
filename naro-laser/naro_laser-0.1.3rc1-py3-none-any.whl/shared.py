# Copyright (c) 2021, 2022 Narotechnology, nash@narotechnology.com
# SPDX-License-Identifier: LicenseRef-Narotechnology-Proprietary

import json
import logging

# from flaskr import my_globals as gm
import os

mylog = logging.getLogger('mylog')


def print2(*s):
    print(__name__, 'debug:', *s)


def config_from_to_file(cmd, cnfg):
    """앱 설정을 파일에 쓰거나 불러오기"""
    conf_filename = 'config_app.json'
    # dic = cnfg

    if cmd is 'save':
        # dic --> json
        jo = json.dumps(cnfg, ensure_ascii=True)  # 한글금지

        try:
            # 'wt' 를 사용하면 더러워진다 그리고 숫자를 스트링 처리한다
            with open(conf_filename, 'w') as f:  # with: 파일닫기를 자동으로
                # json --> file
                json.dump(jo, f)  # indent 안먹힌다
                print2('save config to file:', jo)
        except:
            print2('failed to write to file')

    if cmd is 'load':
        try:
            with open(conf_filename, 'r') as f:
                # file --> json
                jo = json.load(f)
                mylog.info('load config from file:' + str(jo))

                # json --> python dic
                dic = json.loads(jo)
                cnfg = dic
                print2('default global config values replaced')
        except:
            print2('no config file found')

    if cmd is 'delete':
        try:
            os.remove(conf_filename)
            print2('file deleted')
        except:
            print2('failed to delete file')


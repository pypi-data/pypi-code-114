import os
import sys
import re
import datetime
import argparse

from util_hj3415 import noti
from dart_hj3415 import opendart
from db_hj3415 import mongo2, dbpath

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


# from tendo import singleton

# reference from http://seorenn.blogspot.com/2011/12/python.html
# 인스턴스를 한번만 실행하기
# me = singleton.SingleInstance()

present_addr = dbpath.load()
client = mongo2.connect_mongo(present_addr)

if __name__ == '__main__':
    # reference form https://docs.python.org/3.3/howto/argparse.html#id1
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help=f"save_by_date, refresh_set_count")
    parser.add_argument('-d', '--date', metavar='date', help='Set report date(yyyymmdd)')
    parser.add_argument('-m', '--message', action='store_true', help='Send telegram message with result after work.')

    args = parser.parse_args()

    # -d 인자를 입력하면 해당날짜의 dart를 수집하고 생략하면 오늘날짜를 수집한다.
    if args.date:
        # 날짜입력이 형식에 맞는지 정규표현식으로 확인한다.
        p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
        if p.match(args.date) is None:
            print(f'Invalid date - {args.date}(YYYYMMDD)')
            sys.exit()
        else:
            date = args.date
    else:
        date = datetime.datetime.today().strftime('%Y%m%d')

    if args.cmd == 'save_by_date':
        df = opendart.Dart(client).make_df(edate=date)
        mongo2.DartWithDate(client, date).save_df(df)
        if args.message:
            noti.telegram_to(botname='manager',
                             text=f'>>> python {os.path.basename(os.path.realpath(__file__))} {args.cmd}\n'
                                  f'date : {date}\titems : {len(df)}')
    elif args.cmd == 'refresh_set_count':
        # dart중 해당날짜의 분기, 반기, 사업보고서를 검색하여 데이터베이스에 회사코드와 카운터, 날짜를 저장한다.
        # 하루에 한번만 실행한다. 반복실행하면 카운터가 계속 10으로 리셋된다.
        len_corp_refresh_table = opendart.Dart(client).set_refresh_count(date)
        if args.message:
            noti.telegram_to(botname='manager',
                             text=f'>>> python {os.path.basename(os.path.realpath(__file__))} {args.cmd}\n'
                                  f'total items : {len_corp_refresh_table}')
    else:
        parser.print_help()

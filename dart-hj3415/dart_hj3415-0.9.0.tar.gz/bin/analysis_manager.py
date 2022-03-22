import os
import sys
import re
import datetime
import argparse

from dart_hj3415 import analysis
from util_hj3415 import noti

import logging
logger = logging.getLogger(__name__)
formatter = logging.Formatter('%(levelname)s: [%(name)s] %(message)s')
ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
logger.setLevel(logging.WARNING)


if __name__ == '__main__':
    # reference form https://docs.python.org/3.3/howto/argparse.html#id1
    parser = argparse.ArgumentParser()
    parser.add_argument('cmd', help=f"run, run_today, run_1da")
    parser.add_argument('-d', '--date', metavar='date', help='Set report date(yyyymmdd)')
    parser.add_argument('-m', '--message', action='store_true', help='Send telegram message with result after work.')

    args = parser.parse_args()

    if args.cmd == 'run':
        if args.date:
            # 날짜입력이 형식에 맞는지 정규표현식으로 확인한다.
            p = re.compile('^20[0-9][0-9][0,1][0-9][0-3][0-9]$')
            if p.match(args.date) is None:
                print(f'Invalid date - {args.date}(YYYYMMDD)')
                sys.exit()
            else:
                analysis.run_all_subjects(args.date)
        else:
            print(f'Option run need to set date.')
            sys.exit()
    elif args.cmd == 'run_today':
        date = datetime.datetime.today().strftime('%Y%m%d')
        s_min, s_sec = divmod(analysis.run_all_subjects(date), 60)
        if args.message:
            noti.telegram_to(botname='manager',
                             text=f'>>> python {os.path.basename(os.path.realpath(__file__))} {args.cmd}\n'
                                  f'spent time : {s_min}m {s_sec}s')
    elif args.cmd == 'run_1da':
        date = (datetime.datetime.today() - datetime.timedelta(days=1)).strftime('%Y%m%d')
        s_min, s_sec = divmod(analysis.run_all_subjects(date), 60)
        if args.message:
            noti.telegram_to(botname='manager',
                             text=f'>>> python {os.path.basename(os.path.realpath(__file__))} {args.cmd}\n'
                                  f'spent time : {s_min}m {s_sec}s')
    else:
        parser.print_help()

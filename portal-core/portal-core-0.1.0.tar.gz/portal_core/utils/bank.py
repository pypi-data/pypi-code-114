""" utils/bank.py

銀行営業日関係の処理ユーティリティ
"""
import datetime

import jpholiday
from dateutil.relativedelta import relativedelta


def get_bank_openday(target_date):
    """ 指定日から最寄りの銀行営業日を取得 """
    # 銀行法施行令により、12/31〜1/3が年末年始の銀行休日となる
    if datetime.date(target_date.year, 12, 31) <= target_date <= datetime.date(target_date.year + 1, 1, 3):
        # 前営業日
        if target_date.month == 1:
            date_earlier = datetime.date(target_date.year - 1, 12, 30)
        else:
            date_earlier = datetime.date(target_date.year, 12, 30)
        # 翌営業日
        date_later  = datetime.date(target_date.year + 1, 1, 4)
    else:
        date_earlier = target_date
        date_later = target_date

    # 土日祝日の場合は前営業日に飛ばす。
    while date_earlier.isoweekday() in (6, 7) or jpholiday.is_holiday(date_earlier):
        date_earlier -= datetime.timedelta(days=1)

    # 土日祝日の場合は翌営業日に飛ばす。
    while date_later.isoweekday() in (6, 7) or jpholiday.is_holiday(date_later):
        date_later += datetime.timedelta(days=1)
    return (date_earlier, date_later)


def get_bank_openday_earlier(target_date):
    """ 前営業日のみ """
    return get_bank_openday(target_date)[0]


def get_bank_openday_later(target_date):
    """ 翌営業日のみ """
    return get_bank_openday(target_date)[1]

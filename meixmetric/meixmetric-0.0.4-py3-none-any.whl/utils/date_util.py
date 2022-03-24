import datetime

import pandas as pd

from meixmetric.exc.mx_exc import BizException

ALL_DATE_PERIOD = ['cm', 'cq', 'cy', '1w', '1m', '3m', '6m', '1y', '2y', '3y', '5y', 'all']


def calc_date(date: datetime.datetime, period: str, bdate: datetime.datetime) -> datetime.datetime:
    if period == 'cm':
        # 本月
        return datetime.datetime(date.year, date.month, 1) - pd.DateOffset(days=1)
    if period == 'cq':
        # 本季
        return datetime.datetime(date.year, date.month - (date.month - 1) % 3, 1) - pd.DateOffset(days=1)
    if period == 'cy':
        # 本年
        return datetime.datetime(date.year, 1, 1) - pd.DateOffset(days=1)
    if period == '1w':
        return date - pd.DateOffset(days=7)
    if period == '1m':
        return date - pd.DateOffset(months=1)
    if period == '3m':
        return date - pd.DateOffset(months=3)
    if period == '6m':
        return date - pd.DateOffset(months=6)
    if period == '1y':
        return date - pd.DateOffset(years=1)
    if period == '2y':
        return date - pd.DateOffset(years=2)
    if period == '3y':
        return date - pd.DateOffset(years=3)
    if period == '5y':
        return date - pd.DateOffset(years=5)
    if period == 'all':
        return bdate
    else:
        raise BizException("period错误")

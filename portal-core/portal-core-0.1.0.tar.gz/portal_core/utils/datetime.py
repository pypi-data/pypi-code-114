import calendar
import datetime

from django.utils import timezone

from dateutil.relativedelta import relativedelta


def get_nth_weekday(year, month, weekday, n):
    """ 指定年月の第n曜日の日付を取得する

    :param int year: year
    :param int month: month [1-12]
    :param int weekday: weekday [0-6] 0:Mon ... 6:Sun
    :param int n: nth
    :rtype: datetime.date
    :return: date

    """
    if not (1 <= month <= 12 > 12 or 0 <= weekday <= 6):
        raise ValueError

    month_days = calendar.Calendar().monthdatescalendar(year, month)
    days = [d[weekday] for d in month_days if d[weekday].month == month]

    if 0 < n <= len(days):
        return days[n-1]
    else:
        raise ValueError


def get_month_last(obj):
    """ 月末日を取得

    :param datetime.date obj: obj
    :rtype: datetime.date
    :return: date

    """
    if isinstance(obj, datetime.datetime):
        _date_obj = timezone.make_aware(obj).date
    elif isinstance(obj, datetime.date):
        _date_obj = obj
    else:
        raise ValueError
    return _date_obj - relativedelta(day=99)


def get_next_year_month(year, month):
    if month > 12 or month < 1:
        raise ValueError('月は、1〜12の間である必要があります。')

    if month == 12:
        year += 1
        month = 1
    else:
        month += 1
    return year, month


def get_prev_year_month(year, month):
    if month > 12 or month < 1:
        raise ValueError('月は、1〜12の間である必要があります。')

    if month == 1:
        year -= 1
        month = 12
    else:
        month -= 1
    return year, month

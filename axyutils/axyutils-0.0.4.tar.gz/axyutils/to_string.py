'''
Convert something to string.

XXX deep alpha

Initially it was for date/time.
XXX must be an already invented wheel out there somewhere but I had no luck to find any so far

In python, date/time conversion is based on system locale and extremely inconvenient
for multilingual services.

:copyright: Copyright 2022 AXY axy@declassed.art
:license: BSD, see LICENSE for details.
'''

from datetime import datetime

def to_string(lang, something, **kvargs):

    converter_class = globals().get('_%s_to_string_%s' % (type(something).__name__, lang), None)
    if converter_class is None:
        # try en
        converter_class = globals().get('_%s_to_string_en' % type(something).__name__, None)
        if converter_class is None:
            return str(something)
    else:
        converter = converter_class()
        return converter.to_string(something, **kvargs)

class _date_to_string_en:

    def to_string(self, date, **kvargs):
        return '%s %s, %s' % (
            self.months[date.month],
            date.day,
            date.year
        )

    months = [0, 'January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December']

class _date_to_string_ru(_date_to_string_en):

    def to_string(self, date, **kvargs):
        return '%s %s, %s' % (
            date.day,
            self.months[date.month],
            date.year
        )

    months = [0, 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

class _datetime_to_string_en(_date_to_string_en):

    def to_string(self, datetime, **kvargs):
        return '%s %s, %s %s' % (
            self.months[datetime.month],
            datetime.day,
            datetime.year,
            '%2d:%02d' % (datetime.hour, datetime.minute)
        )

class _datetime_to_string_ru(_datetime_to_string_en, _date_to_string_ru):

    def to_string(self, datetime, **kvargs):
        return '%s %s, %s %s' % (
            datetime.day,
            self.months[datetime.month],
            datetime.year,
            '%2d:%02d' % (datetime.hour, datetime.minute)
        )

class _timedelta_to_string_en:

    def to_string(self, timedelta, **kvargs):
        seconds = timedelta.total_seconds()
        if seconds > (365 + 180) * 24 * 60 * 60:
            years = round(seconds / (365 * 24 * 60 * 60))
            return self.pattern % (years, self.get_years_ago(years))
        if seconds > (45 * 24 * 60 * 60):
            months = round(seconds / (45 * 60 * 60))
            return self.pattern % (months, self.get_months_ago(months))
        if seconds > (36  * 60 * 60):
            days = round(seconds / (45 * 60 * 60))
            return self.pattern % (days, self.get_days_ago(days))
        if seconds > (90 * 60):
            hours = round(seconds / (90 * 60))
            return self.pattern % (hours, self.get_hours_ago(hours))
        if seconds > (60):
            minutes = round(seconds / 60)
            return self.pattern % (minutes, self.get_minutes_ago(minutes))
        return self.just_now

    pattern = '%s %s ago'
    just_now = 'just_now'

    def get_years_ago(self, years):
        if years == 1:
            return 'year'
        else:
            return 'years'

    def get_months_ago(self, months):
        if months == 1:
            return 'month'
        else:
            return 'months'

    def get_days_ago(self, days):
        if days == 1:
            return 'day'
        else:
            return 'days'

    def get_hours_ago(self, hours):
        if hours == 1:
            return 'hour'
        else:
            return 'hours'

    def get_minutes_ago(self, minutes):
        if minutes == 1:
            return 'minute'
        else:
            return 'minutes'

class _timedelta_to_string_ru(_timedelta_to_string_en):

    pattern = '%s %s назад'
    just_now = 'только что'

    def get_years_ago(self, years):
        return {
            1: 'год',
            2: 'года',
            3: 'года',
            4: 'года'
        }.get(years % 10, 'лет')

    def get_months_ago(self, months):
        return {
            1: 'месяц',
            2: 'месяца',
            3: 'месяца',
            4: 'месяца'
        }.get(months % 10, 'месяцев')

    def get_days_ago(self, days):
        return {
            1: 'день',
            2: 'дня',
            3: 'дня',
            4: 'дня'
        }.get(days % 10, 'дней')

    def get_hours_ago(self, hours):
        return {
            1: 'час',
            2: 'часа',
            3: 'часа',
            4: 'часа'
        }.get(hours % 10, 'часов')

    def get_minutes_ago(self, minutes):
        return {
            1: 'минута',
            2: 'минуты',
            3: 'минуты',
            4: 'минуты'
        }.get(minutes % 10, 'минут')

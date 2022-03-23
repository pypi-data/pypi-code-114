from datetime import datetime, timedelta
from typing import Union


class SatDatetime:
    @staticmethod
    def get_from_datetime(date):
        delta = date - datetime(2017, 12, 25)
        convert = (delta.days + (delta.seconds + delta.microseconds / 1000000) / 86400) / 7 * 20
        return SatDatetime(convert)

    def __init__(self,
                 year: float, month: float = 1, day: float = 1,
                 hour: float = 0, minute: float = 0, second: float = 0):
        minute += second / 60
        hour += minute / 60
        day += -1 + hour / 24
        month += -1 + day / 22
        year += month / 8

        self.year = 1
        self.month = 1
        self.day = 1
        self.hour = 0
        self.minute = 0
        self.second = 0.0

        self.refresh_by_year(year)

    def __copy__(self):
        return SatDatetime(self.year, self.month, self.day, self.hour, self.minute, self.second)

    def __str__(self):
        """ A user-friendly string representation of SatTimedelta. """
        return f'{self.year}. {self.month}. {self.day:02d}. {self.hour:02d}:{self.minute:02d}:{self.second:09.6f}'

    def __repr__(self):
        """ A programmer-friendly string representation of SatTimedelta. """
        return f'SatDatetime({self.year}, {self.month}, {self.day}, {self.hour}, {self.minute}, {self.second})'

    def __add__(self, other: 'SatTimedelta') -> 'SatDatetime':
        """ Adds SatTimedelta object from self and returns new SatTimedelta object. """
        if isinstance(other, SatTimedelta):
            return SatDatetime(self.year + other.years, self.month + other.months, self.day + other.days,
                               self.hour + other.hours, self.minute + other.minutes, self.second + other.seconds)
        else:
            raise TypeError(f'SatDatetime can only be added to SatTimedelta, not {type(other)}')

    def __sub__(self, other: 'SatTimedelta') -> 'SatDatetime':
        """ Subtracts SatTimedelta object from self and returns new SatTimedelta object. """
        if isinstance(other, SatTimedelta):
            return SatDatetime(self.year - other.years, self.month - other.months, self.day - other.days,
                               self.hour - other.hours, self.minute - other.minutes, self.second - other.seconds)
        else:
            raise TypeError(f'SatDatetime can only be subtracted from SatTimedelta, not {type(other)}')

    def __mul__(self, other: float) -> 'SatDatetime':
        """ Multiplies SatTimedelta object by float and returns new SatTimedelta object. """
        return SatDatetime(self.year * other, self.month * other, self.day * other,
                           self.hour * other, self.minute * other, self.second * other)

    def __truediv__(self, other: float) -> 'SatDatetime':
        """ Divides SatTimedelta object by float and returns new SatTimedelta object. """
        return SatDatetime(self.year / other, self.month / other, self.day / other,
                           self.hour / other, self.minute / other, self.second / other)

    def __lt__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() < other.get_on_year()

    def __le__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() <= other.get_on_year()

    def __eq__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() == other.get_on_year()

    def __ne__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() != other.get_on_year()

    def __gt__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() > other.get_on_year()

    def __ge__(self, other: 'SatDatetime') -> bool:
        return self.get_on_year() >= other.get_on_year()

    def refresh_by_year(self, year):
        year, month = int(year), (year - int(year)) * 8
        month, day = int(month) + 1, (month - int(month)) * 22
        day, hour = int(day) + 1, (day - int(day)) * 24
        hour, minute = int(hour), (hour - int(hour)) * 60
        minute, second = int(minute), (minute - int(minute)) * 60
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.second = second

    def get_on_year(self):
        minute = self.minute + self.second / 60
        hour = self.hour + minute / 60
        day = self.day - 1 + hour / 24
        month = self.month - 1 + day / 22
        year = self.year + month / 8
        return year

    def to_datetime(self):
        c = self.get_on_year()
        days_plus = c / 20 * 7
        return datetime(2017, 12, 25) + timedelta(days=days_plus)


class SatTimedelta:
    def __init__(self,
                 years: float = 0, months: float = 0, days: float = 0,
                 hours: float = 0, minutes: float = 0, seconds: float = 0):
        self.years = years
        self.months = months
        self.days = days
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

        seconds = self.get_in_seconds()
        self.years = seconds // 15206400
        seconds -= self.years * 15206400
        self.months = seconds // 1900800
        seconds -= self.months * 1900800
        self.days = seconds // 86400
        seconds -= self.days * 86400
        self.hours = seconds // 3600
        seconds -= self.hours * 3600
        self.minutes = seconds // 60
        seconds -= self.minutes * 60
        self.seconds = seconds

    def __str__(self):
        return f'{self.days + self.months * 22 + self.years * 176:d} days, ' \
               f'{self.hours:d} hours {self.minutes:d} minutes {self.seconds} seconds'

    def __repr__(self):
        return f'SatTimedelta({self.years}, {self.months}, {self.days}, {self.hours}, {self.minutes}, {self.seconds})'

    def __add__(self, other: 'SatTimedelta') -> Union['SatTimedelta', SatDatetime]:
        if isinstance(other, SatTimedelta):
            return SatTimedelta(self.years + other.years, self.months + other.months, self.days + other.days,
                                self.hours + other.hours, self.minutes + other.minutes, self.seconds + other.seconds)
        elif isinstance(other, SatDatetime):
            return SatDatetime(self.years + other.year, self.months + other.month, self.days + other.day,
                               self.hours + other.hour, self.minutes + other.minute, self.seconds + other.second)
        else:
            raise TypeError(f'SatTimedelta can only be added to SatTimedelta or SatDatetime, not {type(other)}')

    def __sub__(self, other: 'SatTimedelta') -> 'SatTimedelta':
        if isinstance(other, SatTimedelta):
            return SatTimedelta(self.years - other.years, self.months - other.months, self.days - other.days,
                                self.hours - other.hours, self.minutes - other.minutes, self.seconds - other.seconds)
        else:
            raise TypeError(f'SatTimedelta can only be subtracted from SatTimedelta, not {type(other)}')

    def __mul__(self, other: float) -> 'SatTimedelta':
        return SatTimedelta(self.years * other, self.months * other, self.days * other,
                            self.hours * other, self.minutes * other, self.seconds * other)

    def __truediv__(self, other: float) -> 'SatTimedelta':
        return SatTimedelta(self.years / other, self.months / other, self.days / other,
                            self.hours / other, self.minutes / other, self.seconds / other)

    def __floordiv__(self, other: float) -> 'SatTimedelta':
        return SatTimedelta(self.years // other, self.months // other, self.days // other,
                            self.hours // other, self.minutes // other, self.seconds // other)

    def get_in_seconds(self):
        return self.seconds \
               + self.minutes * 60 \
               + self.hours * 3600 \
               + self.days * 86400 \
               + self.months * 1900800 \
               + self.years * 15206400

    def get_in_years(self) -> float:
        return self.get_in_seconds() / 15206400


if __name__ == '__main__':
    pass

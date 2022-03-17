"""
Copyright 2019 Goldman Sachs.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an
"AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied.  See the License for the
specific language governing permissions and limitations
under the License.
"""
import datetime as dt
from dateutil.parser import isoparse
import re
from typing import Optional, Union

__valid_date_formats = ('%Y-%m-%d',  # '2020-07-28'
                        '%d%b%y',    # '28Jul20'
                        '%d-%b-%y',  # '28-Jul-20'
                        '%d/%m/%Y')  # '28/07/2020


def encode_date_or_str(value: Optional[Union[str, dt.date]]) -> Optional[str]:
    return value.isoformat() if isinstance(value, dt.date) else value


def decode_optional_date(value: Optional[str]) -> Optional[dt.date]:
    if value is None:
        return value
    elif isinstance(value, str):
        return dt.datetime.strptime(value, '%Y-%m-%d').date()

    raise ValueError(f'Cannot convert {value} to date')


def decode_date_or_str(value: Union[dt.date, float, str]) -> Optional[Union[dt.date, str]]:
    if value is None or isinstance(value, dt.date):
        return value
    elif isinstance(value, float):
        # Assume it's an Excel date
        if value > 59:
            value -= 1  # Excel leap year bug, 1900 is not a leap year!
        return (dt.datetime(1899, 12, 31) + dt.timedelta(days=value)).date()
    elif isinstance(value, str):
        # Try the supported string date formats
        for fmt in __valid_date_formats:
            try:
                return dt.datetime.strptime(value, fmt).date()
            except ValueError:
                pass

        # Assume it's a tenor
        return value

    raise TypeError(f'Cannot convert {value} to date')


def encode_datetime(value: Optional[dt.datetime]) -> Optional[str]:
    if value is None:
        return value

    try:
        iso_formatted = value.isoformat(timespec='milliseconds')
    except TypeError:
        # Pandas Timestamp objects don't take timespec, will raise TypeError (as of 1.2.4)
        iso_formatted = value.isoformat()

    return iso_formatted if value.tzinfo else iso_formatted + 'Z'  # Make sure to be explict about timezone


def decode_datetime(value: Optional[Union[int, str]]) -> Optional[dt.datetime]:
    if value is None:
        return value
    if isinstance(value, int):
        return dt.datetime.fromtimestamp(value / 1000)
    elif isinstance(value, str):
        matcher = re.search('\\.([0-9]*)Z$', value)
        if matcher:
            sub_seconds = matcher.group(1)
            if len(sub_seconds) > 6:
                value = re.sub(matcher.re, '.{}Z'.format(sub_seconds[:6]), value)

        return isoparse(value)

    raise TypeError(f'Cannot convert {value} to datetime')


def decode_float_or_str(value: Optional[Union[float, int, str]]) -> Optional[Union[float, str]]:
    if value is None:
        return value
    elif isinstance(value, float):
        return value
    elif isinstance(value, int):
        return float(value)
    elif isinstance(value, str):
        if value.endswith('%'):
            return float(value[:-1]) / 100
        elif value.endswith('bp'):
            return float(value[:-2]) / 10000
        else:
            try:
                return float(value)
            except ValueError:
                # Assume it's a strike or similar, e.g. 'ATM'
                return value

    raise TypeError(f'Cannot convert {value} to float')


def decode_instrument(value: Optional[dict]):
    from gs_quant.instrument import Instrument
    return Instrument.from_dict(value) if value else None


def encode_dictable(o):
    return o if o is None else o.to_dict()

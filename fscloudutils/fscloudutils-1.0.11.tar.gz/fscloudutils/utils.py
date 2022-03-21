"""
This module holds various useful tools
"""

import traceback
from datetime import datetime


class NavParser:
    """ nav_reader is a class implementing methods to read .nav files in NMEA format """

    def __init__(self, path):
        """
        :param path:
        """
        super()
        self._points = []
        self._direction_true = []
        self._direction_mag = []
        self._speed_kmh = []
        self._time = None
        self.read_file(path)

    def read_file(self, path: str) -> None:
        """
        :param path:
        :return:
        """
        if not path.split('.')[-1] == 'nav':
            print('you should only use .nav file formats, please try again')
            return
        else:
            with open(path, 'r') as f:
                try:
                    read_data = f.read()
                except FileNotFoundError as e:
                    traceback.print_exc()
                    print(e.filename)
                    return
                read_data = read_data.split('$')
                for point in read_data:
                    try:
                        if 'GPGGA' in point and len(point.split(',')) > 6:  # taking only the relevant row
                            # and ensuring it has all the neccesary data by checking the length of the row
                            latBeforeConversion = float(point.split(',')[2])
                            longBeforeConversion = float(point.split(',')[4])

                            lat_dec = latBeforeConversion // 100
                            long_dec = longBeforeConversion // 100

                            lat_partial = ((latBeforeConversion / 100 - lat_dec) * 100) / 60
                            long_partial = ((longBeforeConversion / 100 - long_dec) * 100) / 60

                            final_lat = lat_dec + lat_partial
                            final_long = long_dec + long_partial

                            # if S then *-1
                            if point.split(',')[3] == 'S':
                                final_lat = final_lat * -1
                            if point.split(',')[5] == 'W':
                                final_long = final_long * -1

                            self._points.append([final_lat, final_long])

                            format_time = int(point.split(',')[1])
                            self._time = datetime(format_time[4:6] + 2000, format_time[2:4], format_time[0:2]).date()

                        if 'GNRMC' in point and len(point.split(',')) > 6:  # taking only the relevant row
                            # and ensuring it has all the neccesary data by checking the length of the row
                            data = point.split(',')
                            latBeforeConversion = float(data[3])
                            longBeforeConversion = float(data[5])
                            try:
                                self._speed_kmh.append(str(1.852 * float(data[7])))
                            except Exception:
                                pass
                            lat_dec = latBeforeConversion // 100
                            long_dec = longBeforeConversion // 100

                            lat_partial = ((latBeforeConversion / 100 - lat_dec) * 100) / 60
                            long_partial = ((longBeforeConversion / 100 - long_dec) * 100) / 60

                            final_lat = lat_dec + lat_partial
                            final_long = long_dec + long_partial

                            # if S then *-1
                            if point.split(',')[3] == 'S':
                                final_lat = final_lat * -1
                            if point.split(',')[5] == 'W':
                                final_long = final_long * -1

                            self._points.append([final_lat, final_long])

                        if 'GNVTG' in point:
                            try:
                                x = point.split(',')
                                if len(x) > 6:  # taking only the relevant row
                                    self._direction_true.append(x[1])
                                    self._direction_mag.append(x[3])
                                    self._speed_kmh.append(x[7])
                            except IndexError as ie:
                                traceback.print_exc()
                                continue

                        else:
                            continue
                    except ValueError as e:
                        pass

    def get_points(self) -> list:  # getter function
        """
        :return:
        """
        return self._points

    def get_speed(self):  # getter function
        """
        :return:
        """
        return self._speed_kmh

    def get_direction_mag(self):  # getter function
        """
        :return:
        """
        return self._direction_mag

    def get_direction_true(self):  # getter function
        """
        :return:
        """
        return self._direction_true

    def get_time(self):
        return self._time

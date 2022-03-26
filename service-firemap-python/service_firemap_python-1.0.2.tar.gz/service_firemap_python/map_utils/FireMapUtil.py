# -*- coding: utf-8 -*-
import math
from typing import List

from ..data.version1 import LocationV1
# from service_firemap_python.data.version1 import LocationV1


class FireMapUtil:
    """
    This is utility class that help works with coordinates and convert their to QTH locators
    """
    __append_loc = '00AA00AA'
    # mapping zoom to locator symbol
    __locator_sym = [10, 8, 6, 4, 2, 0]

    @staticmethod
    def compose_tile_loc_by_zoom(loc: str, zoom: int) -> str:
        index_of_append = 10 - (zoom * 2)
        full_loc = loc[0: index_of_append] + FireMapUtil.__append_loc[index_of_append - 2:]

        if full_loc == 'AA':
            full_loc += FireMapUtil.__append_loc

        return full_loc.upper()

    @staticmethod
    def get_loc_by_zoom(loc: str, zoom: int):
        return loc[0: FireMapUtil.__locator_sym[zoom]]

    @staticmethod
    def get_locator(location: LocationV1) -> str:
        """
        Convert lat, long to QTH locator

        :return: QTH locator with 10 symbols
        """

        alphabet: List[str] = 'A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z'.split(',')

        word = ''

        # first lvl AA-RR
        lon = location.long + 180
        lat = location.lat + 90
        lon1 = lon / 20
        lat1 = lat / 10
        word += alphabet[int(lon1)] + alphabet[int(lat1)]

        # second lvl 00-99
        lonR = lon - (int(lon1) * 20)
        latR = lat - (int(lat1) * 10)
        lon2 = lonR / 2
        lat2 = latR / 1
        word += str(int(lon2)) + str(int(lat2))

        # third lvl aa-xx
        lonR = lonR - (int(lon2) * 2)
        latR = latR - (int(lat2) * 1)
        lon3 = lonR * 12
        lat3 = latR * 24
        word += (alphabet[int(lon3)] + alphabet[int(lat3)])

        # fourth lvl 00-99
        lonR = lonR - (int(lon3) / 12)
        latR = latR - (int(lat3) / 24)
        lon4 = lonR * 120
        lat4 = latR * 240
        word += str(int(lon4)) + str(int(lat4))

        # fifth lvl AA-XX
        lonR = lonR - (int(lon4) / 120)
        latR = latR - (int(lat4) / 240)
        lon5 = lonR * 2880
        lat5 = latR * 5760
        word += alphabet[int(lon5)] + alphabet[int(lat5)]

        # correct special chars
        word = word.upper()
        locator = ''
        for index, char in enumerate(word):
            # if is digit
            if ord('0') - 1 <= ord(char) <= ord('9') + 1:
                # check number chars of loc
                if ord(char) - ord('0') >= 10:
                    char = '9'

                elif ord('9') - ord(char) >= 10:
                    char = '0'
            else:
                # if is char
                if ord('A') - 1 <= ord(char) <= ord('X') + 1:
                    if index == 0 or index == 1:
                        # check for first chars pair in loc
                        if ord(char) - ord('A') >= 18:
                            char = 'R'

                        elif ord('R') - ord(char) >= 18:
                            char = 'A'
                    else:
                        if ord(char) - ord('A') >= 24:
                            char = 'X'

                        elif ord('X') - ord(char) >= 24:
                            char = 'A'

            locator += char

        return locator

    @staticmethod
    def get_locator_coordinates(loc: str, zoom: int, invert_angles: bool = False) -> List[LocationV1]:
        symbol = FireMapUtil.__locator_sym[zoom]
        loc = loc.upper()

        # if it smallest zoom
        if symbol == 0:
            if invert_angles:
                return [LocationV1(lat=90, long=180), LocationV1(lat=-90, long=-180)]
            else:
                return [LocationV1(lat=90, long=-180), LocationV1(lat=-90, long=180)]

        append_loc = FireMapUtil.__append_loc[symbol - 2:]

        # calculate coordinates of corners
        left_bottom = FireMapUtil.locator_to_polar(
            loc[0: symbol - 2]
            + loc[symbol - 2: symbol - 1]
            + loc[symbol - 1: symbol]
            + append_loc
        )

        right_bottom = FireMapUtil.locator_to_polar(
            loc[0: symbol - 2]
            + chr(1 + ord(loc[symbol - 2]))
            + loc[symbol - 1: symbol]
            + append_loc
        )

        right_top = FireMapUtil.locator_to_polar(
            loc[0: symbol - 2]
            + chr(1 + ord(loc[symbol - 2]))
            + chr(1 + ord(loc[symbol - 1]))
            + append_loc
        )

        left_top = FireMapUtil.locator_to_polar(
            loc[0: symbol - 2]
            + loc[symbol - 2: symbol - 1]
            + chr(1 + ord(loc[symbol - 1]))
            + append_loc
        )

        if invert_angles:
            return [left_bottom, right_top]

        return [left_top, right_bottom]

    @staticmethod
    def locator_to_polar(loc: str) -> LocationV1:
        e = []
        loc = loc.upper()

        for i in range(10):
            e.append(ord(loc[i]) - 65)

        e[2] += 17
        e[3] += 17
        e[6] += 17
        e[7] += 17

        long = 20 * e[0] + 2 * e[2] + e[4] / 12 + e[6] / 120 + e[8] / 2880 - 180
        lat = 10 * e[1] + e[3] + e[5] / 24 + e[7] / 240 + e[9] / 5760 - 90

        return LocationV1(lat=lat, long=long)

    @staticmethod
    def calc_center_coordinates(of: LocationV1, to: LocationV1) -> LocationV1:
        to_rad = lambda c: c * math.pi / 180
        to_degree = lambda c: c * 180 / math.pi

        flat = to_rad(of.lat)
        flng = to_rad(of.long)
        tlat = to_rad(to.lat)
        tlng = to_rad(to.long)

        delta_long = tlng - flng
        x_modified = math.cos(tlat) * math.cos(delta_long)
        y_modified = math.cos(tlat) * math.sin(delta_long)

        center_lat = math.atan2(math.sin(flat) + math.sin(tlat),
                                math.sqrt((math.cos(flat) + x_modified) *
                                          (math.cos(flat) + x_modified) + y_modified * y_modified))

        center_long = flng + math.atan2(y_modified, math.cos(flat) + x_modified)

        center_lat = to_degree(center_lat)
        center_long = to_degree(center_long)

        return LocationV1(lat=center_lat, long=center_long)

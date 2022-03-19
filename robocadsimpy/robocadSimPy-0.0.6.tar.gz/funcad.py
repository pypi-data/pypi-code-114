import numpy as np
import math


class Funcad:
    COS15 = 0.965926
    COS30 = 0.866
    COS45 = 0.7071
    COS60 = 0.5
    COS75 = 0.258819
    PI = 3.1415926535

    @staticmethod
    def fmta(right: float, left: float, back: float) -> tuple:
        """
        From Motors To Axes
        :param right: Right motor speed
        :param left: Left motor speed
        :param back: Back motor speed
        :return: Axes speeds
        """
        x: float = (right - left) * Funcad.COS30
        y: float = (right + left) * Funcad.COS60 - back
        z: float = -right - left - back
        return x, y, z

    @staticmethod
    def fatm(x: float, y: float, z: float) -> tuple:
        """
        From Axes To Motors
        :param x: X speed
        :param y: Y speed
        :param z: Z speed
        :return: Motor speeds
        """
        r: float = (x / Funcad.COS30) - y + z
        l: float = (x / -Funcad.COS30) - y + z
        b: float = y * 2 + z
        return r, l, b

    @staticmethod
    def in_range(val: float, min_v: float, max_v: float) -> float:
        """
        Func that returns value in range min and max
        :param val: Value that needs to clip
        :param min_v: Min limit
        :param max_v: Max limit
        :return: Ranged value
        """
        return val if (val <= max_v) and (val >= min_v) else (min_v if val < min_v else max_v)

    @staticmethod
    def in_range_bool(val: float, min_v: float, max_v: float) -> bool:
        """
        Func that checks that value in range min and max
        :param val: Value that needs to check
        :param min_v: Min limit
        :param max_v: Max limit
        :return: Value in range
        """
        return (val <= max_v) and (val >= min_v)

    @staticmethod
    def transfunc_np(arr: np.ndarray, inp: float) -> float:
        """
        Numpy transfer function
        :param arr: Input 2D array like: [[-1, 0, 1, 2], [-15, 0, 15, 30]]
        :param inp: Input of value to conversion by transfer function
        :return: Output is conversed input
        """
        if inp <= arr[0, 0]:
            return arr[1, 0]
        elif inp >= arr[0, -1]:
            return arr[1, -1]
        else:
            n = np.argmax(arr[0] > inp) - 1
            return (arr[1, n + 1] - arr[1, n]) / (arr[0, n + 1] - arr[0, n]) * (inp - arr[0, n]) + arr[1, n]

    @staticmethod
    def reim_to_polar(x: float, y: float) -> tuple:
        """
        Converts the rectangular components of a complex number into its polar components.
        :param x: X
        :param y: Y
        :return: Polar components of a complex number
        """
        return math.sqrt(x * x + y * y), math.atan2(y, x)

    @staticmethod
    def polar_to_reim(r: float, theta: float) -> tuple:
        """
        Converts the polar components of a complex number into its rectangular components.
        :param r: R
        :param theta: Theta
        :return: Rectangular components
        """
        return r * math.cos(theta), r * math.sin(theta)

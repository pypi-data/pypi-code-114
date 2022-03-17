'''Utility functions.'''
import math


# Python 3.9 has `math.lcm`
def lcm_multiple(*numbers):
    if len(numbers) > 0:
        lcm = numbers[0]
        for n in numbers[1:]:
            lcm = lcm_single(lcm, n)
        return lcm
    else:
        return None


def lcm_single(a, b):
    """
    Least Common Multiple
    """
    if a == 0 and b == 0:
        return 0
    else:
        return int((a * b) / math.gcd(a, b))

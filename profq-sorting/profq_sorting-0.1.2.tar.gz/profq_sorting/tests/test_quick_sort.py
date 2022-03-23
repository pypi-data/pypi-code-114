import sys
sys.path.append("..")

from sorting.quick_sort import quick_sort
import random


def test():
    """Test a huge list
    """
    for _ in range(100):
        arr_sorted = [random.randint(-100, 100) for _ in range(random.randint(2, 100))]
        arr = arr_sorted.copy()

        quick_sort(arr_sorted, 0, len(arr_sorted) - 1)

        arr.sort()
        assert arr == arr_sorted

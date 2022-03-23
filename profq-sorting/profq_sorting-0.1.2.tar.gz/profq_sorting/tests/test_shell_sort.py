import sys
sys.path.append("..")

from sorting.shell_sort import shell_sort
import random


def test():
    """Test a huge list
    """
    for _ in range(100):
        arr_sorted = [random.randint(-100, 100) for _ in range(random.randint(2, 100))]
        arr = arr_sorted.copy()

        shell_sort(arr_sorted)

        arr.sort()
        assert arr == arr_sorted

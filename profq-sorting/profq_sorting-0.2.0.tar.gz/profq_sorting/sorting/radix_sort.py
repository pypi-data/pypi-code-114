import sys
sys.path.append("..")

from profq_sorting.sorting.counting_sort import counting_sort
from profq_sorting.helpers.max import get_max

def radix_sort(arr: list) -> list:
    """Sort a list using radix sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    # Get the max value
    max_value = get_max(arr)

    # Get the amount of digits (alternate)
    """
    digits = 1
    while max_value > 0:
        max_value /= 10
        digits += 1
    """
    
    place_value = 1
    output = arr

    value = max_value

    # Sort the array
    while value > 0:
        # Use counting sort
        output = counting_sort(output, 10, place_value)

        # Increase place value and decrease digits
        place_value *= 10
        value = max_value // place_value
    
    return output
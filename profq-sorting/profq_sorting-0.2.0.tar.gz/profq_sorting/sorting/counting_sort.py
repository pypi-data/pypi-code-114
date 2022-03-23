import sys
sys.path.append("..")

from profq_sorting.helpers.max import get_max


def counting_sort(arr: list, max_value: int = None, place_value: int = None) -> list:
    """Sort a list using counting sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    # Get the max value
    if max_value is None:
        max_value = get_max(arr) + 1

    # Set output array and count table
    output = [0] * size
    count = [0] * max_value

    # Count all the numbers
    for i in range(size):
        # Calculate the index for radix sort
        index = arr[i]
        if place_value is not None:
            index = (arr[i] // place_value) % 10
        
        count[index] += 1

    # Cumulative sum
    for i in range(1, max_value):
        count[i] += count[i - 1]

    # Fill the output array
    for i in range(size - 1, -1, -1):
        # Calculate the index for radix sort
        index = arr[i]
        if place_value is not None:
            index = (arr[i] // place_value) % 10

        count[index] -= 1
        # arr[i] is the current element
        # count[arr[i]] is thus the index of the element
        # output[count[arr[i]]] is thus the correct location
        output[count[index]] = arr[i]

    return output
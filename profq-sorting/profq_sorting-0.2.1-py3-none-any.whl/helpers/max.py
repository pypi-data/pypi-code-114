def get_max(arr: list) -> int:
    """Returns the maximum value in an list

    Args:
        arr (list): the list to find the value in

    Returns:
        int: the value itself
    """
    max_value = arr[0]
    for value in arr:
        if value > max_value:
            max_value = value
    return max_value
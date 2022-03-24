def insertion_sort(arr: list):
    """Sort a list using insertion sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    # Loop over all items
    for i in range(1, size):
        # Get the first unsorted element
        key = arr[i]
        # Index of last sorted element
        j = i - 1

        # While we haven't reached the end of the array
        # And the current sorted item is larger than the unsorted item
        while j >= 0 and arr[j] > key:
            # Move the sorted item to the right
            arr[j + 1] = arr[j]
            # Move back through the array
            j -= 1
        
        # Set the key to the position before the sorted element
        arr[j + 1] = key
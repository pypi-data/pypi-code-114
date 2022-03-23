def selection_sort(arr: list):
    """Sort a list using selection sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    # Loop over entire array
    for j in range(size - 1):
        # Set the current minimum index to j
        iMin = j

        # Loop over the unsorted array (starting at j + 1)
        for i in range(j + 1, size):
            # Change the minimum when the number is smaller
            if arr[i] < arr[iMin]:
                iMin = i

        # If they aren't the same
        # Swap the minimum and the first element in the unsorted array
        if iMin != j:
            arr[j], arr[iMin] = arr[iMin], arr[j]
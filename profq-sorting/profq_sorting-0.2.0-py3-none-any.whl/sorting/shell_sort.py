def shell_sort(arr: list):
    """Sort a list using shell sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    # Calculate the gap to sort the items
    gap = len(arr) // 2

    # While the gap isn't 0
    while gap > 0:
        # Set i to the first element
        i = 0
        # Set j to the element of the gap
        j = gap

        # Loop over all items from gap to arr end
        while j < len(arr):
            # If the ith element is greater, swap the items
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

            # Increase i index and j index to simulatiously
            # Moves both pointers at the same time
            i += 1
            j += 1

            # Set k to the index of the left selected element
            k = i

            # While k is greater than or equal to gap,
            # Make it smaller than gap
            while k >= gap:
                # Check for
                #  left element > right element
                if arr[k - gap] > arr[k]:
                    # Swap if true
                    arr[k - gap], arr[k] = arr[k], arr[k - gap]
                
                # Reduce k to keep it within gap
                k -= 1

        # Make gap smaller
        gap //= 2

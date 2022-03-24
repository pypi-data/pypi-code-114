MIN_MERGE = 32

def calc_minrun(size: int):
    """Calculates the minimum size of the runs for a certain number of items.

    Args:
        n (int): the number of items in the array
    """
    r = 0
    while size >= MIN_MERGE:
        r |= size & 1
        size >>= 1
    
    return size + r

def insertion_sort(arr: list, left: int, right: int) -> list:
    """Insertion sort from left index to right index
    Which is at most the size of a run

    Args:
        arr (list): the array to sort
        left (int): the left-most index to start from
        right (int): the right-most index to end from

    Returns:
        list: the sorted list
    """
    # Loop over all items in a run
    for i in range(left + 1, right + 1):
        # Set j equal to the current item
        j = i

        # While we haven't reached the end of the array (on the left)
        # And the item on the right is less than the item on the left
        while j > left and arr[j] < arr[j - 1]:
            # Swap the items and decrease j
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1


def merge(arr: list, left: int, middle: int, right: int):
    """Merge sorted runs

    Args:
        arr (list): the list to be merged
        left (int): the left index of the run
        middle (int): the middle of the run
        right (int): the right index of the run
    """
    # Calculate the length of the left array
    # index in the middle - the left-most index + 1
    left_arr_len = middle - left + 1
    # E.g. with array [0, 1, 2, 3] middle = 2, left = 0
    # 2 - 0 + 1 = 3 from 0 to 2

    # Calculate the length of the right array
    # right-most index - index in the middle
    right_arr_len = right - middle
    # E.g. with array [0, 1, 2, 3] middle = 2, right = 4
    # 4 - 2 = 2 from 3 to 4


    # Create the left and right arrays
    left_arr, right_arr = [], []

    # Add all left items to left array
    left_arr.extend(arr[left + i] for i in range(left_arr_len))
    # Add all items from the right to right array
    right_arr.extend(arr[middle + i + 1] for i in range(right_arr_len))

    # Setup some variables
    l_index, r_index, k = 0, 0, left

    # If there are still items left in both arrays
    # Merge the items
    while l_index < left_arr_len and r_index < right_arr_len:
        # If the left array item is less than the right array item
        if left_arr[l_index] <= right_arr[r_index]:
            # Set the next available item in the original array to the left item
            arr[k] = left_arr[l_index]
            l_index += 1
        else:
            # Set the next available item in the original array to the right item
            arr[k] = right_arr[r_index]
            r_index += 1
    
        # Increase the available array index
        k += 1
    
    # If there are just items left in the left array
    # Add them to the list
    while l_index < left_arr_len:
        arr[k] = left_arr[l_index]
        k += 1
        l_index += 1
    
    # If there are just items left in the right array
    # Add them to the list
    while r_index < right_arr_len:
        arr[k] = right_arr[r_index]
        k += 1
        r_index += 1


def timsort(arr: list):
    size = len(arr)

    # Calculate the minimum run size
    min_run = calc_minrun(size)

    # Sort each run using insertion sort
    for start in range(0, size, min_run):
        end = min(start + min_run - 1, size - 1)
        insertion_sort(arr, start, end)
    
    # Start merging from size run (or 32)
    # It will merge to form 64, then 128, 256 and so on...
    run_size = min_run
    while run_size < size:
        # Get the starting point of left sub array
        for left in range(0, size, 2 * run_size):
            # Calculate the middle
            # Get the minimum between the last array index and the left index + the run size
            middle = min(size - 1, left + run_size - 1)
            # Calculate the right
            # Get the minimum between the last array index and the left index + 2 * the run size
            # Left index + 2 * run size = the end of the run
            right = min(left + 2 * run_size - 1, size - 1)

            # Merge sub arrays:
            # arr[left..middle] & arr[middle+1..right]
            if middle < right:
                merge(arr, left, middle, right)

        run_size = 2 * run_size
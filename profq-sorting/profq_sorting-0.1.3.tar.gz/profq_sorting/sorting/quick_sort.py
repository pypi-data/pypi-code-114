def partition(arr: list, low: int, high: int) -> int:
    """Partition the array

    Args:
        arr (list): the array to partition
        low (int): the left-most index
        high (int): the right-most index

    Returns:
        int: the new pivot location
    """
    i = low - 1
    pivot = arr[high]

    # Swap the numbers of the right-most and left-most index
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Swap the right-most number with the pivot
    arr[i+1], arr[high] = arr[high], arr[i+1]

    return i + 1

def quick_sort(arr: list, low: int, high: int):
    if len(arr) == 1:
        return arr
    
    # If there is an array to be sorted
    if low < high:
        # Partition the array
        pivot_location = partition(arr, low, high)

        # Quicksort the partitions
        quick_sort(arr, low, pivot_location - 1)
        quick_sort(arr, pivot_location + 1, high)
def merge(arr1: list, arr2: list) -> list:
    """Merge two arrays for merge sort

    Args:
        arr1 (list): the first array
        arr2 (list): the second array

    Returns:
        list: the merged array
    """
    merged = []

    # Compare elements for both arrays
    while arr1 and arr2:
        if (arr1[0] > arr2[0]):
            merged.append(arr2[0])
            arr2.pop(0)
        else:
            merged.append(arr1[0])
            arr1.pop(0)
    
    # Either arr1 or arr2 is empty now
    # Empty arr1
    while arr1:
        merged.append(arr1[0])
        arr1.pop(0)
    
    # Empty arr2
    while arr2:
        merged.append(arr2[0])
        arr2.pop(0)
    
    return merged

def merge_sort(arr: list) -> list:
    """Sort a list using merge sort

    Args:
        arr (list): the list to be sorted

    Returns:
        list: the sorted list
    """
    size = len(arr)

    # End condition for recursion
    if (size == 1):
        return arr

    # Get the index to split the array in half
    index = size // 2

    # Get the two split arrays
    arr1 = arr[:index]
    arr2 = arr[index:]

    # Recursivly call merge sort
    arr1 = merge_sort(arr1)
    arr2 = merge_sort(arr2)

    # Merge the two arrays back together
    return merge(arr1, arr2)

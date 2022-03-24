import sys
sys.path.append("..")

from profq_sorting.sorting.insertion_sort import insertion_sort

def bucket_sort(arr: list) -> list:
    # This means there will be 10 buckets
    # From 0 up to 9
    # For 0.0 to 0.999999999...
    slot_num = 10

    # Create an array for each slot
    buckets = [[] for _ in range(slot_num)]

    # Fill the buckets
    for item in arr:
        # Calculate the index of the bucket
        # 0.9 -> 9
        # 0.3452 -> 3
        # Etc
        index = int(slot_num * item)
        # Add the item to the buckets index
        buckets[index].append(item)

    # Sort the buckets
    for i in range(slot_num):
        buckets[i] = insertion_sort(buckets[i])

    output = []

    for i in range(slot_num):
        output.extend(buckets[i])

    return output
    
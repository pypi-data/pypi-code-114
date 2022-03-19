from collections import defaultdict


def digit_map(x: int, func=list):
    return func(str(x))


def digit_counts(x: int):
    counts = defaultdict(int)
    for i in str(x):
        counts[i] += 1
    return counts
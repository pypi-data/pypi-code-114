"""Tests for the ptvpy.utils module."""


from ptvpy.utils import LazyMapSequence


def test_LazyMapSequence():
    counter = 0

    def func(item):
        nonlocal counter
        counter += 1
        return counter, item

    sequence = LazyMapSequence(func, list(range(10)), cache_size=2)
    assert sequence.cache_size == 2
    assert len(sequence) == 10

    assert sequence[0] == (1, 0)
    assert sequence[1] == (2, 1)
    # Two items are cached now, so the counter shouldn't increase
    assert sequence[0] == (1, 0)
    assert sequence[1] == (2, 1)

    # Accessing a third item overwrites the oldest entry at 0
    assert sequence[2] == (3, 2)
    assert sequence[1] == (2, 1)  # still in cache, counter is still 2
    assert sequence[0] == (4, 0)  # was overridden, counter is no longer 1
    assert sequence[2] == (5, 2)  # 2 was dropped from the cache

    # 0 and 2 are in the cache now
    assert sequence[0] == (4, 0)
    assert sequence[2] == (5, 2)

    info = sequence._get_item.cache_info()  # Finally check the actual cache object
    assert info.hits == 5
    assert info.misses == counter

    sequence.clear_cache()
    assert sequence[0] == (6, 0)
    assert sequence[2] == (7, 2)
    info = sequence._get_item.cache_info()
    assert info.hits == 0
    assert info.misses == 2

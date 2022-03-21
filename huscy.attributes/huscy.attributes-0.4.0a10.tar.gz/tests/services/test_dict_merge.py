import pytest

from huscy.attributes.services import _dict_merge


@pytest.fixture
def source_dict():
    return {
        'a': 1,
        'b': {
            'c': 2,
            'd': {'e': 3},
        },
        'f': {
            'g': 4,
            'h': {'i': 5},
        },
        'j': 6
    }


@pytest.mark.parametrize('merge_dict, expected_result', [
    (
        {'a': 100},
        {'a': 100, 'b': {'c': 2, 'd': {'e': 3}}, 'f': {'g': 4, 'h': {'i': 5}}, 'j': 6}
    ),  # change first level value
    (
        {'a': 100, 'j': 101},
        {'a': 100, 'b': {'c': 2, 'd': {'e': 3}}, 'f': {'g': 4, 'h': {'i': 5}}, 'j': 101}
    ),  # change multiple first level values
    (
        {'b': {'c': 100}},
        {'a': 1, 'b': {'c': 100, 'd': {'e': 3}}, 'f': {'g': 4, 'h': {'i': 5}}, 'j': 6}
    ),  # change second level value
    (
        {'b': {'c': 100}, 'f': {'g': 101}},
        {'a': 1, 'b': {'c': 100, 'd': {'e': 3}}, 'f': {'g': 101, 'h': {'i': 5}}, 'j': 6}
    ),  # change multiple second level values
    (
        {'b': {'d': {'e': 100}}},
        {'a': 1, 'b': {'c': 2, 'd': {'e': 100}}, 'f': {'g': 4, 'h': {'i': 5}}, 'j': 6}
    ),  # change third level value
    (
        {'b': {'d': {'e': 100}}, 'f': {'h': {'i': 101}}},
        {'a': 1, 'b': {'c': 2, 'd': {'e': 100}}, 'f': {'g': 4, 'h': {'i': 101}}, 'j': 6}
    ),  # change multiple third level values
    (
        {'a': 100, 'b': {'c': 101}, 'f': {'h': {'i': 102}}},
        {'a': 100, 'b': {'c': 101, 'd': {'e': 3}}, 'f': {'g': 4, 'h': {'i': 102}}, 'j': 6}
    ),  # change mixed level values
])
def test_dict_merge(source_dict, merge_dict, expected_result):
    _dict_merge(source_dict, merge_dict)

    assert source_dict == expected_result

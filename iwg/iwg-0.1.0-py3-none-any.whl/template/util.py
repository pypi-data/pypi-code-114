from collections.abc import Mapping


def update_dict(d: Mapping, other: Mapping):
    """Updates a dictionary recursively
    
    On collisions, value of `other` will be used."""

    for k, v in other.items():
        if isinstance(v, Mapping):
            d[k] = update_dict(d.get(k, {}), v)
        else:
            d[k] = v

    return d

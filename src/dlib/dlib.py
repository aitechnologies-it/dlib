from typing import Optional, Any
from flatten_dict import flatten, unflatten


def _get(d: dict, path: str) -> Optional[dict]:
    keys = path.split('.')
    keys.reverse()
    curr = d
    while keys and isinstance(curr, dict):
        k = keys.pop()
        curr = curr.get(k, None)
    if len(keys) > 0:
        return None
    return curr


def has(d: dict, path: str) -> bool:
    if not isinstance(d, dict) or d is None or d == {}:
        return False
    if not isinstance(path, str) or path is None or path == '':
        return False
    curr = _get(d, path)
    return curr is not None


def get(d: dict, path: str, default: Any = None):
    if not has(d, path):
        return default
    return _get(d, path)


def update(d: dict, path: str, value: Any):
    if not has(d, path):
        return d
    keys = tuple(path.split('.'))
    d_flat = flatten(d)
    d_flat[keys] = value
    return unflatten(d_flat)


def delete(d: dict, path: str):
    if not has(d, path):
        return d
    keys = tuple(path.split('.'))
    d_flat = flatten(d)
    del d_flat[keys]
    return unflatten(d_flat)
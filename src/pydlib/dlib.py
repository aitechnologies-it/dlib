from typing import Optional, Any
from flatten_dict import flatten, unflatten


DEFAULT_SEP = '.'


def _get(d: dict, path: str, sep: str) -> Optional[dict]:
    keys = path.split(sep)
    keys.reverse()
    curr = d
    while keys and isinstance(curr, dict):
        k = keys.pop()
        curr = curr.get(k, None)
    if len(keys) > 0:
        return None
    return curr


def has(d: dict, path: str, sep: str = DEFAULT_SEP) -> bool:
    if not isinstance(d, dict) or d is None or d == {}:
        return False
    if not isinstance(path, str) or path is None or path == '':
        return False
    curr = _get(d, path, sep)
    return curr is not None


def get(d: dict, path: str, sep: str = DEFAULT_SEP, default: Any = None):
    if not has(d, path, sep):
        return default
    return _get(d, path, sep)


def update(d: dict, path: str, value: Any, sep: str = DEFAULT_SEP):
    if not has(d, path, sep):
        return d
    keys = tuple(path.split(sep))
    d_flat = flatten(d)
    d_flat[keys] = value
    return unflatten(d_flat)


def delete(d: dict, path: str, sep: str = DEFAULT_SEP):
    if not has(d, path, sep):
        return d
    keys = tuple(path.split(sep))
    d_flat = flatten(d)
    del d_flat[keys]
    return unflatten(d_flat)
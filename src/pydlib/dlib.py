from typing import Optional, Any, Union
from flatten_dict import flatten, unflatten


DEFAULT_SEP = '.'


def _get(d: Union[dict, list], path: str, sep: str) -> Optional[Union[dict, list]]:
    keys = path.split(sep)
    keys.reverse()
    curr = d
    while keys and isinstance(curr, (dict, list)):
        k = keys.pop()
        if isinstance(curr, dict):
            curr = curr.get(k)
        else: # list
            curr = [get(el, k, sep) for el in curr]
            curr = [el for el in curr if el is not None]
    if len(keys) > 0:
        return None
    return curr


def has(d: Union[dict, list], path: str, sep: str = DEFAULT_SEP) -> bool:
    if not isinstance(d, (dict, list)) or d is None or d == {} or d == []:
        return False
    if not isinstance(path, str) or path is None or path == '':
        return False
    curr = _get(d, path, sep)
    return curr is not None


def get(d: Union[dict, list], path: str, sep: str = DEFAULT_SEP, default: Any = None):
    if not has(d, path, sep):
        return default
    return _get(d, path, sep)


def update(d: Union[dict, list], path: str, value: Any, sep: str = DEFAULT_SEP):
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
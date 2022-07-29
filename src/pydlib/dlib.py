from typing import Optional, Any, Union
from flatten_dict import flatten, unflatten


DEFAULT_SEP = '.'


def _get(d: Union[dict, list], path: str, sep: str, search_lists: bool):
    keys = path.split(sep)
    keys.reverse()
    curr = d
    while keys and (
        isinstance(curr, dict)
        or search_lists and isinstance(curr, list)
    ):
        k = keys.pop()
        if isinstance(curr, dict):
            curr = curr.get(k)
        elif search_lists:
            curr = [_get(el, k, sep=sep, search_lists=search_lists) for el in curr]
            curr = [el for el in curr if el is not None]
            curr = None if curr == [] else curr
    if len(keys) > 0:
        return None
    return curr


def has(d: Union[dict, list], path: str, sep: str = DEFAULT_SEP, search_lists: bool = True) -> bool:
    if search_lists:
        if not isinstance(d, (dict, list)) or d == {} or d == []:
            return False
    else:
        if not isinstance(d, dict) or d == {}:
            return False
    if not isinstance(path, str) or path is None or path == '':
        return False

    curr = _get(d, path, sep=sep, search_lists=search_lists)
    return curr is not None


def get(d: Union[dict, list], path: str, sep: str = DEFAULT_SEP, default: Any = None, search_lists: bool = True):
    if not has(d, path, sep=sep, search_lists=search_lists):
        return default
    return _get(d, path, sep=sep, search_lists=search_lists)


def update(d: dict, path: str, value: Any, sep: str = DEFAULT_SEP):
    if not has(d, path, sep):
        return d
    keys = tuple(path.split(sep))
    d_flat = flatten(d)
    d_flat[keys] = value
    return unflatten(d_flat)


def delete(d: dict, path: str, sep: str = DEFAULT_SEP):
    if not has(d, path, sep=sep):
        return d
    keys = tuple(path.split(sep))
    d_flat = flatten(d)
    del d_flat[keys]
    return unflatten(d_flat)
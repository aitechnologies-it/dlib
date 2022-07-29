# :yarn: pydlib [![Downloads](https://pepy.tech/badge/pydlib)](https://pepy.tech/project/pydlib)
The **py**thon **d**ictionary **lib**rary to get into complex nested python dictionary structures (e.g. json) in a safe and clean way. We take inspiration from Greek myth of Minotaur, where Ariadne with the help of a thread escaped the labyrinth with his beloved Theseus.

## Installation

To install **pydlib**, simply use `pip`:

```bash
$ pip install pydlib
```

or install from the repository:

```bash
$ git clone https://github.com/aitechnologies-it/dlib.git
$ cd dlib
$ python setup.py install
```

## Basic usage

### get()

You can **get** the value from a nested field, just by indicating the path to the nested sub-structure as follows:

```python
>>> import pydlib as dl

>>> dictionary = {
>>>   'path': {
>>>       'to': {
>>>          'nested': {
>>>             'field': 42
>>>           }
>>>        }
>>>    }
>>> }
>>> dl.get(dictionary, path='path.to.nested.field', default=0)
42
```

Instead, if the field we are looking for doesn't exists, or, if it exists but has a None value, then:

```python
>>> ...
>>> dl.get(dictionary, path='path.to.nested.nonexisting.field', default=0)
0
```

### has()

You can also test for a field simply calling:

```python
>>> import pydlib as dl

>>> dictionary = { ... }
>>> dl.has(dictionary, path='path.to.nested.field')
True
```

### update()

Furthermore, the **pydlib** comes with built-in functions to also **update** and **delete** fields. For example, to **update**:

```python
>>> import pydlib as dl

>>> dictionary = { ... }
>>> dl.update(dictionary, path='path.to.nested.field', value=1)
{
   'path': {
       'to': {
          'nested': {
             'field': 1
           }
        }
    }
}
```

### delete()

Instead, to **delete**:

```python
>>> import pydlib as dl

>>> dictionary = { ... }
>>> dl.delete(dictionary, path='path.to.nested.field')
{
   'path': {
       'to': {
          'nested': {}
        }
    }
}
```

### Type-safety

pydlib is **type safe**, in fact you don't have to manually check the type of inputs, **pydlib** does it for you:

```python
>>> import pydlib as dl

>>> res = dl.get("not a dictionary", path="nowhere", default=None)
>>> res is None
True
```

## Advanced features

### Custom separator

It may happen that a dictionary has a string key with `.` in it. In this case you should use a different separator:

```python
>>> import pydlib as dl

>>> d = {"a": {"b.c": 42}}

# Separator conflict
>>> dl.get(d, "a.b.c")
None

# This works!
>>> dl.get(d, "a/b.c", sep="/")
42
```

### Search inside lists

```has()``` and ```get()``` (but not ```update``` and ```delete```!) can handle lists. This means that, if a list is encountered, the search for the rest of the path continues for each element of the list. A few examples are needed:

- ```b``` is a list, get() will return a list with all dictionaries containing the rest of the path ```c.d```:

    ```python
    >>> d = {"a":
                {"b": [
                    {"c":   {"d":   1}}, # <-- this
                    {"bad": {"d":   2}},
                    {"c":   {"d":   3}}, # <-- this
                    {"c":   {"bad": 4}}
                ]
            }
        }

    >>> dl.get(d, "a.b.c.d")
    [1, 3]
    ```
- this works also for nested lists. In this case a nested list of matching depth is returned:

    ```python
    >>> d = {"a":
                {"b": [
                    {"c":
                        {"d": [
                            {"e":   1},
                            {"e":   2},
                            {"bad": 3},
                        ]}
                    },
                    {"bad":
                        {"d": [
                            {"e":   4},
                        ]}
                    },
                    {"c":
                        {"d": [
                            {"e": 5},
                        ]}
                    },
                ]
            }
        }

    >>> dl.get(d, "a.b.c.d.e")
    [[1, 2], [5]]
    ```

- In this case the elements of list ```b``` are of different types, ```(1)``` and ```(3)``` are dictionaries, ```(2)``` is a list:
    ```python
    >>> d = {"a":
                {"b": [
                    {"c": {"d": 1}},     # (1)
                    [ {"c": {"d": 3}} ], # (2)
                    {"c": {"d": 4}},     # (3)
                ]
            }
        }

    >>> dl.get(d, "a.b.c.d")
    [1, [3], 4]
    ```

- Handling of lists can be disabled by setting ```search_lists=False```. Here's different behaviours for ```search_lists```:
    ```python
    >>> d = {"a":
                {"b": [
                    {"c":   {"d":   1}},
                    {"bad": {"d":   2}},
                    {"c":   {"d":   3}},
                    {"c":   {"bad": 4}}
                ]
            }
        }

    >>> print(dl.get(d, "a.b.c.d", search_lists=True))
    [1, 3]
    >>> print(dl.get(d, "a.b.c.d", search_lists=False))
    None

    # But if instead we want to get `a.b`, no lists are traversed and both return the value of `b`
    >>> print(dl.get(d, "a.b", search_lists=True))
    [{'c': {'d': 1}}, [{'c': {'d': 3}}], {'c': {'d': 4}}]
    >>> print(dl.get(d, "a.b", search_lists=False))
    [{'c': {'d': 1}}, [{'c': {'d': 3}}], {'c': {'d': 4}}]
    ```

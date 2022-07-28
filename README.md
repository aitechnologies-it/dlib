# :yarn: pydlib [![Downloads](https://pepy.tech/badge/pydlib)](https://pepy.tech/project/pydlib)
The **py**thon **d**ictionary **lib**rary to get into complex nested python dictionary structures (e.g. json) in a safe and clean way. We take inspiration from Greek myth of Minotaur, where Ariadne with the help of a thread escaped the labyrinth with his beloved Theseus.

## Overview

* [src/pydlib](src/pydlib) contains all the underlying code implementing the pydlib functions.

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

## Get Started

### get

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

### has

You can also test for a field simply calling:

```python
>>> import pydlib as dl

>>> dictionary = { ... }
>>> dl.has(dictionary, path='path.to.nested.field')
True
```

### update

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

### delete

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
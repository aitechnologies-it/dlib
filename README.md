# :yarn: pydlib
The Python **d**ictionary **lib**rary to get into complex nested python dictionary structures (json-like) in a safe and clean way.

## Overview

* [src/](src) contains all the underlying code implementing the dlib functions.

## Installation

To install dlib, simply use `pip`:

```bash
$ pip install dlib
```

or install from the repository:

```bash
$ git clone https://github.com/luigidisotto/dlib.git
$ cd dlib
$ python setup.py install
```

## Get Started

You can for example get the value from a nested field, just by indicating the path to tha nested sub-structure as follows:

```python
>>> import dlib

>>> dictionary = {
>>>   'path': {
>>>       'to': {
>>>          'nested': {
>>>             'field': 42
>>>           }
>>>        }
>>>    }
>>> }
>>> dlib.get(dictionary, path='path.to.nested.field', default=0)
42
```

Instead, if the field we are looking for doesn't exists, or, if it exists but has a None value, then:

```python
>>> dlib.get(dictionary, path='path.to.nested.nonexisting.field', default=0)
0
```

You can also test for a field simply calling:

```python
>>> import dlib
>>> dictionary = { ... }
>>> dlib.has(dictionary, path='path.to.nested.field', default=0)
True
```

# :yarn: pydlib
The Python **d**ictionary **lib**rary to get into complex nested python dictionary structures (json-like) in a safe and clean way. We take inspiration from Greek myth of Minotaur, where Ariadne with the help of a thread escaped the labyrinth with his beloved Theseus.

## Overview

* [src/](src) contains all the underlying code implementing the dlib functions.

## Installation

To install dlib, simply use `pip`:

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

You can for example get the value from a nested field, just by indicating the path to tha nested sub-structure as follows:

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

You can also test for a field simply calling:

```python
>>> import pydlib as dl

>>> dictionary = { ... }
>>> dl.has(dictionary, path='path.to.nested.field', default=0)
True
```

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

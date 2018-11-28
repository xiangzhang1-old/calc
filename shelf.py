"""Stores persistent variables, even if their definitions are volatile."""
from collections import OrderedDict

shelf = OrderedDict(
    root = None
)
"""
Persistent variables are "collected" in a :class:`collections.OrderedDict`.

Considering :mod:`tensorflow`-like objects, which requires custom persistence,
each object either
* implements its own shelve/unshelve (save/load may be taken)
* or, by default, use :mod:`dill` (with dates etc)

"""

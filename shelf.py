"""Stores persistent variables, even if their definitions are volatile."""
from collections import OrderedDict

shelf = OrderedDict()
"""
Persistent variables are "collected" in a :class:`collections.OrderedDict`,
similar to :class:`shelve.Shelf`.

Considering :mod:`tensorflow`-like objects, which requires custom save/load(),
each object either
* implements its own save/load()
* doesn't implement save/load(), in which case :mod:`dill` is used.

"""

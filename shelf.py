"""Stores persistent variables, even if their definitions are volatile."""
from collections import OrderedDict

shelf = OrderedDict()
"""
Persistent variables are "collected" in a dict, similar to :class:`shelve.shelf`.

Considering Tensorflow-like objects, which requires custom saving / loading,
each object either implements its own save()/load(), or utilizes :module:`dill`.
"""

import collections

shelf = collections.OrderedDict()
r"""
Stores persistent variables in a :class:`collections.OrderedDict`, that either
* are :mod:`dill`-compatible
* or implement shelve/unshelve (eg. :mod:`tensorflow`-based ones)

"""

shelf['root'] = None

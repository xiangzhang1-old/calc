import collections, time, dill
import util

shelf = collections.OrderedDict()
r"""
Stores State of Discussion in a :class:`collections.OrderedDict`, that either
* implement shelve/unshelve (eg. :mod:`tensorflow`-based ones)
* are :mod:`dill`-compatible

"""


def shelve():
    r"""
    Manually call the respective `shelve` function for each componenet of `shelf`.

    """
    util.dump(shelf['root'], 'root')

def unshelve():
    r"""
    Manually call the respective `unshelve` function for each componenet of `shelf`.

    """
    shelf['root'] = util.load('root')

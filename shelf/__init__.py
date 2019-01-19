r"""Stores and shelve/unshelves State of Discussion."""
import collections, time, dill, os


script_dir = os.path.dirname(os.path.realpath(__file__))


shelf = collections.OrderedDict()
r"""
Stores State of Discussion in a :class:`collections.OrderedDict`, that either
* implement shelve/unshelve (eg. :mod:`tensorflow`-based ones)
* are :mod:`dill`-compatible

"""


def dump(obj, file):
    r"""
    Substitute for :method:`dill.dump`.

    :param str file: will :method:`dill.dump` `obj` to `file.dill.20190101120000`
    :param object obj: object to save

    """
    with open("%s.dill.%s" % (file, time.strftime('%Y%m%d%H%M%S')), "wb") as f:
        dill.dump(obj, f)


def load(file):
    r"""
    Substitute for :method:`dill.load`.

    :param str file: will return :method:`dill.load`ed object from latest `file.dill.20190101120000`

    """
    _ = sorted([_ for _ in os.listdir(script_dir) if _.startswith(file)])
    with open(_[-1], "rb") as f:
        return dill.load(f)


def shelve():
    r"""
    Manually call the respective `shelve` function for each componenet of `shelf`.

    """
    dump(shelf['root'], 'root')


def unshelve():
    r"""
    Manually call the respective `unshelve` function for each componenet of `shelf`.

    """
    shelf['root'] = load('root')

import time, dill, os
from . import state


script_dir = os.path.dirname(os.path.realpath(__file__))


def dump(obj, filename):
    r"""
    :meth:`dill.dump` `obj` to `file.dill.YYYYMMDDHHMMSS`

    :param unicode filename:
    :param object obj: object to save

    """
    with open("%s.dill.%s" % (filename, time.strftime('%Y%m%d%H%M%S')), "wb") as f:
        dill.dump(obj, f)


def load(filename):
    _ = sorted([_ for _ in os.listdir(script_dir) if _.startswith(filename)])
    with open(_[-1], "rb") as f:
        return dill.load(f)


def dump_state():
    r"""
    For each componenet of :mod:`state`, either

    * call custom-built `dump` (eg. :mod:`tensorflow`-based objects)
    * :meth:`dump`

    """
    dump(state.root, 'root')


def load_state():
    state.root = load('root')

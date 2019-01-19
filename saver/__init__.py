import time, dill, os
from .. import state


script_dir = os.path.dirname(os.path.realpath(__file__))


def dump(obj, file):
    r"""
    :method:`dill.dump` `obj` to `file.dill.YYYYMMDDHHMMSS`

    :param str file:
    :param object obj: object to save

    """
    with open("%s.dill.%s" % (file, time.strftime('%Y%m%d%H%M%S')), "wb") as f:
        dill.dump(obj, f)


def load(file):
    _ = sorted([_ for _ in os.listdir(script_dir) if _.startswith(file)])
    with open(_[-1], "rb") as f:
        return dill.load(f)


def dump_state():
    r"""
    For each componenet of `shelf`, either
    * call custom-built `dump` (eg. :mod:`tensorflow`-based objects)
    * :method:`dump`

    """
    dump(state.root, 'root')


def load_state():
    state.root = load('root')

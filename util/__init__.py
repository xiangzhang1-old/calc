"""Implements constants and utility functions/classes."""
from __future__ import print_function, division, unicode_literals
import re, unicodedata, collections, pandas as pd, os


script_dir = os.path.dirname(os.path.realpath(__file__))


def slugify(value):
    r"""
    Make a string URL- and filename-friendly.

    Normalizes string into unicode, converts to lowercase, removes non-alpha-nu-
    merics, and converts spaces to hyphens.

    Taken from django/utils/text.py. In Django, a "slug" is a URL- and filename-
    friendly string.

    :param unicode value: String to be converted
    :return: Filename-friendly string
    :rtype: unicode
    :raises TypeError: if value is not unicode string

    """
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')
    value = unicode(re.sub('[^\w\s-]', '', value).strip().lower())
    value = unicode(re.sub('[-\s]+', '-', value))
    return value


class Graph(collections.OrderedDict):
    r"""
    Implements a graph as an adjacency list.

    :class:`collections.OrderedDict`: ``self[src]=[dst, dst2, ...]``

    Xiang Zhang, 2019/01/01

    """

    def add_node(self, n):
        r"""
        Given :math:`n\notin G`, consider :math:`G\cup\{n\}`.

        :param Node n: Node to be added

        """
        assert n not in self
        self[n] = []

    def add_edge(self, src, dst):
        r"""
        Given :math:`s,d\in G \,\bigwedge\, \neg (s\to d)`, consider :math:`G\cup\{s\to d\}`.

        :param Node src: Source node
        :param Node dst: Destination node

        """
        assert src in self and dst in self
        assert dst not in self[src]
        self[src].append(dst)

    def del_edge(self, src, dst):
        r"""
        Given :math:`\{s\to d\}\subset G`, consider :math:`G - \{s\to d\}`

        :param Node src: Source node
        :param Node dst: Destination node

        """
        assert dst in self[src]
        self[src].remove(dst)

    def del_node(self, n):
        r"""
        Given :math:`n\in G`, consider :math:`G - \{n\to m\}\forall m - \{m\to n\}\forall m`

        :param Node n: Node to be deleted

        """
        assert n in self
        del self[n]
        for m in self:
            if n in self[m]:
                self[m].remove(n)


periodic_table = pd.read_excel(script_dir + '/periodic_table.xlsx')
r"""
Periodic table. :class:`pandas.DataFrame` read from periodic_table.xlsx.
"""


def dump(obj, file):
    r"""
    Substitute for :method:`dill.dump`.

    :param str file: will :method:`dill.dump` `obj` to `file.dill.20190101120000`
    :param object obj: object to save

    """
    with open("%s.dill.%s" %(file, time.strftime('%Y%m%d%H%M%S')), "wb") as f:
        dill.dump(obj, f)

def load(file):
    r"""
    Substitute for :method:`dill.load`.

    :param str file: will return :method:`dill.load`ed object from latest `file.dill.20190101120000`

    """
    _ = sorted([_ for _ in os.listdir(script_dir) if _.startswith(file)])
    with open(_[-1], "rb") as f:
        return dill.load(f)

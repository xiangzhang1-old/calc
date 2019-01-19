"""Reusable code: constants, functions, classes."""
from __future__ import print_function, division, unicode_literals
import re, unicodedata, pandas as pd, os, collections


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


periodic_table = pd.read_excel(script_dir + '/periodic_table.xlsx')
r"""
Periodic table. :class:`pandas.DataFrame` read from periodic_table.xlsx.
"""


class Graph(collections.OrderedDict):
    r"""
    Adjacency list.
    """

    def __init__(self):
        collections.OrderedDict.__init__(self)

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

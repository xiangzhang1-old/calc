import collections


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

# -*- coding: utf-8 -*-
"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import numpy as np, pandas as pd
import uuid, weakref
import collections


class Node:

    def __init__(self, name, x=None, y=None):
        """
        Implements a generic "node" in a nested directed graph.

        :param str name: Node's name. '/' will be silently replaced with '|', \
        to facilitate id.
        :param float x: x coordinate. None to use random number
        :param float y: y coordinate

        """
        self.name = name.replace('/', '|')
        """str: Node's name."""
        self.x = x if x is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). x coordinate when drawn in 2D by Ogma.js"""
        self.y = y if y is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). y coordinate"""


class Graph(collections.OrderedDict, Node):

    def __init__(self, *args, **kwargs):
        """
        Implements a nested directed graph.

        It is-a :class:`Node`. It __init__'s in the same way as, and has the
        API of, :class:`Node`.

        In addition, a graph is implemented as adjacency list, as :class:`dict`: `self[src]=[dst, dst2, ...]`.

        """
        dict.__init__(self)
        Node.__init__(self, *args, **kwargs)

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

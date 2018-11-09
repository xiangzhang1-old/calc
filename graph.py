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
        self.uuid = str(uuid.uuid1())
        """str. UUID"""


class Graph(collections.OrderedDict, Node):

    def __init__(self, *args, **kwargs):
        """
        Implements a nested directed graph. See :meth:`Node.__init__` for syntax.

        It is-a :class:`Node`. It __init__'s in the same way as, and has the
        API of, :class:`Node`.

        It also implements a graph as-a :class:`dict`::

            {
                src:    [dst0, dst1, dst2, ...]
            }

        """
        dict.__init__(self)
        Node.__init__(self, *args, **kwargs)

    def add_node(self, n):
        """
        Trivially implements adding a node.

        :param Node n: Node to be added. Checks duplication
        """
        assert n not in self
        self[n] = []

    def add_edge(self, src, dst):
        """
        Trivially implements adding an edge.

        :param Node src: Source node
        :param Node dst: Destination node. Checks duplication
        """
        assert dst not in self[src]
        self[src].append(dst)

    def del_edge(self, src, dst):
        """
        Trivially implements deleting an edge.

        :param Node src: Source node
        :param Node dst: Destination node
        """
        self[src].remove(dst)

    def del_node(self, n):
        """
        Trivially implements deleting a node.

        :param Node n: Node to be deleted
        """
        del self[n]
        for src in self:
            if n in self[src]:
                self.del_edge(src, n)

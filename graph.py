# -*- coding: utf-8 -*-
"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import numpy as np, collections
from . import util, state


class Node:

    def __init__(self, name, x=None, y=None):
        """
        Implements a generic node in a nested directed graph.

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


class Graph(Node, util.Graph):

    def __init__(self, *args, **kwargs):
        r"""
        Implements a nested directed graph :math:`\subset` state.root.

        Is-a :class:`Node`.
        Is-a :class:`util.Graph`
        Has-a few more tricks up its sleeve.

        """
        util.Graph.__init__(self)
        Node.__init__(self, *args, **kwargs)

    def iter(self):
        r"""
        :return: generator that recursively iterates through `self`

        """
        yield self
        for _ in self:
            if isinstance(_, Graph):
                for __ in iter(_):
                    yield __

    @property
    def parent(self):
        r"""
        :return: first parent :class:`Node` or `None` if nonexistent

        """
        for _ in iter(state.root):
            if self in _:
                return _
        return None

    @property
    def prev(self):
        r"""
        :return: first prev :class:`Node` or `None` if nonexistent

        """
        parent = self.parent
        if parent is None:
            return None
        for _ in parent:
            if self in parent[_]:
                return _
        return None

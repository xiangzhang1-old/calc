# -*- coding: utf-8 -*-
"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import numpy as np
from . import lib, state


class Node:

    def __init__(self, name, x=None, y=None):
        """
        A generic node in a nested directed graph.

        :param str name: Node's name. '/' will be silently replaced with '|', to facilitate id.
        :param float x: x coordinate. None to use random number
        :param float y: y coordinate

        """
        self.name = name.replace('/', '|')
        """str: Node's name."""
        self.x = x if x is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). x coordinate when drawn in 2D by Ogma.js"""
        self.y = y if y is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). y coordinate"""


class Graph(lib.Graph, Node):

    def __init__(self, *args, **kwargs):
        r"""
        Implements a nested directed graph :math:`\subset` state.root.
        Borrows from the Linux Filesystem paradigm.

        Is-a :class:`Node`.
        Is-a :class:`lib.Graph`.
        Has-a few more tricks borrowed from the Linux FileSystem metaphor.

        """
        lib.Graph.__init__(self)
        Node.__init__(self, *args, **kwargs)

    #lfs
    def ls(self):
        r"""
        :return: generator that recursively iterates through `self`

        """
        yield self
        for _ in self:
            if isinstance(_, Graph):
                for __ in iter(_):
                    yield __

    @property
    def _parent(self):
        r"""
        :return: first parent
        :rtype: class.Node
        :raises LookupError: if non-existent

        """
        for _ in state.root.ls():
            if self in _:
                return _
        raise LookupError

    @property
    def _prev(self):
        r"""
        :return: first prev
        :rtype: class.Node
        :raises LookupError: if non-existent

        """
        parent = self._parent
        for _ in parent:
            if self in parent[_]:
                return _
        raise LookupError

    def cd(self, path):
        r"""
        :param unicode path: one of

        * relative path. parent `..`, previous `-`, root '/' supported
        * absolute path, e.g. `/QD/15A vacuum`

        :rtype: graph.Node
        :raises LookupError: if non-existent
        :raises ValueError: if path is illegal


        """
        path = path.rstrip('/').split('/', 1)
        if len(path) == 1:
            if path[0] == '':
                return state.root
            if path[0] == '..':
                return self._parent
            if path[0] == '-':
                return self._prev
            for _ in self:
                if _.name == path[0]:
                    return _
            raise LookupError
        if len(path) == 2:
            return self.cd(path[0]).cd(path[1])
        raise ValueError

    @property
    def pwd(self):
        r"""
        :return: absolute path

        """
        if self is state.root:      # hack. should be if parent not exist
            return ''
        return self._parent.pwd + '/' + self.name

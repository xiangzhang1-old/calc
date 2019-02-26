"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import numpy as np
from . import lib, state


class Node(object):

    def __init__(self):
        r"""
        A generic node in a nested directed graph.

        :ivar str name: Node's name. Hint: don't insert /.
        :ivar float x: x coordinate for Ogma.js. float in (-200, 200).
        :ivar float y: y coordinate

        """
        super().__init__()
        self.name = None
        self.x = np.random.uniform(low=-200, high=200)
        self.y = np.random.uniform(low=-200, high=200)


class Graph(lib.Graph, Node):

    def __init__(self):
        r"""
        Implements a nested directed graph :math:`\subset` state.root.
        Borrows from the Linux Filesystem paradigm.

        Is-a :class:`Node`.
        Is-a :class:`lib.Graph`.
        Has-a few more tricks borrowed from the Linux FileSystem metaphor.

        """
        super().__init__()

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

# -*- coding: utf-8 -*-
"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import numpy as np, collections
import util


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


class Graph(collections.OrderedDict, util.Graph):

    def __init__(self, *args, **kwargs):
        """
        Implements a directed graph.

        It is-a :class:`Node`, and is-a :class:`util.Graph`.

        """
        util.graph.Graph.__init__(self)
        Node.__init__(self, *args, **kwargs)

# -*- coding: utf-8 -*-
"""Implements nested directed graphs. Like folders, they organize DFT computations."""
from __future__ import print_function, division, unicode_literals
import weakref
import numpy as np


def id(id):
    """
    The node identified by id.

    (Consider) the node whose id is id.
    Located by iterating through each segment of id.

    :param Node.id id: the query
    :return: the response to query
    :rtype: Node
    :raises KeyError: if the node identified by id does not exist
    """
    # naming shit
    # folder.child, also KeyError
    # where is master
    n = node.the('master')

# 如果是folder的话太脑残了吧？加点料，双指针？


class Node:

    def __init__(self, name, prev, parent, x=None, y=None):
        """
        Implements a generic "node" in a nested directed graph.

        :param str name: Node's name. '/' will be silently replaced with '|', \
        to facilitate id.
        :param Node prev: Previous node, can be None.
        :param Node parent: Parent node, is None for root node
        :param float x: x coordinate. None to use random number
        :param float y: y coordinate. None to use random number

        """
        self.name = name.replace('/', '|')
        """str: Node's name."""
        self.prev = weakref.proxy(prev) if prev is not None else None
        """
        :obj:`weakref.ProxyType` to prev Node, or None. Similar to a double\
        linked list, the pointer needs to be updated when the node is moved
        """
        self.parent = weakref.proxy(parent) if parent is not None else None
        """:obj:`weakref.ProxyType` to parent Node, or None for root node."""
        self.x = x if x is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). x coordinate when drawn in 2D by Ogma.js"""
        self.y = y if y is not None else np.random.uniform(low=-200, high=200)
        """float in (-100, 100). y coordinate"""

    @property
    def id(self):
        """
        Slash-join of all ancestors' names.

        Joins the node's name, its parent's name, it's grandparent's name, all
        the way to but excluding "root", by slash(/). It's the node's UID in
        a nested graph.

        Caveat: While a Unix filesystem look-and-feel is achieved, the root \
        node's id is qualitatively different, which may cause problems.

        :return: UID of the node, e.g. ``/PbS QD/bare qd/o(e) performance``
        :rtype: str
        """
        if parent is None:
            return ""
        else:
            return parent.id + "/" + name

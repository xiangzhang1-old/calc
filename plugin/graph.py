from .. import state


class GraphMixin:
    r"""
    Based on the Linux FS paradigm, a few more tricks for :class:`graph.Graph`.
    """

    def ls(self):
        r"""
        :return: generator that recursively iterates through `self`

        """
        yield self
        for _ in self:
            if isinstance(_, GraphMixin):   # hack. should be Graph. https://stackoverflow.com/a/2462040/6417519
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
        parent = self.parent
        for _ in parent:
            if self in parent[_]:
                return _
        raise LookupError

    def cd(self, path):
        r"""
        :param str path: one of

        * relative path. parent `..` and previous `-` supported
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
            return path[0].cd(path[1])
        raise ValueError

    @property
    def pwd(self):
        r"""
        :return: absolute path

        """
        if self is state.root:      # hack. should be if parent not exist
            return ''
        return self._parent.pwd + '/' + self.name

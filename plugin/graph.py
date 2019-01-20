import state

class GraphMixin:

    def iter(self):
        r"""
        :return: generator that recursively iterates through `self`

        """
        yield self
        for _ in self:
            if isinstance(_, GraphMixin):   # hack. should be Graph.
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

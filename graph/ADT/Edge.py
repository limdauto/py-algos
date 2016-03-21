class Edge:

    __slots__ = '_origin', '_dest', '_weight'

    def __init__(self, u, v, w):
        self._origin = u
        self._dest = v
        self._weight = w

    def endpoints(self):
        return (self._origin, self._destination)

    def opposite(self, v):
        return self._dest if v is self._origin else self._origin

    def weight(self):
        return self._weight

    def __hash__(self):
        return hash((self._origin, self._dest))

    def __str__(self):
        return "{} -{}-> {}".format(self._origin, self._weight, self._dest)

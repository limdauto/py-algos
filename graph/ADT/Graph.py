from ADT.Edge import Edge
from ADT.Vertex import Vertex

class Graph:
    """
    A graph representation using adjacency map {source: {dest: edge}}
    """

    def __init__(self, directed=False):

        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def has_vertex(self, u):
        return u in self._outgoing

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed else total // 2

    def edges(self):
        result = set()

        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())

        return result

    def get_edge(self, u, v):
        return self._outgoing[u].get(v, None)

    def degree(self, v, outgoing=True):
        return len(self._outgoing[v]) if outgoing else len(self._incoming[v])

    def incident_edges(self, v, outgoing=True):
        adj = self._outgoing if outgoing else self._incoming
        return adj[v].values()

    def insert_vertex(self, x):
        v = Vertex(x)
        self._outgoing[v] = {}
        if self.is_directed():
            self._incoming[v] = {}
        return v

    def insert_edge(self, u, v, w):
        e = Edge(u, v, w)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

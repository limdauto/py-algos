# https://www.hackerrank.com/challenges/bfsshortreach
import sys

from ADT.Graph import Graph
from ADT.Vertex import Vertex
from algorithms.traversal import bfs_depth

WEIGHT = 6


def readint(x):
    return int(x)


if __name__ == '__main__':
    t = sys.stdin.readline()
    for i in range(int(t)):
        g = Graph(directed=False)
        n, m = map(readint, sys.stdin.readline().split(" "))

        vertices = []
        for i in range(1, n + 1):
            v = g.insert_vertex(i)
            vertices.append(v)

        for i in range(m):
            u, v = map(readint, sys.stdin.readline().split(" "))
            u = vertices[u - 1]
            v = vertices[v - 1]
            g.insert_edge(u, v, WEIGHT)

        s = vertices[int(sys.stdin.readline()) - 1]

        discovered = {s: None}
        bfs_depth(g, s, discovered)

        res = []
        for i in range(1, n + 1):
            v = vertices[i - 1]

            if v is s:
                continue
            elif v in discovered:
                res.append(discovered[v] * WEIGHT)
            else:
                res.append(-1)

        print(*res)
    print('\n')

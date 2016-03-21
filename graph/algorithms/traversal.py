def dfs(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            dfs(g, v, discovered)


def construct_path(g, u, v, discovered):
    path = []
    if v in discovered:
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[v]
            parent = e.opposite(v)
            path.append(parent)
            walk = parent

    path.reverse()
    return path


def dfs_forest(g):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            dfs(g, u, forest)


def bfs(g, s, discovered):
    level = [s]

    while len(level) > 0:
        next_level = []

        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)

        level = next_level


def bfs_depth(g, s, discovered):
    """
    Instead of storing the discovery edge,
    store the discovery depth
    """

    level = [s]
    depth = 1

    while len(level) > 0:
        next_level = []

        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = depth
                    next_level.append(v)

        level = next_level
        depth += 1

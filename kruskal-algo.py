class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pu] > self.rank[pv]:
            self.parent[pv] = pu
        elif self.rank[pv] > self.rank[pu]:
            self.parent[pu] = pv
        else:
            self.parent[pu] = pv
            self.rank[pv] += 1
        return True

def kruskal(graph):
    graph.sort(key=lambda x: x[2])
    n = len(graph)
    ds = DisjointSet(n)
    mst = []
    for edge in graph:
        u, v, w = edge
        if ds.union(u, v):
            mst.append(edge)
    return mst

# Example 
graph = [(0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11), (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9), (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1), (6, 8, 6), (7, 8, 7)]
mst = kruskal(graph)
print("Minimum Spanning Tree:", mst)

import heapq

def prim(graph):
    n = len(graph)
    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, vertex)
    mst = []

    while min_heap:
        weight, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst.append((u, weight))
        for v, w in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (w, v))

    return mst

# Example usage:
graph = [[(1, 4), (7, 8)],
         [(0, 4), (2, 8), (7, 11)],
         [(1, 8), (3, 7), (5, 4), (8, 2)],
         [(2, 7), (4, 9), (5, 14)],
         [(3, 9), (5, 10)],
         [(2, 4), (3, 14), (4, 10), (6, 2)],
         [(5, 2), (7, 1), (8, 6)],
         [(0, 8), (1, 11), (6, 1), (8, 7)],
         [(2, 2), (6, 6), (7, 7)]]
mst = prim(graph)
print("Minimum Spanning Tree:", mst)

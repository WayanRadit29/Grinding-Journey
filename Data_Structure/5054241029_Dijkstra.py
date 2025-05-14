import heapq

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n

    dist[start] = 0
    pq = [(0, start)]   # (jarak, node)

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue

        for v, w in graph[u]:
            nd = d + w
            if nd < dist[v]:
                dist[v] = nd
                prev[v] = u
                heapq.heappush(pq, (nd, v))

    return dist, prev

def reconstruct_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    return path[::-1]


n = 9
edges = [
    (0, 1, 4),(0, 7, 8),(1, 2, 8),(1, 7, 11),
    (2, 3, 7),(2, 5, 4),(2, 8, 2),(3, 4, 9),
    (3, 5, 14),(4, 5, 10),(5, 6, 2),(6, 7, 1),
    (6, 8, 6),(7, 8, 7)
]


adj_list = [[] for _ in range(n)]
for u, v, w in edges:
    adj_list[u].append((v, w))
    adj_list[v].append((u, w))

start = 0
distances, parents = dijkstra(adj_list, start)

print(f"Start node: {start}\n")
for node in range(n):
    if distances[node] == float('inf'):
        print(f"Node {node}: unreachable")
    else:
        path = reconstruct_path(parents, node)
        print(f"Node {node}: distance = {distances[node]}, path = {path}")

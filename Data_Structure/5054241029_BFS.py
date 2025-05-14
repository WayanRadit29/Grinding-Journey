from collections import deque

def bfs(start, adj_list):
    visited = [False] * len(adj_list)
    queue = deque()

    visited[start] = True
    queue.append(start)

    while queue:
        u = queue.popleft()
        print(f"Visited {u}")

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)



n = 7

edges = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (3,4),
    (2, 4),
    (4, 5),
    (5, 6)
]

adj_list = [[] for _ in range(n)]

for u, v in edges:
    adj_list[u].append(v)
    adj_list[v].append(u)


bfs(0, adj_list)
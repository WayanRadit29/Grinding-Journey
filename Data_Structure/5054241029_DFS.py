def dfs_iterative(start, adj_matrix):
    n = len(adj_matrix)
    visited = [False] * n
    stack = [start]

    while stack:
        u = stack.pop()
        if not visited[u]:
            print(f"Visited {u}")
            visited[u] = True
          
            for v in range(n):
                if adj_matrix[u][v] == 1 and not visited[v]:
                    stack.append(v)
            

n = 7  # Jumlah simpul (0 sampai 6)


adj_matrix = [[0] * n for _ in range(n)]


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


for u, v in edges:
    adj_matrix[u][v] = 1
    adj_matrix[v][u] = 1

dfs_iterative(0, adj_matrix)



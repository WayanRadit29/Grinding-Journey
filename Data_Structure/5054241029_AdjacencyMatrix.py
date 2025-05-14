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


print("Adjacency Matrix:")
for row in adj_matrix:
    print(row)

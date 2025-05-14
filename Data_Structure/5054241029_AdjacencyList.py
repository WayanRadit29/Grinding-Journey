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

print("Adjacency List:")
for i in range(n):
    print(f"{i}: {adj_list[i]}")

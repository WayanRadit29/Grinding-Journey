n = 7 

edges_list = [
    (0, 1),
    (0, 2),
    (1, 2),
    (1, 3),
    (3,4),
    (2, 4),
    (4, 5),
    (5, 6)
]

print("Edge List:")
for idx, (u, v) in enumerate(edges_list):
    print(f"{idx}: ({u}, {v})")
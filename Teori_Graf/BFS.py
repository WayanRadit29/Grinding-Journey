#Kita akan membuat fungsi implementasi dari BFS secara sederhana

def BFS(Graf, start):
    visited = set()
    result = []
    queue = [start]

    while len(queue) > 0:
        vertex = queue.pop(0)

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)
            queue.extend(Graf[vertex])

    return result

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}
print(BFS(graph, 'A')) 


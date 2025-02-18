graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)]
}

def Dijkstra(graph, start_node):
    visited = set()  # Untuk menyimpan node-node yang sudah dikunjungi
    distance = {node: float('inf') for node in graph}  # Jarak dari start_node ke setiap node
    distance[start_node] = 0  # Jarak ke start_node adalah 0
    unvisited = [node for node in graph]  # Daftar node yang belum dikunjungi

    while unvisited:
        #Mencari node dengan jarak terpendek yang belum dikunjungi
        min_node = None
        min_dist = float('inf')
        for node in unvisited:
            if distance[node] < min_dist:
                min_dist = distance[node]
                min_node = node

        #Jika tidak ada node yang bisa diproses, keluar dari loop
        if min_node is None:
            break

        #Tandai node ini sebagai sudah dikunjungi
        visited.add(min_node)
        unvisited.remove(min_node)  # Hapus dari daftar node yang belum dikunjungi

        #Perbarui jarak ke tetangga-tetangga min_node
        for neighbor, weight in graph[min_node]:
            if neighbor not in visited:  # Hanya proses tetangga yang belum dikunjungi
                new_distance = distance[min_node] + weight
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance

    return distance

print(Dijkstra(graph, 'A'))
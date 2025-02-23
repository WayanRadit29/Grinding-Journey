class Solution(object):
    def networkDelayTime(self, times, n, k):
        #Proses memasukan struktur data graf menggunakan adjacency list
        graf = dict()
        for u, v, w in times:
            if u not in graf:
                 graf[u] = []  # Inisialisasi sebagai list kosong jika belum ada
            graf[u].append((v, w))

            if v not in graf:
                graf[v] = []
        
        if len(graf) != n:
            return -1
            
        #Mulai masuk ke algoritma Dijsktra
        visited = set()
        unvisited = [node for node in graf]
        total = {node : float('inf') for node in graf} #Edit kode ini agar semua node dijangkau
        total[k] = 0

        while unvisited:
            min_node = None
            min_total = float('inf')
            for node in unvisited:
                if total[node] < min_total:
                    min_node = node
                    min_total = total[node]

            if min_node is None:
                break

            #Proses untuk mengecek tetangganya
            for neighbor, time in graf[min_node]:
                if neighbor not in visited:
                    new_total = total[min_node] + time
                    if new_total < total[neighbor]:
                        total[neighbor] = new_total

            visited.add(min_node)
            unvisited.remove(min_node) 

        #Sekarang ngecek total waktu minimum dan apakah semua node berhasil dikunjungi
        min_time = max(list(total.values()))
        if min_time == float('inf'):
            return -1
        else:
            return min_time 



        

        

        
        

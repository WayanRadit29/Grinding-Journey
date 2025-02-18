#Implementasi BFS dengan konsep flood fill, yang dimana warna akan diwakili oleh warna-warna tertentu

#Membuat grid terlebih dahulu untuk menjadi tempat-tempat dari warna
row = int(input())
collumn = int(input())
grid = [list(map(int, input().split())) for _ in range(row)]

#Membuat fungsi untuk BFS Flood Fill
def FloodFillBFS(row, collumn, start_row, start_collumn, new, grid):
    old = grid[start_row][start_collumn]
    queue = [(start_row, start_collumn)] #Untuk menyimpan tetangga-tetangga dari pixel yang dipilih, syaratnya harus memiliki warna yang sama
    visited = [[False for _ in range(collumn)] for _ in range(row)] #Untuk menyimpan pixel-pixel yang sudah dikunjungi dan diubah warnanya
    
    
    while len(queue) > 0:
        vertex = queue.pop(0)
        grid[vertex[0]][vertex[1]] = new
        visited[vertex[0]][vertex[1]] = True

    
        #Pengecekan empat arah: atas, bawah, kiri, kanan
        # Tandai vertex saat ini sebagai sudah dikunjungi

        # Pengecekan empat arah: atas, bawah, kiri, kanan
        if vertex[0] - 1 >= 0 and grid[vertex[0] - 1][vertex[1]] == old and not visited[vertex[0] - 1][vertex[1]]:  # Atas
            location = (vertex[0] - 1, vertex[1])
            queue.append(location)

        if vertex[0] + 1 < row and grid[vertex[0] + 1][vertex[1]] == old and not visited[vertex[0] + 1][vertex[1]]:  # Bawah
            location = (vertex[0] + 1, vertex[1])
            queue.append(location)

        if vertex[1] - 1 >= 0 and grid[vertex[0]][vertex[1] - 1] == old and not visited[vertex[0]][vertex[1] - 1]:  # Kiri
            location = (vertex[0], vertex[1] - 1)
            queue.append(location)

        if vertex[1] + 1 < collumn and grid[vertex[0]][vertex[1] + 1] == old and not visited[vertex[0]][vertex[1] + 1]:  # Kanan
            location = (vertex[0], vertex[1] + 1)
            queue.append(location)


    return grid


print(FloodFillBFS(row, collumn,0,0,3,grid))
        








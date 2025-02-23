class Solution(object):
    def orangesRotting(self, grid):
        #Deklarasi variabel untuk hitung waktu
        minutes = 0
        fresh = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        queue = [] 

        #For loop untuk mencari posisi jeruk yang busuk
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:  #Kalau tidak ada jeruk segar, langsung return 0
            return 0

        while queue and fresh > 0:
            for _ in range(len(queue)):
                start = queue.pop(0)
            
            
                if start[0] - 1 >= 0 and grid[start[0] - 1][start[1]] == 1 and not visited[start[0] - 1][start[1]]:  # Atas
                    location = (start[0] - 1, start[1])
                    queue.append(location)
                    grid[start[0] - 1][start[1]] = 2
                    visited[start[0] - 1][start[1]] = True
                    fresh -= 1
                  

                if start[0] + 1 < len(grid) and grid[start[0] + 1][start[1]] == 1 and not visited[start[0] + 1][start[1]]:  # Bawah
                    location = (start[0] + 1, start[1])
                    queue.append(location)
                    grid[start[0] + 1][start[1]] = 2
                    visited[start[0] + 1][start[1]] = True
                    fresh -= 1
               

                if start[1] - 1 >= 0 and grid[start[0]][start[1] - 1] == 1 and not visited[start[0]][start[1] - 1]:  # Kiri
                    location = (start[0], start[1] - 1)
                    queue.append(location)
                    grid[start[0]][start[1] - 1] = 2
                    visited[start[0]][start[1] - 1] = True
                    fresh -= 1
               
                    

                if start[1] + 1 < len(grid[0]) and grid[start[0]][start[1] + 1] == 1 and not visited[start[0]][start[1] + 1]:  # Kanan
                    location = (start[0], start[1] + 1)
                    queue.append(location)
                    grid[start[0]][start[1] + 1] = 2
                    visited[start[0]][start[1] + 1] = True
                    fresh -= 1
                    
            minutes += 1

                
            


            #Proses untuk memastikan apakah semua jeruk membusuk 
        for a in range(len(grid)):
                for b in range(len(grid[0])):
                    if grid[a][b] == 1:
                        return -1

        return minutes




        

        

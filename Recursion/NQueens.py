#Input nilai N - Queens
N = int(input())

#Buat papan dengan ukuran N kali N dan isinya "titik" semua
board = [['.' for _ in range(N)] for _ in range(N)]
solusi = []

#Mulai ke function
def NQueensSolve(board, N, row):
    if N == row:
        for baris in board:
            solusi.append([''.join(baris)])
        return

    for col in range(N):
        if isSafe(board, N, row, col):
            board[row][col] = 'Q'
            NQueensSolve(board, N, row + 1)
            board[row][col] = '.'

    
def isSafe(board, N, row, col):
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 'Q':
            return False

    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 'Q':
            return False
            
    return True



NQueensSolve(board, N, 0)
for hasil in solusi:
    for baris in hasil:
        print(baris)
    print()
print(f"Total Solution : {len(solusi)}")


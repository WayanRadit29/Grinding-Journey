def HanoiTower(N, A, B, C, from_rod, aux_rod, to_rod):
    if N == 1:  # Base case
        C.append(A.pop())  # Pindahkan cakram terakhir dari A ke C
        print(f"Pindahkan cakram {C[-1]} dari {from_rod} ke {to_rod}")  # Print langkah
    else:
        # Langkah 1: Pindahkan N-1 cakram dari A ke B, gunakan C sebagai perantara
        HanoiTower(N-1, A, C, B, from_rod, to_rod, aux_rod)
        
        # Langkah 2: Pindahkan cakram ke-N dari A ke C
        C.append(A.pop())
        print(f"Pindahkan cakram {C[-1]} dari {from_rod} ke {to_rod}")
        
        # Langkah 3: Pindahkan N-1 cakram dari B ke C, gunakan A sebagai perantara
        HanoiTower(N-1, B, A, C, aux_rod, from_rod, to_rod)

# Input jumlah cakram
N = int(input("Masukkan jumlah cakram: "))

# Inisialisasi tiang-tiang
A = [i for i in range(N, 0, -1)]  # Isi tiang A dengan cakram (dari besar ke kecil)
B = []  # Tiang B kosong
C = []  # Tiang C kosong

# Panggil fungsi Tower of Hanoi
print("Langkah-langkah untuk menyelesaikan Tower of Hanoi:")
HanoiTower(N, A, B, C, "A", "B", "C")

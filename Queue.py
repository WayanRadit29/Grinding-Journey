from collections import deque

antrian = deque(list(map(str, input().split())))

def enqueue(antrian, N):
    return antrian.append(N)

def dequeue(antrian):
    if len(antrian) < 0:
        return "Tidak ada orang yang antri"
    else:
        return antrian.popleft()

def peek(antrian):
    if len(antrian) < 0:
        return "Tidak ada orang yang antri"
    else:
        return antrian[0]

def isEmpty(antrian):
    return len(antrian) == 0

enqueue(antrian, "Budi Doremi")
print(f"Ada pelanggan yang baru datang di antrian, hasilnya : {antrian}")
dequeue(antrian)
print(f"Pelanggan pertama telah dilayani : {antrian}")
dequeue(antrian)
print(f"Pelanggan selanjutnya juga telah dilayani : {antrian}")
print(f"Pelanggan yang sedang dilayani sekarang : {peek(antrian)}")
print(f"Mengecek apakah antrian kosong : {isEmpty(antrian)}")


N = int(input())  # Ambil jumlah bebek (atau elemen) yang akan dimasukkan

peek = []      # Ini buat nyimpan berapa banyak bebek yang bisa diintip oleh tiap bebek (hasil akhir)
store = []     # Ini buat nyimpen tinggi bebek-bebeknya
stack = []     # Ini stack monotonic — isinya **indeks** bebek yang bisa jadi "tembok pembatas"

# Kita masukkan tinggi bebek satu per satu ke store
for _ in range(N):
    h = int(input())
    store.append(h)

# Kita proses satu per satu bebek dari kiri ke kanan (urutan indeks)
for i in range(len(store)):
    if stack:
        # Selama bebek di stack lebih pendek atau sama tinggi dengan bebek sekarang, kita buang dari stack
        # Artinya: bebek yang pendek ini gak bisa "menghalangi pandangan"
        while stack and store[stack[-1]] <= store[i]:
            stack.pop()

        # Kalau setelah pembersihan stack kosong, berarti semua sebelumnya bisa diintip
        if not stack:
            peek.append(0 + i + 1)  # semua dari awal sampai sekarang bisa diintip
        else:
            peek.append(i - stack[-1])  # hanya yang jaraknya ke belakang hingga pemblokir terakhir
        stack.append(i)  # Tambahkan bebek saat ini sebagai kandidat pemblokir berikutnya
    else:
        # Stack kosong artinya ini bebek pertama, otomatis bisa intip semua ke belakang (yaitu cuma dirinya)
        stack.append(i)

# Kita jumlahkan semua hasil pengintipan, dan tambahkan 1 untuk bebek pertama (karena peek awal tidak ditambah)
print(sum(peek) + 1)

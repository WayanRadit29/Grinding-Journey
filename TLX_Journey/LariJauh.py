# Ambil jumlah patok (N) dan jumlah bebek (K)
N, K = map(int, input().split())

# Ambil input jarak antar patok (misalnya jarak dari patok ke patok)
jarak_patok = list(map(int, input().split()))

# Ambil kemampuan lari setiap bebek (berapa jauh maksimal bisa lari)
kemampuan_lari = list(map(int, input().split()))

# Ubah jarak patok jadi prefix sum → artinya: patok[i] = total jarak dari start sampai patok ke-i
# Ini penting karena kita mau tau bebek bisa sampai patok ke berapa berdasarkan total jarak
prefix_sum = 0
for i in range(N):
    prefix_sum = prefix_sum + jarak_patok[i]
    jarak_patok[i] = prefix_sum

# Sekarang kita cek satu per satu bebek
for bebek in kemampuan_lari:
    ketemu = False  # Flag untuk cek apakah kita sudah nemu patok yang gak bisa dicapai
    for patok in jarak_patok:
        # Kalau bebek gak sanggup lari sejauh patok ini
        if bebek < patok:
            # Print posisi patok tersebut (index pertama yang tidak bisa dicapai)
            # Tapi hati-hati, .index() bisa salah kalau ada jarak yang sama di list
            print(jarak_patok.index(patok))
            ketemu = True
            break
    # Kalau semua patok bisa dicapai, maka kita print total jumlah patok (artinya bisa sampai ujung)
    if not ketemu:
        print(jarak_patok.index(patok) + 1)

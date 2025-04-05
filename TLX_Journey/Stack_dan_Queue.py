N = int(input())  # Kita ambil jumlah perintah (command) yang akan diproses

arr = []  # Kita pakai list sebagai tempat penyimpanan, bisa diibaratkan kereta yang bisa nambah depan-belakang

for _ in range(N):
    command = input().split()  # Kita pecah inputnya, karena bisa jadi ada dua bagian: command dan value
    command = list(command)

    # Kalau perintahnya 'push_back', artinya nambah elemen di belakang list (kayak append biasa)
    if command[0] == 'push_back':
        arr.append(command[1])

    # Kalau 'push_front', kita gak bisa pakai insert(0, ...) langsung (agak lambat), 
    # jadi kita bikin list baru yang dimulai dari elemen baru lalu gabungin sisanya
    elif command[0] == 'push_front':
        temp_arr = [command[1]] + arr
        arr = temp_arr  # temp_arr jadi list yang sudah ditambahkan di depan

    # 'pop_back' berarti hapus elemen terakhir (kalau masih ada)
    elif command[0] == 'pop_back':
        if arr:
            arr.pop()

    # 'pop_front' berarti hapus elemen pertama (kalau masih ada)
    elif command[0] == 'pop_front':
        if arr:
            arr.pop(0)

# Di akhir, kita cetak seluruh isi list satu per satu sesuai urutannya
for element in arr:
    print(element)

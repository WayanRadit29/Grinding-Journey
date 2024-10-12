#Input n sebagai panjang dari perhitungan 1234...dst
n = int(input())

#Inisiasi sebuah string kosong untuk menyimpan nilai dari penjumlahan string angka
simpan_nilai = ''

#Melakukan foor loop untuk melakukan penjumlahan strinng secara berulang sepanjang nilai n
for a in range(1, n + 1):
    simpan_nilai += str(a)

#print outputnya
print(simpan_nilai)

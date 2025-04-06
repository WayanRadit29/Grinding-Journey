class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        # Kita akan mencari elemen pertama yang lebih besar (Next Greater Element / NGE)
        # untuk setiap elemen di nums2, lalu gunakan itu untuk menjawab pertanyaan pada nums1.

        # Array untuk menyimpan NGE. nge[i] menyimpan elemen pertama yang lebih besar dari nums2[i].
        # Jika tidak ada elemen lebih besar di kanan, maka nilainya -1.
        nge = [-1] * len(nums2)

        # Stack digunakan untuk menyimpan indeks dari elemen-elemen
        # yang belum menemukan NGE-nya.
        stack = []

        # Kita iterasi nums2 dari kiri ke kanan.
        # Saat kita menemukan elemen yang lebih besar dari elemen di atas stack,
        # maka itu adalah NGE untuk elemen di stack tersebut.
        for i in range(len(nums2)):
            # Selama stack tidak kosong dan elemen saat ini lebih besar
            # dari elemen yang diwakili oleh indeks paling atas di stack...
            while stack and nums2[stack[-1]] < nums2[i]:
                # Maka elemen saat ini adalah NGE bagi elemen tersebut.
                nge[stack.pop()] = nums2[i]
            # Tambahkan indeks elemen saat ini ke stack.
            # Karena mungkin elemen ini belum menemukan NGE-nya.
            stack.append(i)

        # Sekarang, kita siapkan output berdasarkan elemen di nums1.
        # Untuk tiap elemen di nums1, kita cari dulu indeksnya di nums2,
        # lalu ambil NGE-nya dari array nge.
        output = []
        for num in nums1:
            idx = nums2.index(num)   # Cari posisi elemen num di nums2
            output.append(nge[idx])  # Ambil hasil NGE dari posisi tersebut

        return output

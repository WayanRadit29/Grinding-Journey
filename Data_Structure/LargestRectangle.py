def largestRectangle(h):
    stak = []
    luas_maks = 0
    for i in range(len(h)):
        while stak and h[stak[-1]] > h[i]:
            tinggi = h[stak.pop()]
            lebar = i if not stak else i - stak[-1] - 1
            luas = tinggi * lebar
            luas_maks = max(luas_maks, luas)
        stak.append(i)
        
    while stak:
            tinggi = h[stak.pop()]
            lebar = len(h) if not stak else len(h) - stak[-1] - 1
            luas = tinggi * lebar
            luas_maks = max(luas_maks, luas)
        
    return luas_maks


arr = list(map(int,input().split()))

print(largestRectangle(arr))
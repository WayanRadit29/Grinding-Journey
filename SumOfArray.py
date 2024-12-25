#input :
arr = list(map(int,input().split()))

#Inisialisasi fungsi dan rekursinya:

def sumarray(arr):
    if len(arr) == 0 or arr is None:
        return 0
    else:
        return arr[0] + sumarray(arr[1:])
    
print(sumarray(arr))
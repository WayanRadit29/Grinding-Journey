arr = list(map(int,input("Input bilangan-bilangan : ").split()))
target = int(input("Masukan target dari subset sum : "))

#Fungsi dan rekursi
def subsetsum(arr, result = target):
    #Base Case
    if result == 0:
        return True
    elif result != 0 and len(arr) == 0:
        return False
    else:
        #Opsi 1
        first = arr[0]
        remain = arr[1:]
        ex = subsetsum(remain, result)

        #Opsi 2
        result -= first
        inc = subsetsum(remain, result)
    return ex or inc


print(subsetsum(arr))


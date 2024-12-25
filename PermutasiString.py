#Input
string = input("Masukan string yang anda ingin permutasi : ")


#Recursion
def stringpermutate(string):
    if len(string) == 1:
        return [string]

    else: 
        simpan = []
        for i in range(len(string)):
            L = list(string)
            del L[i]
            result = stringpermutate(''.join(L))
            for hasil in result:
                simpan.append(string[i] + hasil)
    return simpan
    


for kata in stringpermutate(string):
    print(kata)





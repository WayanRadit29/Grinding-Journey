N = int(input())

for i in range(N):
    print(' ' * (N - i - 1), end='')
    
    nilai = 1  
    for j in range(i + 1):
        print(nilai, end=' ')
       
        nilai = nilai * (i - j) // (j + 1)

    print()

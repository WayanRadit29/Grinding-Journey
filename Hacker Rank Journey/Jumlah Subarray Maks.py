def subArraySum(arr, n, s): 
      for i in range(n):
          for j in range(n):
              sub_sum = sum(arr[i:j])
              if sub_sum == s:
                  i += 1
                  print(i, j)
                  break
               
               
       
       
       
       
       
       
       
n, s = map(int,input().split())
arr = list(map(int,input().split()))
subArraySum(arr, n, s)






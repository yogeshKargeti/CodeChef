def countswap(arr):
  count=0
  while arr[0]!=1:
    temp=arr[0]
    arr[0]=arr[temp-1]
    arr[temp-1]=temp
    print(arr)
    count+=1
  return count

ar=list(map(int,input().split()))
print(countswap(ar))
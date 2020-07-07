#n,s=map(int,input().split())
#arr=list(input().split())
n=50
arr=[1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8,9,10,]
tf=1
s=list()
s.append(arr[0])
for k in range(1,n):
  if(arr[k]>=s[-1]):
    s.append(arr[k])
  while(len(s)>0 and s[-1]>arr[k]):
    p=arr[s[-1]]
    tf=(tf*(p-k+1))%1000000007
  s.append(arr[k])
print(tf)
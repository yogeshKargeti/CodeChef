"""def cald():
  n,k=map(int,input().split())
  ck=list(map(int,input().split()))
  maxl=0
  st=set(ck)
  if len(st)<k:
    return n
  i=0
  while(i<n-k+1 and n-i>maxl) :
  	j=n
  	while j>i and j-i>maxl :
  		st=set(ck[i:j])
  		if(len(st)<k):
  			maxl=max(maxl,j-i)
  		j-=1
  	i+=1
  return maxl
  
for y in range(int(input())):
  print(cald())"""

def cald():
  n,k=map(int,input().split())
  ck=list(map(int,input().split()))
  maxl=0
  st=set(ck)
  if len(st)<k:
    return n
  ck.append(0)
  for i in range(1,k+1):
    ck[n]=i
    s=0
    for j in range(0,n+1):
      if(ck[j]==i):
        maxl=max(maxl,j-s)
        s=j+1
    if(maxl==n):
      break
  return maxl

for y in range(int(input())):
  print(cald())
import math
for j in range(int(input())):
  max_pr=0
  for i in range(int(input())):
    s,p,v=map(int,input().split())
    c=math.floor(p/(s+1))
    if c*v > max_pr:
      max_pr=c*v
  print(max_pr) 
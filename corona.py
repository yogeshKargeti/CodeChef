for k in range(int(input())) :
  i=int(input())
  inp_lt = list(map(int,input().split()))
  count=1
  mn=i
  mx=1
  for j in range(0,i-1):
    if inp_lt[j+1]-inp_lt[j] < 3:
      count+=1
    else :
      mn=min(mn,count)
      mx=max(mx,count)
      count=1 
  mn=min(mn,count)
  mx=max(mx,count)    
  print(mn,end="  ")
  print(mx)
def lower(lt,target):
  first=0
  last=len(lt)
  while(first<last):
    mid=int((first+last)/2)
    if(lt[mid]<target):
      first=mid+1
    else:
      last=mid
  if lt[first]==target:
    return first
  else:
    return first-1

def upper(lt,target):
  first=0
  last=len(lt)
  while(first<last):
    mid=int((first+last)/2)
    if(lt[mid]<target):
      first=mid+1
    else:
      last=mid
  return first


n,x,y=map(int,input().split())
mtime=0
t=[]
for i in range(n):
  p,q=map(int,input().split())
  t.append([p,q])
v=list(map(int,input().split()))
w=list(map(int,input().split()))
v.sort()
w.sort()
for i in t:
  stime=lower(v,i[0])
  etime=upper(w,i[1])
  if stime==-1 or etime==-1 or stime==x or etime==y:
    time=0
  else:
    time=w[etime]-v[stime]+1
  if mtime==0:
    mtime=time
  elif time<mtime and time!=0:
    mtime=time

print(mtime)
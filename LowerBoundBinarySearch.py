lt=[4,8,13,16,20,24,27]
target=28
first=0
last=len(lt)
while(first<last):
  mid=int((first+last)/2)
  if(lt[mid]<target):
    first=mid+1
  else:
    last=mid
print(first)
"""if lt[first]==target:
  print(lt[first],"  ",first)
else:
  print(lt[first-1],"  ",first-1)"""
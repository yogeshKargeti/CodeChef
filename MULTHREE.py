import math
for m in range(int(input())):
  num_ar=[2,4,8,6]
  af=0
  k,d0,d1=map(int,input().split())
  if k==2 or d0+d1==10 :
    s=d0+d1
  elif k==3 or ((d0+d1+((d0+d1)%10))%10==0) :
    s=d0+d1+((d0+d1)%10);
  else :
    rem=(d0+d1)%10;
    s=d0+d1;
    if rem%2==0 :
      k-=2
    else :
      s+=rem
      rem=(rem*2)%10
      k-=3
    s+=(20*math.floor(k/4))
    af=k%4
    for i in range(4):
      if rem==num_ar[i]:
        p=i
    while af>0 :
      s+=num_ar[p]
      p+=1
      if p==4:
        p=0
      af-=1
  if s%3==0 :
    print("YES")
  else :
    print("NO")

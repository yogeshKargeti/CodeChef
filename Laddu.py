import math

for i in range(int(input())):
  ac,org=input().split()
  lad=0
  for k in range(int(ac)):
    tas=input()
    if tas[0]=='C' :
      if tas[11]==' ' :
        p,k=tas.split()
        k=int(k)
        if(k>19) :
          lad+=300
        else:
          lad+=300+20-k
      else :
        lad+=50
    elif tas[0]=='T' :
      lad+=300
    elif tas[0]=='B' :
      p,k=tas.split()
      k=int(k)
      lad+=k
  print(lad)
  if(org=="INDIAN") :
    print(math.floor(lad/200))
  else :
    print(math.floor(lad/400))
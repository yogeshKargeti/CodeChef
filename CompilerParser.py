for j in range(int(input())):
  strin=input()
  l=len(strin)
  sta=0
  bp=-1
  maxl=0
  for i in range(l):
    if strin[i]=='<' :
      sta+=1
    else :
      sta-=1
    if sta==-1:
      bp=i
      sta=0
    if sta==0:
      maxl=max(maxl,(i-bp))
  print(maxl)
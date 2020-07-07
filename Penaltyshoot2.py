for j in range(int(input())):
  ts=int(input())
  s=input()
  sc=[0,0]
  rem=[ts,ts]
  i=0
  while i<(ts*2):
    if s[i]=='1':
      sc[0]+=1
    rem[0]-=1
    i+=1
    if sc[0]+rem[0] < sc[1] or sc[1]+rem[1] < sc[0]:
      break
    if s[i]=='1' :
      sc[1]+=1
    rem[1]-=1
    i+=1
    if sc[1]+rem[1] < sc[0] or sc[0]+rem[0] < sc[1]:
      break
  print(i)

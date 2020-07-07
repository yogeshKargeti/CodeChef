le=int(input())
string=input()
string="".join(string.split())
stack=0
start=0
dep=0
maxl=0
in_dep=0
in_maxl=0
for i in range(0,le):
  if string[i]=='1':
    stack+=1
    if stack>dep :
      dep=stack
      in_dep=i
  else:
    stack-=1
  if stack==0:
    if maxl < i-start :
      maxl=i-start+1
      in_maxl=start
    start=i+1
print(str(dep)+" "+str(in_dep+1)+" "+str(maxl)+" "+str(in_maxl+1))

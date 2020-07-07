for j in range(int(input())) :
  n,q=map(int,input().split())
  st=input()
  l=[0]*26
  for i in st:
    l[ord(i)-97]+=1
  for k in range(q):
    s=0
    c=int(input())
    final_list= list(map(lambda x:x-c, l))
    for i in final_list:
      if(i>0) :
        s+=i
    print(s)
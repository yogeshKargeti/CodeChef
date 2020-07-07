for i in range(int(input())):
  no=int(input())
  tok_lt=list(map(int,input().split()))
  tok=0
  minn=no
  for i in tok_lt:
    if i<minn :
      minn=i
    tok+=minn
  print(tok)
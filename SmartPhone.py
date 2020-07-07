n=int(input())
price_ar=[]
max_rev=0
for i in range(n):
  price_ar.append(int(input()))
price_ar.sort()
for i in range(n):
  if(max_rev<((n-i)*price_ar[i])) :
    max_rev=(n-i)*price_ar[i]
print(max_rev)
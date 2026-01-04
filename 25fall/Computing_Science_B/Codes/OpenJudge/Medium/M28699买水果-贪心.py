from collections import defaultdict
n,m=map(int,input().split())
price=list(map(int,input().split()))
fruit=defaultdict(int)
for i in range(m):
    name=input()
    fruit[name]+=1
a,b=0,0
price1=sorted(price)
price2=sorted(price,reverse=True)
for i in sorted(fruit,key=lambda x:fruit[x],reverse=True):
    a+=price2[-1]*fruit[i]
    b+=price1[-1]*fruit[i]
    price1.pop()
    price2.pop()
print(a,b)

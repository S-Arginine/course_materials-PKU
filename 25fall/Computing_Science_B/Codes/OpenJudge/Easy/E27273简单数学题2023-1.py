t=int(input())
result=[]
for i in range(t):
    n=int(input())
    total1=(1+n)*n//2
    total2=0
    n2=1
    while n2<=n:
        total2+=n2
        n2=n2*2
    total1-=total2*2
    result.append(total1)
for i in result:
    print(i)
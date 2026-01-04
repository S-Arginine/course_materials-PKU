from math import sqrt
def prime(x):
    s=set(range(2,x+1))
    for i in range(2,int(sqrt(x))+1):
        if i in s:
            s-={i*k for k in range(2,x//i+1)}
    if x in s:
        return 'YES'
    else:
        return 'NO'
n=int(input())
l=[]
l1=list(map(int,input().split()))
for p in l1:
    num=sqrt(p)
    m=int(num)
    if m==num:
        if m==1:
            l.append('NO')
        else:
            l.append(prime(m))
    else:
        l.append('NO')
for i in l:
    print(i)


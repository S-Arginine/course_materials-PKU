from math import sqrt
from functools import lru_cache
@lru_cache(maxsize=None)
def prime(x):
    l=[True]*(x+1)
    l[0:2]=[False]*2
    for i in range(2,int(sqrt(x))+1):
        if l[i]:
            l[i*2:x+1:i]=[False]*(x//i-1)
    return l[x]
n=int(input())
num=list(map(int,input().split()))
s=[]
for j in num:
    p,q=int(sqrt(j)),sqrt(j)
    if p==q:
        if p==3 or p==2:
            s.append('YES')
        elif p%6==1 or p%6==5:
            if prime(p):
                s.append('YES')
            else:
                s.append('NO')
        else:
            s.append('NO')
    else:
        s.append('NO')
for i in s:
    print(i)

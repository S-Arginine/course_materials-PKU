import sys
from functools import lru_cache
@lru_cache(maxsize=None)
def f(x):
    if x==1:
        return 1
    elif x==2:
        return 2
    else:
        return 2*f(x-1)+f(x-2)
n=int(input())
l=[]
for i in range(n):
    k=int(input())
    l.append(f(k)%32767)
sys.stdout.write('\n'.join(map(str,l))+'\n')

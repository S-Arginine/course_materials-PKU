import sys
from functools import lru_cache
from collections import deque
n=int(input())
out=[]
@lru_cache(maxsize=None)
def pell(x):
    lst=deque([0,1])
    if x==1:
        return 1
    else:
        for j in range(1,x):
            a=lst[1]*2+lst[0]
            if a>=32767:
                a=a%32767
            lst.append(a)
            lst.popleft()
        return lst[1]
for i in range(n):
    k=int(input())
    out.append(pell(k))
sys.stdout.write('\n'.join(map(str,out))+'\n')

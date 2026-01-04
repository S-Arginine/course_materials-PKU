import sys
import math
def solve():
    n=int(input())
    data=sys.stdin.readline().strip().split()
    l=[int(i) for i in data]
    b,c=[math.inf]*2,[math.inf]*2
    b[0],b[1]=l[0],0
    c[0],c[1]=min(b[0],b[1])+l[1],0
    for i in range(3,n+1):
        d=[math.inf]*2
        d[0]=min(c[0],c[1])+l[i-1]
        d[1]=min(c[0],b[0])
        b,c=c,d
    print(min(c[0],c[1]))
solve()
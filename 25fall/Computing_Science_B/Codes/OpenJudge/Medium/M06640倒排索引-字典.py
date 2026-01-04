from collections import defaultdict
N=int(input())
d=defaultdict(list)
for i in range(N):
    lst=input().split()
    n=int(lst[0])
    del lst[0]
    d[i+1]=lst
M=int(input())
num=defaultdict(list)
for i in range(M):
    s=input()
    for j in range(1,N+1):
        if s in d[j]:
            num[i].append(str(j))
    if not num[i]:
        num[i].append('NOT FOUND')
for val in num.values():
    print(' '.join(val))

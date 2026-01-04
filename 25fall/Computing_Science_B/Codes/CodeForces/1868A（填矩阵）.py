from collections import deque
t=int(input())
ls=[]  #放s
l=[]   #放矩阵
for i in range(t):
    n,m=map(int,input().split())
    if m==1:
        ls.append(0)
        l.append([[0]]*n)
    else:
        dq=deque(sorted(range(m),reverse=True))
        matrix=[]
        ls.append(min(n+1,m))
        for j in range(n):
            if j<m-1:
                a=dq.pop()
                dq.appendleft(a)
                matrix.append(list(dq))
            else:
                matrix.append(matrix[-1])
        l.append(matrix)
for p in range(t):
    print(ls[p])
    for q in l[p]:
        print(' '.join(map(str,q)))

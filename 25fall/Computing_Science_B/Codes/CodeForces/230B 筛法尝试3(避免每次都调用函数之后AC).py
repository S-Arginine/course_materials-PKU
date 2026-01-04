from math import sqrt
l=[True]*1000001
l[0:2]=[False]*2
for i in range(2,1001):
    if l[i]:
        l[i*2:1000001:i]=[False]*(1000000//i-1)
n=int(input())
num=list(map(int,input().split()))
s=[]
for i in num:
    p=sqrt(i)
    q=int(p)
    if q==p:
        if q==2 or q==3:
            s.append('YES')
        elif q%6==1 or q%6==5:
            if l[q]:
                s.append('YES')
            else:
                s.append('NO')
        else:
            s.append('NO')
    else:
        s.append('NO')
for i in s:
    print(i)

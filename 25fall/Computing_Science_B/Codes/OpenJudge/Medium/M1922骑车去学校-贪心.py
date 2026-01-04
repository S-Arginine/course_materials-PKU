import math
l3=[]
i=int(input())
while i!=0:
    a,b=[],[]
    for j in range(i):
        l1=list(map(int,input().split()))
        if l1[1]>=0:
            a.append(l1[0])
            b.append(l1[1])
    l2 = [4500/a[k]*3.6+b[k] for k in range(len(a))]
    t=min(l2)
    l3.append(math.ceil(t))
    i=int(input())
for num in l3:
    print(num)







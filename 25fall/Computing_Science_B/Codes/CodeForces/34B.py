def f(x):
    m=0
    for i in x:
        if i<=0:
            m+=1
    return m
l=list(map(int,input().split()))
a,b,n=l[0],l[1],0
num_list=list(map(int,input().split()))
if b>=f(num_list):
    for j in num_list:
        if j<=0:
            n+=-j
else:
    for k in range(b):
        n+=-(sorted(num_list)[k])
print(n)


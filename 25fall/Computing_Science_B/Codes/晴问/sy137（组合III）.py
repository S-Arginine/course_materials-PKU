from collections import defaultdict
n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
d=defaultdict(int)
for i in l:
    d[i]+=1
l=list(d.keys())
result=[]
def f(x,r,s):
    if len(s)==k:
        r.append(s[:])
        return
    else:
        for j in range(len(x)):
            if d[x[j]]!=0:
                s.append(x[j])
                d[x[j]]-=1
                f(x[j:],r,s)
                d[x[j]]+=1
                s.pop()
f(l,result,[])
for i in result:
    print(' '.join([str(j)for j in i]))
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(int)
re=[]
for i in l:
    d[i]+=1
def f(x,result,s):
    if sum(d.values())==0:
        result.append(s[:])
        return
    else:
        for key in x.keys():
            if x[key]>0:
                s.append(key)
                x[key]-=1
                f(x,result,s)
                x[key]+=1
                s.pop()
f(d,re,[])
for i in re:
    print(' '.join([str(j)for j in i]))




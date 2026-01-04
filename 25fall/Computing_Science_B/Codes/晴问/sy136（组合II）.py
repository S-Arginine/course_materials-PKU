n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
result=[]
def f(x,r,s):
    if len(s)==k:
        r.append(s[:])
        return
    else:
        for j in range(len(x)):
            s.append(x[j])
            f(x[j+1:],r,s)
            s.pop()
f(l,result,[])
for i in result:
    print(' '.join([str(j)for j in i]))

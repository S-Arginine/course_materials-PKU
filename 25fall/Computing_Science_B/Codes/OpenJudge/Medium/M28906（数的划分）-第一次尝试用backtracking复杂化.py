n,k=map(int,input().split())
s=set()
def f(x,y,l):
    if y>1:
        for i in range(1,x//2+1):
            l.append(i)
            f(x-i,y-1,l)
            l.pop()
    elif y==1:
        l.append(x)
        l1=sorted(l)
        s.add(tuple(l1))
        l.pop()
f(n,k,[])
print(s)

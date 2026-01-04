def g():
    n,m=map(int,input().split())
    matrix=[]
    for i in range(n):
        l=list(map(int,input().split()))
        matrix.append(l)
    result,count=[],n*m
    lst=[(-1,0),(0,1),(1,0),(0,-1)]
    def f(x,y,r,c):
        nonlocal result,count
        if matrix[x][y]==0:
            r.append((x,y))
            matrix[x][y]=1
            c+=1
            if x==1 and y==1:
                if c<count:
                    count=c
                    result=r[:]
                return
            else:
                for dx,dy in lst:
                    xx,yy=x+dx,y+dy
                    if 0<=xx<n and 0<=yy<m:
                        f(xx,yy,r,c)
            matrix[x][y]=0
            r.pop()
    f(0,0,[],0)
    print(count)
    return result
for p,q in g():
    print(f'{p+1} {q+1}')


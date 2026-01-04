def g():
    T=int(input())
    result=[]
    d=[(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]
    def f(m,x,y):
        nonlocal k
        if sum([sum(_)for _ in m])==0:
            k+=1
            return
        else:
            for dx,dy in d:
                xx,yy=x+dx,y+dy
                if m[xx+2][yy+2]==1:
                    m[xx+2][yy+2]=0
                    f(m,xx,yy)
                    m[xx+2][yy+2]=1
    for i in range(T):
        N,M,X,Y=map(int,input().split())
        ma=[[0]*(M+4),[0]*(M+4)]
        for j in range(N):
            l=[0,0]
            l.extend([1]*M)
            l.extend([0,0])
            ma.append(l)
        ma.append([0]*(M+4))
        ma.append([0]*(M+4))
        k=0
        ma[X+2][Y+2]=0
        f(ma,X,Y)
        result.append(k)
    for num in result:
        print(num)
g()


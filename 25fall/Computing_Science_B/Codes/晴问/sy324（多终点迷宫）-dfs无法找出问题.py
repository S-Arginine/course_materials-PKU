def g():
    import sys
    from copy import deepcopy
    n,m=map(int,input().split())
    matrix=[]
    for i in range(n):
        matrix.append(list(map(int,sys.stdin.readline().split())))
    result=[[0]*m for i in range(n)]
    l=[(-1,0),(0,1),(1,0),(0,-1)]
    def f(x,y,p,q,c):
        nonlocal result,count
        if ma[x][y]==0:
            c+=1
            ma[x][y]=1
            if x==p and y==q:
                if 0<c<count:
                    count=c
                    result[p][q]=c
                return
            else:
                for dx,dy in l:
                    xx,yy=x+dx,y+dy
                    if 0<=xx<n and 0<=yy<m:
                        f(xx,yy,p,q,c)
            ma[x][y]=0
            c-=1
    for i in range(n):
        for j in range(m):
            ma=deepcopy(matrix)
            count=n*m
            if ma[i][j]==1:
                result[i][j]=-1
            else:
                f(0,0,i,j,0)
                if result[i][j]==0:
                    result[i][j]=-1
    for i in result:
        sys.stdout.write(' '.join([str(j) for j in i])+'\n')
g()

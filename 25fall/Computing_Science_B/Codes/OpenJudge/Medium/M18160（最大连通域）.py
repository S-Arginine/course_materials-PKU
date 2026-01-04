def f(i,j,m,t):
    if m[i][j]=='W':
        t+=1
        m[i][j]='.'
        return f(i-1,j-1,m,f(i,j-1,m,f(i+1,j-1,m,f(i-1,j,m,f(i+1,j,m,f(i-1,j+1,m,f(i,j+1,m,f(i+1,j+1,m,t))))))))
    else:
        return t
T=int(input())
result=[]
for p in range(T):
    N,M=map(int,input().split())
    matrix=[['.']*(M+2)]
    for q in range(N):
        matrix.append(['.']+list(input())+['.'])
    matrix.append(['.']*(M+2))
    x=0
    for c in range(1,N+1):
        for d in range(1,M+1):
            y=f(c,d,matrix,0)
            if y>x:
                x=y
    result.append(x)
for num in result:
    print(num)


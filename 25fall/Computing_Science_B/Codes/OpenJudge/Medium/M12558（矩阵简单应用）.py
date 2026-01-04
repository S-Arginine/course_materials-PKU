n,m=map(int,input().split())
A=[[0*i for i in range(m+2)]]
for i in range(n):
    A.append([0])
    A[i+1].extend(list(map(int,input().split())))
    A[i+1].append(0)
A.append([0*i for i in range(m+2)])
l=0
for i in range(1,n+1):
    for j in range(1,m+1):
        x=0
        if A[i][j]==1:
            if A[i-1][j]==0:
                x+=1
            if A[i][j-1]==0:
                x+=1
            if A[i+1][j]==0:
                x+=1
            if A[i][j+1]==0:
                x+=1
        l+=x
print(l)

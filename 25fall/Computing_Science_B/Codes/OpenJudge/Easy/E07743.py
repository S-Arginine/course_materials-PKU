l=list(map(int,input().split()))
m,n=l[0],l[1]
matrix=[list(map(int,input().split())) for _ in range(m)]
a=0
for i in range(m):
    for j in range(n):
        if i==0 or j==0 or i==m-1 or j==n-1:
            a+=matrix[i][j]
print(a)

l=list(map(int,input().split()))
m,n=l[0],l[1]
matrix=[list(map(int,input().split())) for _ in range(m)]
a=0
def f(x,y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]==y:
                return [i,j]
for item in matrix:
    lst=f(matrix,item)
    if 0 in lst or n-1 in lst or m-1 in lst:
        a+=item
print(a)

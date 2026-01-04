n=int(input())
l,matrix=[],[]
while True:
    s=input()
    if s:
       l.extend(list(map(int,s.split())))
    if len(l)==n*n:
        break
for i in range(n):
    matrix.append(l[i*n:(i+1)*n])
m=matrix[0][0]
for j in range(n):
    for i in range(j,n):
        global_max=sum(matrix[0][j:i+1])
        current_max=sum(matrix[0][j:i+1])
        for k in range(1,n):
            s=sum(matrix[k][j:i+1])
            current_max=max(current_max+s,s)
            global_max=max(current_max,global_max)
        m=max(global_max,m)
print(m)
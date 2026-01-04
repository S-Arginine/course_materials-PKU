import sys
def r():       #顺时针旋转：先把主对角线上下交换，再倒置每一列
    for i in range(n):
        for j in range(i+1,n):
            s[i][j],s[j][i]=s[j][i],s[i][j]
    for lst in s:
        lst.reverse()
    return
def c():
    for i in range(n):
        for j in range(n):
            if s[i][j]!='#':
                results.append(matrix[i][j])
    return
n=int(input())
s=[list(sys.stdin.readline().strip()) for i in range(n)]
matrix=[list(sys.stdin.readline().strip()) for j in range(n)]
results=[]
c()
for i in range(3):
    r()
    c()
print(''.join(results))
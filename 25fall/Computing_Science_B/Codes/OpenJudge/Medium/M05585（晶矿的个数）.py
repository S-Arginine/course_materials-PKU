k=int(input())
t=[]
def f(lst,x,y,m):
    if lst[x][y]==m:
        lst[x][y]='0'
        return f(f(f(f(lst,x,y+1,m),x+1,y,m),x,y-1,m),x-1,y,m)
    else:
        return lst
for i in range(k):
    n = int(input())
    matrix=[['0']*(n+2)]
    for j in range(n):
        l=['0']
        l+=list(input())
        l.append('0')
        matrix.append(l)
    matrix.append(['0']*(n+2))
    R,B=0,0
    for p in range(1,n+1):
        for q in range(1,n+1):
            if matrix[p][q]=='r':
                matrix=f(matrix,p,q,'r')
                R+=1
            elif matrix[p][q]=='b':
                matrix=f(matrix,p,q,'b')
                B+=1
    t.append([R,B])
for i in t:
    print(f'{i[0]} {i[1]}')
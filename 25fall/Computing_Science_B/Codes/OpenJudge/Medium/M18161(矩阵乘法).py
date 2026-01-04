A,B,C=[],[],[]
r1,c1=map(int,input().split())
for i in range(r1):
    A.append(list(map(int,input().split())))
r2,c2=map(int,input().split())
for i in range(r2):
    B.append(list(map(int,input().split())))
r3,c3=map(int,input().split())
for i in range(r3):
    C.append(list(map(int,input().split())))
if c1!=r2:
    print('Error!')
else:
    if r1!=r3 or c2!=c3:
        print('Error!')
    else:
        for i in range(r1):
            for j in range(c2):
                for m in range(c1):
                    C[i][j]+=A[i][m]*B[m][j]
                C[i][j]=str(C[i][j])
        for p in C:
            print(' '.join(p))
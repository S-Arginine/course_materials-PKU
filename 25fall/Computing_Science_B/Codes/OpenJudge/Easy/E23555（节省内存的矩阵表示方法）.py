from collections import defaultdict
n,m1,m2=map(int,input().split())
X,Y,Z=defaultdict(int),defaultdict(int),defaultdict(int)
for i in range(m1):
    row1,col1,val1=map(int,input().split())
    X[(row1,col1)]=val1
for i in range(m2):
    row2,col2,val2=map(int,input().split())
    Y[(row2,col2)]=val2
for row in range(n):
    for col in range(n):
        for i in range(n):
            if (row,i) in X and (i,col) in Y:
                Z[(row,col)]+=X[(row,i)]*Y[(i,col)]
for i in Z.keys():
    print(i[0],i[1],Z[i])



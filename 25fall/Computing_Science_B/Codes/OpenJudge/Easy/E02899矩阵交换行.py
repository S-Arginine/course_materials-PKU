matrix=[]
for i in range(5):
    matrix.append(input().split())
n,m=map(int,input().split())
if n>=5 or m>=5:
    print('error')
else:
    l1,l2=matrix[n],matrix[m]
    matrix[n],matrix[m]=l2,l1
for i in range(5):
    print(' '.join(f"{num:4}"for num in matrix[i]))


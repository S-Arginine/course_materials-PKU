def f(n):
    a,b,c=n//100,n//10%10,n%10
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
l=list(map(int,input().split()))
x,y=l[0],l[1]
num_list=[]
for i in range(x,y+1):
    if f(i):
        num_list.append(str(i))
if len(num_list)==0:
    print('NO')
else:
    print(' '.join(num_list))

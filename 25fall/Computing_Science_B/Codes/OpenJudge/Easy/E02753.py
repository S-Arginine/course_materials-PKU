def f(x):
    a,b=1,1
    if x==1:
        return a
    if x==2:
        return b
    if x>=3:
        for p in range(3,x+1):
            if p%2!=0:
               a=a+b
            elif p%2==0:
               b=b+a
        return max(a,b)
    else:
        return 'Error'
n=int(input())
num_list=[]
for q in range(1,n+1):
    y=int(input())
    num_list.append(f(y))
for num in num_list:
    print(num)

def g(x):
    b=0
    for p in range(1,x+1):
        if x%p==0:
            b+=1
    return b
def f(x):
    a=0
    for q in range(1,x+1):
        if g(q)%2!=0:
            a+=1
    return a
n=int(input())
num_list=[]
for i in range(1,n+1):
    y=int(input())
    num_list.append(f(y))
for num in num_list:
    print(num)

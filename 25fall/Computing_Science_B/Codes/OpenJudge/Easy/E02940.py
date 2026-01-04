num_list=list(map(int,input().split()))
a=num_list[0]
b=num_list[1]
n=0
def f(x,y):
    m=0
    for i in range(0,y):
        m+=x*10**i
    return m
for p in range(1,b+1):
    n+=f(a,p)
print(n)

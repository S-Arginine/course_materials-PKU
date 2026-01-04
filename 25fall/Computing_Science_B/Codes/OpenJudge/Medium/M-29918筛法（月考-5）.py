def f(x):
    num=[]
    l=[1 for i in range(x+1)]
    for i in range(2,x+1):
        for k in range(2,x//i+1):
            l[k*i]+=i
    for i in range(2,x+1):
        a=l[i]
        if i<a<=x and l[a]==i:
            num.append((i,a))
    return num
n=int(input())
for item in f(n):
    print(f"{item[0]} {item[1]}")



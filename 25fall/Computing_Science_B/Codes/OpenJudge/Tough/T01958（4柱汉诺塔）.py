def f3(x):
    return 2**x-1
def f4(x):
    if x>1:
        l=[]
        for i in range(1,x):
            l.append(f4(x-i)*2+f3(i))
        return min(l)
    elif x==1:
        return 1
lst=[f4(j) for j in range(1,13)]
for j in lst:
    print(j)

from math import sqrt
def f(x):
    l=[]
    for i in range(2,int(sqrt(x))+1):
        if x%i==0:
            l.append(i)
            l.append(x//i)
    return sum(l)+1
n=int(input())
lst=[]
for i in range(1,n+1):
    for j in range(i+1,n+1):
        if f(i)==j and f(j)==i:
            lst.append(str(i)+' '+str(j))
            break
for item in lst:
    print(item)
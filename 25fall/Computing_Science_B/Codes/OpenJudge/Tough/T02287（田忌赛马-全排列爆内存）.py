from collections import defaultdict
def f(x,r,s):    #构造全排列
    if sum(x.values())==0:
        r.append(s[:])
        return
    else:
        for key in x.keys():
            if x[key]>0:
                s.append(key)
                x[key]-=1
                f(x,r,s)
                x[key]+=1
                s.pop()
n=int(input())
l=[]
while n!=0:
    tian=list(map(int,input().split()))
    king=list(map(int,input().split()))
    d=defaultdict(int)
    for i in king:
        d[i]+=1
    result=[]
    f(d,result,[])   #把其中一个列表全排列
    money=-n
    for item in result:
        t=0
        for i in range(n):
            if tian[i]>item[i]:
                t+=1
            elif tian[i]<item[i]:
                t-=1
        if t>money:
            money=t
    l.append(money)
    n=int(input())
for num in l:
    print(200*num)


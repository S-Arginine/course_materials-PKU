from collections import defaultdict
d=defaultdict(int)
n=int(input())
X,qujian,num=[],[],0
for i in range(n):
    x,h=map(int,input().split())
    d[x]=h
    X.append(x)
for i in range(n):
    if i==0:
        qujian.append([X[i]-d[X[i]],X[i]])
        num+=1
    elif 1<=i<=n-2:
        if X[i]-d[X[i]]>max(qujian[-1][1],X[i-1]):
            num+=1
            qujian.append([X[i]-d[X[i]],X[i]])
        else:
            if X[i]+d[X[i]]<X[i+1]:
                num+=1
                qujian.append([X[i],X[i]+d[X[i]]])
    elif i==n-1:
        num+=1
print(num)
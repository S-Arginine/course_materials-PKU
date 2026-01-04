import sys
n,b=map(int,input().split())
d={}
price=list(map(int,sys.stdin.readline().split()))
weight=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    d[weight[i]]=price[i]
dp=[0]*(b+1)
for key in d.keys():
    if key>b:
        del d[key]
weight=sorted(list(d.keys()))
for i in weight:
    dp[i]=d[i]
for i in range(1,b+1):
    l=[]
    for k in range(0,i//2+1):
        if i-k!=k:
            l.append(dp[i-k]+dp[k])
    dp[i]=max(l)
print(dp[b])



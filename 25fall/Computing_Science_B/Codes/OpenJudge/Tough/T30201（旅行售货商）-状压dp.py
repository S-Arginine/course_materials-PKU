import math
n=int(input())
cost=[list(map(int,input().split())) for i in range(n)]
size=1<<n
dp=[[math.inf]*n for _ in range(size)]
dp[1][0]=0
for i in range(1,size):
    if not i&(1>>0):
        continue
    for j in range(n):
        if dp[i][j]==math.inf:
            continue
        if not i&(1<<j):
            continue
        for k in range(n):
            if i&(1<<k):
                continue
            i_=i|(1<<k)
            dp[i_][k]=min(dp[i][j]+cost[j][k],dp[i_][k])
result=min(dp[size-1][i]+cost[i][0] for i in range(1,n))
print(result)

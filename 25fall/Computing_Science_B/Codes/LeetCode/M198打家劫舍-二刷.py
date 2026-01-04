import sys
n=int(input())
l=list(map(int,sys.stdin.readline().strip().split()))
dp=[0]*(n+1)   #dp[i]表示选第i个时的最小值
dp[1]=l[0]
dp[2]=max(l[0],l[1])
for i in range(3,n+1):
    dp[i]=max(dp[i-2]+l[i-1],dp[i-3]+l[i-1])
print(max(dp))

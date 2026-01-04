import math
l=list(map(int,input().split(',')))
n=len(l)
not_del_dp,del_dp=[-math.inf]*n,[-math.inf]*n
not_del_dp[0]=l[0]
result=l[0]
for i in range(1,n):
    not_del_dp[i]=max(l[i],not_del_dp[i-1]+l[i])
    del_dp[i]=max(not_del_dp[i-1],del_dp[i-1]+l[i])
    result=max(result,not_del_dp[i],del_dp[i])
print(result)

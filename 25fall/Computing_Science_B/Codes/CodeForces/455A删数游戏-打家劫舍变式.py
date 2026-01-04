import sys
from collections import defaultdict
n=int(input())
l=list(map(int,sys.stdin.readline().strip().split()))
d=defaultdict(int)
for i in l:
    d[i]+=1
nums=sorted(list(d.keys()))
x=len(nums)
dp=[0]*(nums[-1]+1)   #dp[i]表示删数为i时的最大得分
dp[nums[0]]=nums[0]*d[nums[0]]
dp[1],dp[2]=d[1],max(d[1],2*d[2])
for i in range(3,nums[-1]+1):
    dp[i]=max(dp[i-2]+d[i]*i,dp[i-3]+d[i]*i)
print(max(dp))

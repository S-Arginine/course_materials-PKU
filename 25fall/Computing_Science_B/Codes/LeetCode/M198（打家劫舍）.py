nums=list(map(int,input().split()))
dp=[0]*(len(nums)+1)
for i in range(1,len(nums)+1):
    if i==1:
        dp[i]=nums[0]
    elif i==2:
        dp[i]=max(nums[0],nums[1])
    elif i==3:
        dp[i]=max(nums[1],nums[0]+nums[2])
    else:
        if dp[i-1]-dp[i-3]!=nums[i-2]:
            dp[i]=dp[i-2]+nums[i-1]
        else:
            dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
print(dp[-1])
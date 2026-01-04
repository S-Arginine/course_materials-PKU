n,a,b,c=map(int,input().split())   #背包容量为n，有3个物品每个价值为1且可以用无数次
l=list({a,b,c})
dp=[-float('inf')]*(n+1)  #dp[i]表示恰好装满i容量时的最大价值
dp[0]=0
for i in range(1,n+1):
    for j in l:
        if i>=j:
            dp[i]=max(dp[i],dp[i-j]+1)
print(dp[-1])

n=int(input())
dp=[float('inf')]*(n+1)
dp[0],dp[1]=0,1
for i in range(2,n+1):
    x=1
    result=float('inf')
    while x*x<=i:
        result=min(result,dp[i-x*x]+1)
        x+=1
    dp[i]=result
print(dp[n])
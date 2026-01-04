t,k=map(int,input().split())
e=10**9+7
result=[]
num=[]
for i in range(t):
    a,b=map(int,input().split())
    num.append((a,b))
c=max(i[1]for i in num)
dp=[0]*(c+1)
dp[0]=1
dp_sum=[0]*(c+1)
dp_sum[0]=1
for i in range(1,c+1):
    dp[i]+=dp[i-1]
    if i>=k:
        dp[i]+=dp[i-k]
    if dp[i]>=e:
        dp[i]-=e
    if i>=1:
        dp_sum[i]=dp_sum[i-1]+dp[i]
    if dp_sum[i]>=e:
        dp_sum[i]-=e
for a,b in num:
    s=dp_sum[b]-dp_sum[a-1]
    s=s%e
    result.append(s)
for i in result:
    print(i)

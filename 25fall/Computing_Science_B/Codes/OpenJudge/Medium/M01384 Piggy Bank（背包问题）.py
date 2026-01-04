t=int(input())
result=[]
for i in range(t):
    weight0,weight1=map(int,input().split())
    W=weight1-weight0
    n=int(input())
    dp=[float('inf')]*(W+1)
    dp[0]=0
    v,w=[],[]
    for j in range(n):
        a,b=map(int,input().split())
        v.append(a)
        w.append(b)
    for j in range(n):
        for k in range(w[j],W+1):
            dp[k]=min(dp[k],dp[k-w[j]]+v[j])
    if dp[W]==float('inf'):
        result.append('This is impossible.')
    else:
        result.append(f'The minimum amount of money in the piggy-bank is {dp[W]}.')
for i in result:
    print(i)



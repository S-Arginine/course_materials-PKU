def solve():
    n,k=map(int,input().split())
    result=0
    def dfs(start,end,t):
        nonlocal result
        if t==1:
            result+=1
            return
        for i in range(start,end//t+1):
            dfs(i,end-i,t-1)
    dfs(1,n,k)
    print(result)
solve()

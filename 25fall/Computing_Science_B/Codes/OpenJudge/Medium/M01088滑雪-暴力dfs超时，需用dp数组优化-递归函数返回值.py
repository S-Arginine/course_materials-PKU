def solve():
    import sys
    n,m=map(int,input().split())
    matrix=[list(map(int,sys.stdin.readline().strip().split())) for i in range(n)]
    directions=[(-1,0),(0,-1),(1,0),(0,1)]
    dp=[[0]*m for i in range(n)]
    def dfs(x,y):
        if dp[x][y]!=0:
            return dp[x][y]
        dp[x][y]=1
        for dx,dy in directions:
            xx,yy=x+dx,y+dy
            if 0<=xx<n and 0<=yy<m:
                if matrix[x][y]>matrix[xx][yy]:
                    dp[x][y]=max(dp[x][y],1+dfs(xx,yy))
        return dp[x][y]
    result=1
    for i in range(n):
        for j in range(m):
            result=max(result,dfs(i,j))
    print(result)
    return
solve()
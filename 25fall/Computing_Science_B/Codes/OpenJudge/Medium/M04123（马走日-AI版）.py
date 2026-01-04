def solve():
    directions=[(-2,-1),(-1,-2),(1,-2),(2,-1),(2,1),(1,2),(-1,2),(-2,1)]
    def dfs(x, y, count):
        nonlocal total
        if count==n*m:
            total+=1
            return
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
                visited[nx][ny]=True
                dfs(nx,ny,count+1)
                visited[nx][ny]=False
    T=int(input())
    for _ in range(T):
        n,m,x,y=map(int,input().split())
        visited=[[False] * m for _ in range(n)]
        total=0
        visited[x][y]=True
        dfs(x,y,1)
        print(total)
solve()
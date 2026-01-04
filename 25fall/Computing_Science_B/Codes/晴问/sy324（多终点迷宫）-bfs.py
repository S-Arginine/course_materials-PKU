from collections import deque
def solve():
    n,m=map(int, input().split())
    grid=[list(map(int, input().split())) for _ in range(n)]
    dist=[[-1]*m for _ in range(n)]
    if grid[0][0]==1:
        for row in dist:
            print(' '.join(map(str, row)))
        return
    q=deque()
    q.append((0,0))
    dist[0][0]=0
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        x,y=q.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if grid[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    for row in dist:
        print(' '.join(map(str, row)))
solve()

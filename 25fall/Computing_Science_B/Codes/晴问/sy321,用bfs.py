from collections import deque
n,m=map(int,input().split())
matrix=[list(map(int,input().split())) for i in range(n)]
def bfs(graph,start):
    queue=deque([start])
    visited=set([start])
    directions=[(-1,0),(0,1),(1,0),(0,-1)]
    parent,result={},deque([])
    parent[(start[0],start[1])]=None
    while queue:
        x,y=queue.popleft()
        if x==n-1 and y==m-1:
            break
        for dx,dy in directions:
            xx,yy=x+dx,y+dy
            if 0<=xx<n and 0<=yy<m:
                if graph[xx][yy]==0 and (xx,yy) not in visited:
                    parent[(xx,yy)]=(x,y)
                    visited.add((xx,yy))
                    queue.append((xx,yy))
    current=(n-1,m-1)
    while current is not None:
        result.appendleft(current)
        current=parent[current]
    for x,y in result:
        print(f'{x+1} {y+1}')
bfs(matrix,(0,0))
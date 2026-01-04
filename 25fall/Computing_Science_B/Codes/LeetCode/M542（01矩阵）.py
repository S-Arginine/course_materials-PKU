n=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
l=[lst[0] for lst in mat]
n=len(l)
m=len(mat[0])
result=[[0]*m for j in range(n)]
from collections import deque
def bfs(graph,start):
    queue=deque([start])
    visited=set(queue)
    directions=[(0,1),(1,0),(0,-1),(-1,0)]
    parent={}
    parent[start]=None
    while queue:
        coordinate=queue.popleft()
        x,y=coordinate[0],coordinate[1]
        if graph[x][y]==0:
            current=(x,y)
            t=0
            while current is not None:
                t+=1
                current=parent[current]
            result[start[0]][start[1]]=t-1
            return
        else:
            for dx,dy in directions:
                xx,yy=x+dx,y+dy
                if 0<=xx<n and 0<=yy<m and (xx,yy) not in visited:
                    queue.append((xx,yy))
                    visited.add((xx,yy))
                    parent[(xx,yy)]=(x,y)
for i in range(n):
    for j in range(m):
        if mat[i][j]==1:
            bfs(mat,(i,j))
print(result)

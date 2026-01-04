n=int(input())
mat=[list(map(int,input().split())) for i in range(n)]
l=[lst[0] for lst in mat]
n,m=len(l),len(mat[0])
result=[[-1]*m for j in range(n)]
from collections import deque
queue=deque()
visited=set()
for i in range(n):
    for j in range(m):
        if mat[i][j]==0:
            result[i][j]=0
            queue.append((i,j))
directions=[(1,0),(0,1),(-1,0),(0,-1)]
print(queue)
while queue:
    c=queue.popleft()
    x,y=c[0],c[1]
    for dx,dy in directions:
        xx,yy=x+dx,y+dy
        if 0<=xx<n and 0<=yy<m and (xx,yy) not in visited:
            queue.append((xx,yy))
            visited.add((xx,yy))
            if mat[xx][yy]==1:
                result[xx][yy]=result[x][y]+1
print(result)

from collections import deque
def bfs(end):
    while queue:
        x=queue.popleft()
        if x==end:
            return
        else:
            x1=x*3
            if x1 not in visited:
                parent[x1]=x
                visited.add(x1)
                queue.append(x1)
            x2=x//2
            if x2 not in visited:
                parent[x2]=x
                visited.add(x2)
                queue.append(x2)
n,m=map(int,input().split())
result=[]
while n+m!=0:
    queue=deque([n])
    parent={n:-1}
    visited={n}
    bfs(m)
    y,t=m,0
    current=[]
    while parent[y]!=-1:
        t+=1
        if y==parent[y]*3:
            current.append('H')
        elif y==parent[y]//2:
            current.append('O')
        y=parent[y]
    current.reverse()
    result.append((t,current))
    n,m=map(int,input().split())
for t,current in result:
    print(t)
    print(''.join(current))

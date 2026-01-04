from collections import deque
n=int(input())
nums=[]
def bfs(x):
    if x==1:
        return 1
    else:
        queue=deque([1])
        visited=[False]*x
        visited[1]=True
        directions=[0,1]
        parent,mod={},{}
        parent[1],mod[1]=None,1
        result=deque([])
        while queue:
            a=queue.popleft()
            if a==0:
                break
            for i in directions:
                k=(a*10+i)%x
                if not visited[k]:
                    visited[k]=True
                    queue.append(k)
                    parent[k]=a
                    mod[k]=i
        current=0
        while current is not None:
            result.appendleft(mod[current])
            current=parent[current]
        return ''.join([str(i) for i in result])
while n!=0:
    print(bfs(n))
    n=int(input())
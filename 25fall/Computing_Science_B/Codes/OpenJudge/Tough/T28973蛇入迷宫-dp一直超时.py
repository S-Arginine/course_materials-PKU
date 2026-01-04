from collections import deque   #易错点：当蛇头的位置确定时，蛇实际上有两种状态，需要予以区分
def solve():
    n=int(input())
    matrix=[list(map(int,input().split())) for i in range(n)]
    start_node=((0,1),(0,0),0)
    queue=deque([start_node])
    visited={((0,1),(0,0))}
    target_head=(n-1,n-1)
    target_tail=(n-1,n-2)
    while queue:
        head,tail,steps=queue.popleft()
        hr,hc=head
        tr,tc=tail
        if head==target_head and tail==target_tail:
            print(steps)
            return
        def try_add(nh,nt):
            if (nh,nt) not in visited:
                visited.add((nh,nt))
                queue.append((nh,nt,steps+1))
        if hr==tr:
            if hc+1 < n:
                if matrix[hr][hc+1] == 0:
                    try_add((hr,hc+1),(tr,tc+1))
            if hr+1<n:
                if matrix[hr+1][tc]==0 and matrix[hr+1][hc]==0:
                    try_add((hr+1,hc),(tr+1,tc))
            if hr+1<n:
                if matrix[hr+1][tc]==0 and matrix[hr+1][hc] == 0:
                    try_add((hr+1,tc),(tr,tc))
        else:
            if tc+1<n:
                if matrix[tr][tc+1]==0 and matrix[hr][hc+1]==0:
                    try_add((hr,hc+1),(tr,tc+1))
            if hr+1<n:
                if matrix[hr+1][hc]==0:
                    try_add((hr+1,hc),(tr+1,tc))
            if tc+1<n:
                if matrix[tr][tc+1]==0 and matrix[hr][hc+1]==0:
                    try_add((tr,tc+1),(tr,tc))
    print("-1")
solve()
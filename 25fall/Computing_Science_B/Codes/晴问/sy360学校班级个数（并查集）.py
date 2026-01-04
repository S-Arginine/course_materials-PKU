n,m=map(int,input().split())
parent=[i for i in range(n+1)]
count=n
def find(x):
    if parent[x]!=x:
        parent[x]=find(parent[x])
    return parent[x]
for i in range(m):
    a,b=map(int,input().split())
    a_class=find(a)   #找到最终父节点
    b_class=find(b)
    if a_class!=b_class:
        parent[a_class]=b_class
        count-=1
print(count)
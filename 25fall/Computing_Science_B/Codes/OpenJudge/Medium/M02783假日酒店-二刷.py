n=int(input())
result=[]
while n>0:
    l=[tuple(map(int,input().split())) for i in range(n)]
    t=0
    l.sort(key=lambda x:x[1])
    l.sort(key=lambda x:x[0])
    min_cost=float('inf')
    for dis,cost in l:
        if cost<min_cost:
            t+=1
            min_cost=cost
    result.append(t)
    n=int(input())
for i in result:
    print(i)

import heapq
n=int(input())
stations=[list(map(int,input().split())) for i in range(n)]
L,P=map(int,input().split())
position=[]
for i in range(n):
    position.append((L-stations[i][0],stations[i][1]))
position.append((L,0))
position.sort()
distance,gas=0,P
heap=[]
previous=0
t=0    #计数
for i in range(0,n+1):
    d=position[i][0]-previous
    flag=True
    while gas<d:
        if not heap:
            flag=False
            break
        petrol=-heapq.heappop(heap)
        gas+=petrol
        t+=1
    if not flag:
        t=-1
        break
    gas-=d
    previous=position[i][0]
    heapq.heappush(heap,-position[i][1])
print(t)




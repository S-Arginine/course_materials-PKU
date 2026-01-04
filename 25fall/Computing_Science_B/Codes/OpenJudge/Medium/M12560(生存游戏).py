import copy
def g(x,y):
    lst=[ma[x-1][y-1],ma[x][y-1],ma[x+1][y-1],ma[x-1][y],ma[x+1][y],ma[x-1][y+1],ma[x][y+1],ma[x+1][y+1]]
    return lst.count(1)
n,m=map(int,input().split())
ma=[[-1 for i in range(m+2)]]
for i in range(n):
    ma.append([-1])
    ma[i+1].extend(list(map(int,input().split())))
    ma[i+1].append(-1)
ma.append([-1 for j in range(m+2)])
ma1=copy.deepcopy(ma)
for p in range(1,n+1):
    for q in range(1,m+1):
        if ma[p][q]==0:
            if g(p,q)==3:
                ma1[p][q]=1
            else:
                ma1[p][q]=0
        elif ma[p][q]==1:
            if g(p,q)<2 or g(p,q)>3:
                ma1[p][q]=0
            else:
                ma1[p][q]=1
for i in range(1,n+1):
    l=[str(ma1[i][j]) for j in range(1,m+1)]
    print(' '.join(l))

l=list(map(int,input().split()))
result=[]
while sum(l)!=0:
    total=l[2]//4+l[3]+l[4]+l[5]   #箱子的最少总数量
    l[0]=max(0,l[0]-11*l[4])
    a=min(l[3]*20,l[1]*4)   #4*4填2*2耗掉的格子
    l[1]=max(0,l[1]-l[3]*5)
    l[0]=max(0,l[0]-l[3]*20+a)
    x=l[2]%4
    if x!=0:
        b=4-x
        total+=1
        c=min(4*(2*b-1),4*l[1])  #3*3填2*2耗掉的格子
        l[1]=max(0,l[1]-2*b+1)
        l[0]=max(0,l[0]-(4*(2*b-1)-c))
    total+=l[1]//9
    d=l[1]%9
    if d!=0:
        total+=1
        l[0]=max(0,l[0]-36+d*4)
    total+=l[0]//36
    e=l[0]%36
    if e!=0:
        total+=1
    result.append(total)
    l=list(map(int,input().split()))
for i in result:
    print(i)

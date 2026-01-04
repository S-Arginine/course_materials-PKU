from math import ceil
flag=True
x=[]
while flag:
    l=list(map(int,input().split()))
    a=l[5]+l[4]+l[3]+l[2]//4
    l[0]=max(0,l[0]-l[4]*11)
    if l[1]-l[3]*5>0:
        l[1]-=l[3]*5
    else:
        l[0]=max(0,l[0]-4*(l[3]*5-l[1]))
        l[1]=0
    if l[2]%4==1:
        a+=1
        if l[1]-5>0:
            l[1]-=5
            l[0]=max(0,l[0]-7)
        else:
            l[0]=max(0,l[0]-(27-4*l[1]))
            l[1]=0
    elif l[2]%4==2:
        a+=1
        if l[1]-3>0:
            l[1]-=3
            l[0]=max(0,l[0]-6)
        else:
            l[0]=max(0,l[0]-(18-4*l[1]))
            l[1]=0
    elif l[2]%4==3:
        a+=1
        if l[1]-1>0:
            l[1]-=1
            l[0]=max(0,l[0]-5)
        else:
            l[0]=max(0,l[0]-(9-4*l[1]))
            l[1]=0
    if l[1]!=0:
        if l[1]%9==0:
            a+=l[1]//9
        else:
            a+=l[1]//9+1
            l[0]=max(0,l[0]-(36-l[1]%9*4))
    if l[0]!=0:
        a+=ceil(l[0]/36)
    if a==0:
        flag=False
    else:
        x.append(a)
for i in x:
    print(i)










n=int(input())
group=list(map(int,input().split()))
taxi=0
num=[group.count(i)for i in range(1,5)]
x=min(num[0],num[2])
taxi+=x
num[0]-=x
num[2]-=x
if num[0]%4==3:
    taxi+=num[0]//4+1
elif num[0]%4==2:
    if num[1]!=0:
        taxi+=num[0]//4+1
        num[1]-=1
    else:
        taxi+=num[0]//4+1
elif num[0]%4==1:
    if num[2]!=0:
        taxi+=num[0]//4+1
        num[2]-=1
    elif num[2]==0 and num[1]!=0:
        taxi+=num[0]//4+1
        num[1]-=1
    elif num[2]==0 and num[1]==0:
        taxi+=num[0]//4+1
elif num[0]%4==0:
    taxi+=num[0]//4
if num[1]%2!=0:
    taxi+=num[1]//2+1
elif num[1]%2==0:
    taxi+=num[1]//2
taxi+=num[2]+num[3]
print(taxi)

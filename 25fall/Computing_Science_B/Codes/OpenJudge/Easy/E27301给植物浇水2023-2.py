n,a,b=map(int,input().split())
water=list(map(int,input().split()))
left,right=0,len(water)-1
aw,bw=a,b
count=0
while left<right:
    if aw<water[left]:
        aw=a
        count+=1
    if bw<water[right]:
        bw=b
        count+=1
    aw-=water[left]
    bw-=water[right]
    left+=1
    right-=1
if left==right:
    if aw>bw:
        if aw<water[left]:
            aw=a
            count+=1
    else:
        if bw<water[right]:
            bw=b
            count+=1
print(count)
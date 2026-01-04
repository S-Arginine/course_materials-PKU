n=int(input())
l=list(map(int,input().split()))
l1=[l[0]]
if n>1:
    for i in range(1,n):
        if l[i]!=l[i-1]:
            l1.append(l[i])
t=2
if len(l1)==1 or len(l1)==2:
    print(len(l1))
else:
    for i in range(1,len(l1)-1):
        a1,a2,a3=l1[i-1],l1[i],l1[i+1]
        if (a2-a1)*(a3-a2)<0:
            t+=1
    print(t)

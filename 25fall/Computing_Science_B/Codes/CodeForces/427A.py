n=int(input())
l=list(map(int,input().split()))
a,b,c=0,0,0
for i in range(n):
    if l[i]<=0:
        b-=l[i]
    elif l[i]>0:
        a+=l[i]
    if a<=b:
        c+=b-a
        a,b=0,0
print(c)


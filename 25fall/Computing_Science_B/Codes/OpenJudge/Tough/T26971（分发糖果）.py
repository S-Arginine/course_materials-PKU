n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
c=[1]*n
for i in range(1,n):
    if l[i]>l[i-1]:
        c[i]=c[i-1]+1
c1=c[::-1]
for i in range(1,n):
    if l1[i]>l1[i-1]:
        c1[i]=max(c1[i],c1[i-1]+1)
print(sum(c1))


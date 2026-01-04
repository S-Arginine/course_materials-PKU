n=int(input())
l=sorted(list(map(int,input().split())))
s=set(l[:])
t=0
for i in range(2,n):
    for j in range(i-1):
        a=l[i]-l[j]
        if a!=l[j] and a in s:
            t+=1
            break
print(t)
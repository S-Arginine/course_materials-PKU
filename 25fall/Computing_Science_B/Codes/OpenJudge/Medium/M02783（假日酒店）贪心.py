n=int(input())
l=[]
while n!=0:
    l1,l2,d,a=[],[],{},0
    for i in range(n):
        b=list(map(int,input().split()))
        l1.append(b[0])
        l2.append(b[1])
    for i in range(n):
        if l1[i] not in d.keys():
            d[l1[i]]=[]
            d[l1[i]].append(l2[i])
        else:
            d[l1[i]].append(l2[i])
    for key in d.keys():
        d[key]=min(d[key])
    min_key=min(d.keys())
    a,b=0,0
    for key in sorted(d.keys()):
        if key==min_key:
            a=d[min_key]
            b+=1
        elif d[key]<a:
            b+=1
            a=d[key]
    l.append(b)
    n=int(input())
for i in l:
    print(i)















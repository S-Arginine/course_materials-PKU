L,M=map(int,input().split())
s,l,n=[],[],0
for i in range(M):
    a,b=map(int,input().split())
    s.append([a,b])
s.sort()
for i in s:
    if not l:
        l.append(i)
    else:
        if l[-1][1]>=i[0]-1:
            l[-1][1]=max(i[1],l[-1][1])
        else:
            l.append(i)
for i in l:
    n+=i[1]-i[0]+1
print(L+1-n)



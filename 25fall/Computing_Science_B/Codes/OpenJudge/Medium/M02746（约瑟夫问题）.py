lst=[]
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    else:
        l=set(range(1,n+1))
        s,i=1,1  #次数，索引
        while len(l)>1:
            if i>n:
                i=1
            if i not in l:
                i+=1
            else:
                if s%m==0:
                    l.remove(i)
                    s+=1
                    i+=1
                else:
                    s+=1
                    i+=1
    lst.append(list(l)[0])
for i in lst:
    print(i)
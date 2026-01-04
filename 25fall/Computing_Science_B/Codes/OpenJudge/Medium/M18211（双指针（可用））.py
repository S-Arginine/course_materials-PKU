p=int(input())
l=sorted(list(map(int,input().split())))
m,n,k=0,0,-1
for i in l:
    if i>l[k]:
        break
    else:
        if p-i>=0:
            p-=i
            m+=1
        else:
            p+=l[k]
            k-=1
            n+=1
            if m-n<0:
                n-=1
                break
            else:
                p-=i
                m+=1
print(m-n)


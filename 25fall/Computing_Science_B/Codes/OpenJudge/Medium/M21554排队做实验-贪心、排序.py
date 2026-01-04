n=int(input())
s=list(map(int,input().split()))
sorted_s=sorted(s)
l,su=[],0
x=n-1
for i in sorted_s:
    su+=x*i
    x-=1
    for j in range(n):
        if s[j]==i:
            l.append(str(j+1))
            s[j]=0
            break
print(' '.join(l))
print(f'{su/n:.2f}')
s=input()
l=len(s)
max1=0
result=''
for i in range(l):
    count1=1
    m,n=i,i
    for j in range(min(i+1,l-i)):
        if s[i-j]==s[i+j]:
            count1=2*j+1
            m,n=i-j,i+j
        else:
            break
    if count1>max1:
        result=s[m:n+1]
        max1=count1
for i in range(l-1):
    x=i+0.5
    count2=0
    m,n=i,i
    for j in range(min(i+1,l-i-1)):
        a,b=int(x-0.5-j),int(x+0.5+j)
        if s[a]==s[b]:
            count2=2*j+2
            m,n=a,b
        else:
            break
    if count2>max1:
        result=s[m:n+1]
        max1=count2
print(result)
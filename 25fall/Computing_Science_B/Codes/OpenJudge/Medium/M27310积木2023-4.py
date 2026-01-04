n=int(input())
block=[set(list(input())) for i in range(4)]
result=[]
index1=[tuple([i]) for i in range(4)]
index2=[(1,2),(1,3),(1,4),(2,3),(2,4),(3,4),(4,3),(4,2),(3,2),(4,1),(3,1),(2,1)]
index3=[(1,2,3),(1,3,2),(1,4,2),(2,3,1),(2,4,1),(3,4,1),(4,3,1),(4,2,1),(3,2,1),(4,1,2),(3,1,2),(2,1,3),
        (1,2,4),(1,3,4),(1,4,3),(2,3,4),(2,4,3),(3,4,2),(4,3,2),(4,2,3),(3,2,4),(4,1,3),(3,1,4),(2,1,4)]
index4=[(1,2,3,4),(1,3,2,4),(1,4,2,3),(2,3,1,4),(2,4,1,3),(3,4,1,2),(4,3,1,2),(4,2,1,3),(3,2,1,4),(4,1,2,3),(3,1,2,4),(2,1,3,4),
        (1,2,4,3),(1,3,4,2),(1,4,3,2),(2,3,4,1),(2,4,3,1),(3,4,2,1),(4,3,2,1),(4,2,3,1),(3,2,4,1),(4,1,3,2),(3,1,4,2),(2,1,4,3)]
index=[index1,index2,index3,index4]
for i in range(n):
    word=list(input())
    flag=False
    m=len(word)
    for j in index[m-1]:
        t=0
        for k in range(m):
            if word[k] not in block[j[k]-1]:
                break
            t+=1
        if t==m:
            flag=True
            break
    if flag:
        result.append('YES')
    else:
        result.append('NO')
for i in result:
    print(i)






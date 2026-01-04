n=int(input())
l1=[7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
l2=['1','0','X','9','8','7','6','5','4','3','2']
l3=[]
for i in range(n):
    lst=list(input())
    a=0
    for j in range(17):
        a+=int(lst[j])*l1[j]
    if l2[a%11]==lst[17]:
        l3.append('YES')
    else:
        l3.append('NO')
for item in l3:
    print(item)



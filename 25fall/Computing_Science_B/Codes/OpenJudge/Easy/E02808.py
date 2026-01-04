l1=input().split()
L=int(l1[0])
M=int(l1[1])
list1=[]
for i in range(0,L+1):
    list1.append(1)
for i in range(0,M):
    l2=input().split()
    a=int(l2[0])
    b=int(l2[1])
    for p in range(a,b+1):
        list1[p]=0
new_list=[x for x in list1 if x==1]
print(len(new_list))

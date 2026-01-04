l=list(input())
lst=[int(i) for i in l]
k=int(input())
n=len(lst)-k
result=[]
record=0
while n>0:
    min_num=10
    for i in range(record,k+1):
        if lst[i]<min_num:
            min_num=lst[i]
            record=i+1
    result.append(min_num)
    k+=1
    n-=1
print(int(''.join([str(i)for i in result])))
n=int(input())
m=0
for i in range(0,n):
    num_list=input().split()
    if num_list.count('1')>=2:
        m+=1
print(m)

k=int(input())
num=input()
num_list=num.split()
a=0
b=0
c=0
for i in range(0,k):
    if num_list[i]=='5':
        b+=1
    elif num_list[i]=='1':
        a+=1
    elif num_list[i]=='10':
        c+=1
a+=c
print('''a
b
c''')

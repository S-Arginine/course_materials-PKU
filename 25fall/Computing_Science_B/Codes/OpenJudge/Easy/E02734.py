a=int(input())
num_list=[]
while a!=0:
    b=a%8
    num_list.append(b)
    a=a//8
print(''.join(str(num) for num in num_list[::-1]))

str_list=list(input())
for i in range(0,len(str_list)):
    if 'A'<=str_list[i]<='E':
        str_list[i]=chr(ord(str_list[i])+21)
    elif 'F'<=str_list[i]<='Z':
        str_list[i] = chr(ord(str_list[i])-5)
print(''.join(str_list))


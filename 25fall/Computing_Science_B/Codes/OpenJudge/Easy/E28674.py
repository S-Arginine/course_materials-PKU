k=int(input())
str_list=list(input())
for i in range(0,len(str_list)):
    if 'A'<=str_list[i]<='Z':
        x=ord(str_list[i])-k
        while x<65:
            x+=26
        str_list[i]=chr(x)
    elif 'a'<=str_list[i]<='z':
        y=ord(str_list[i])-k
        while y<97:
            y+=26
        str_list[i]=chr(y)
print(''.join(str_list))


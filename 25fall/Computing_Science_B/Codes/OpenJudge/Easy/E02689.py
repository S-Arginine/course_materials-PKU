str1=input()
list_str1=list(str1)
for i in range(0,len(list_str1)):
    if 'A'<=list_str1[i]<='Z':
        list_str1[i]=chr(ord(list_str1[i])+32)
    elif 'a'<=list_str1[i]<='z':
        list_str1[i]=chr(ord(list_str1[i])-32)
str2=''.join(list_str1)
print(str2)
list_1=list(input().lower())
list_2=list(input().lower())
for i in range(0,len(list_1)):
    if list_1[i]>list_2[i]:
        print('1')
        break
    if list_1[i]<list_2[i]:
        print('-1')
        break
    else:
        if i==len(list_1)-1:
            print('0')

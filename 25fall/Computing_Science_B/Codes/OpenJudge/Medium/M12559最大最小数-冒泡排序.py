n=int(input())
max_result,min_result='',''
l=input().split()
l1=l[:]
while l:
    max_num=l[0]
    for i in range(1,len(l)):
        str1a,str1b=max_num+l[i],l[i]+max_num
        if str1b>str1a:
            max_num=l[i]
    max_result+=max_num
    l.remove(max_num)
while l1:
    min_num=l1[0]
    for i in range(1,len(l1)):
        str2a,str2b=min_num+l1[i],l1[i]+min_num
        if str2b<str2a:
            min_num=l1[i]
    min_result+=min_num
    l1.remove(min_num)
print(max_result,min_result)
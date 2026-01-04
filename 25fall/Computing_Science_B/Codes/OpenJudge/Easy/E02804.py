my_dict={}
while True:
    l=input().split()
    if l==[]:
        break
    else:
        a,b=l[0],l[1]
        my_dict[b]=a
while True:
    try:
        s=input()
        print(my_dict.get(s,'eh'))
    except EOFError:
        break
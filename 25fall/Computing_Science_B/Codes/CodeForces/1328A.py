n=int(input())
l=[]
for i in range(n):
    num_list=list(map(int,input().split()))
    a=num_list[0]
    b=num_list[1]
    c=a%b
    d=b-c
    if c!=0:
        l.append(d)
    elif c==0:
        l.append(0)
for num in l:
    print(num)

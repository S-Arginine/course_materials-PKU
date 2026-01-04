def min_num(x):
    a,n=0,2
    done=True
    while done:
        if a+1/n<=x:
            a+=1/n
            n+=1
        else:
            done=False
    return n-1
num_list=[]
while True:
    c=float(input())
    if c==0.00:
        break
    else:
        num_list.append(min_num(c))
for i in num_list:
    print(i,'card(s)')




data_list=list(map(int,input().split()))
def quzheng(x):
    y=int(x)
    if x==y:
        return y
    else:
        return y+1
a=quzheng(data_list[0]/data_list[2])
b=quzheng(data_list[1]/data_list[2])
print(a*b)


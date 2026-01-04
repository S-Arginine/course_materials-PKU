def prime1(y):
    num=0
    for i in range(2,y):
        if y%i==0:
            num+=1
            break
    if num==0:
        return True
    else:
        return False
def prime2(z):
    prime_list=[]
    for i in range(2,z+1):
        if prime1(i):
            prime_list.append(i)
    return prime_list
x=int(input())
num_list=[]
if x<6 or x%2!=0:
    print('Error!')
else:
    for p in range(1,x):
        if p in prime2(x) and x-p in prime2(x)and p<=x-p:
            num_list.append(p)
for q in num_list:
    print(str(x)+'='+str(q)+'+'+str(x-q))
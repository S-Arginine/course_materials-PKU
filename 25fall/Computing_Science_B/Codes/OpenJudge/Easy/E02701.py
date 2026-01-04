a=int(input())
b=0
for i in range(1,a+1):
    if i%7==0 or i%10==7 or i//10==7:
        continue
    else:
        b+=i*i
print(b)



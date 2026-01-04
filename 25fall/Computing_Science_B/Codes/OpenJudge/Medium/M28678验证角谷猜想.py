n=int(input())
while n>1:
    if n%2!=0:
        print(str(n)+'*3+1='+str(n*3+1))
        n=n*3+1
    else:
        print(str(n)+'/2='+str(int(n/2)))
        n=int(n/2)
print('End')

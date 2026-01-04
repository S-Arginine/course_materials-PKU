a=int(input())
if a%2 !=0 or a<0 or a>=32768:
    print('0 0')
elif a%4==0:
    print(int(a/4),int(a/2))
else:
    print(int((a+2)/4),int(a/2))
d=int(input())
n=int(input())
di={}
for p in range(n):
    x,y,i=map(int,input().split())
    di[(x,y)]=i
max_num,t=0,0
for i in range(1025):
    for j in range(1025):
        s=0
        for key in di.keys():
            a,b=key[0],key[1]
            if i-d<=a<=i+d and j-d<=b<=j+d:
                s+=di[key]
        if s>max_num:
            max_num,t=s,1
        elif s==max_num:
            t+=1
print(t,max_num)





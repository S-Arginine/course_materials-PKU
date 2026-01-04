n=int(input())
result=[]
for i in range(n):
    a,b,c=map(int,input().split())
    num=i+1
    s=a+b+c
    result.append((s,a,num))
result=sorted(result,key=lambda x:x[1],reverse=True)
result=sorted(result,key=lambda x:x[0],reverse=True)
for i in result[0:5]:
    print(i[2],i[0])




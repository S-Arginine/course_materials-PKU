n=int(input())
l=[]    #储存每一组测试数据的结果
for i in range(n):
    a=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x,y=min(l1),min(l2)
    num1=sum(l1)+y*a
    num2=sum(l2)+x*a
    num=min(num1,num2)
    l.append(num)
for i in l:
    print(i)

n=int(input())
num_list=[]
for i in range(1,n+1):
    s=int(input())
    p=int(input())
    list_A=list(map(int,input().split()))
    q=int(input())
    list_B=list(map(int,input().split()))
    num=0
    for a in range(1,p+1):
        num+=list_B.count(s-list_A[a-1])
    num_list.append(num)
for number in num_list:
    print(number)
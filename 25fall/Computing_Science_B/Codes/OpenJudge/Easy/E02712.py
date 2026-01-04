def data_cal(a,b,c,d):
    dict={1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    days=0
    for i in range(a,c):
        days+=dict[i]
    days=days+d-b
    return days
n=int(input())
result_list=list()
for i in range(1,n+1):
    data=input()
    if data=='':
        break
    else:
        data_list=list(map(int,data.split()))
        tol_days=data_cal(data_list[0],data_list[1],data_list[3],data_list[4])
        num=data_list[2]*(2**tol_days)
        result_list.append(str(num))
for item in result_list:
    print(item)



X,N=map(int,input().split())
coins=list(map(int,input().split()))
coins=[i for i in coins if i<=X]
coins.sort(reverse=True)
coin_num=0
max_val=0
if coins[-1]!=1:
    print(-1)
else:
    while max_val<X:
        for coin in coins:
            if coin<=max_val+1:
                max_val+=coin
                coin_num+=1
                break
    print(coin_num)

n,a,b,c=map(int,input().split())
nums=sorted([a,b,c])
a,b,c=nums[0],nums[1],nums[2]
if n%a==0:
    print(n//a)
else:
    m=n//a-1
    ans1=0
    while m>=0:
        if (n-m*a)%c==0:
            ans1=m+(n-m*a)//c
            break
        else:
            m-=1
    m=n//a-1
    while m>=0:
        if (n-m*a)%b==0:
            ans2=m+(n-m*a)//b
            print(max(ans1,ans2))
            break
        else:
            m-=1
    if m==-1:
        m=n//a-1
        while m>=0:
            k=(n-m*a)//b-1
            while k>=0:
                if (n-m*a-k*b)%c==0:
                    print(m+k+(n-m*a-k*b)//c)
                    break
                else:
                    k-=1
            if k>=0:
                break
            else:
                m-=1
        if m==-1:
            m=n//b-1
            while m>=0:
                if (n-m*b)%c==0:
                    print(m+(n-m*b)//c)
                    break
                else:
                    m-=1
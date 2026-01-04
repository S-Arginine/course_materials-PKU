while True:
    try:
        n=float(input())
        m,a,b=0,1,0
        while abs(a-b)>0.000001:
            b=a
            a=(a*a+n)/(2*a)
            m+=1
        x=f"{a:.2f}"
        print(m,x)
    except EOFError:
        break
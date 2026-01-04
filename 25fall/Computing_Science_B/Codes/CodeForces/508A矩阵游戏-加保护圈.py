def f(a,b):   #左上角
    flag=True if ma[a][b]==ma[a][b-1]==ma[a-1][b-1]==ma[a-1][b]==0 else False
    return flag
def g(a,b):    #右上角
    flag=True if ma[a][b]==ma[a][b+1]==ma[a-1][b+1]==ma[a-1][b]==0 else False
    return flag
def p(a,b):    #右下角
    flag=True if ma[a][b]==ma[a][b+1]==ma[a+1][b+1]==ma[a+1][b]==0 else False
    return flag
def q(a,b):    #左下角
    flag=True if ma[a][b]==ma[a][b-1]==ma[a+1][b-1]==ma[a+1][b]==0 else False
    return flag
n,m,k=map(int,input().split())
ma=[[1]*(m+2) for i in range(n+2)]
possible,t=False,0
for i in range(k):
    x,y=map(int,input().split())
    c,d=x-1,y-1
    ma[c][d]=0
    t+=1
    if f(c,d) or g(c,d) or p(c,d) or q(c,d):
        possible=True
        break
t=t if possible else 0
print(t)

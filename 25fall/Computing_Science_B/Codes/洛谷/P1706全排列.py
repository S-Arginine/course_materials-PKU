def solve():
    n=int(input())
    nums=range(1,n+1)
    visited=[False]*n
    result=[]
    def f(x,l):
        nonlocal result,visited
        if len(l)==n:
            result.append(l[:])   #极其易错！！！一定要深拷贝！
            return
        for i in x:
            if not visited[i-1]:
                l.append(i)
                visited[i-1]=True
                f(x,l)
                m=l.pop()
                visited[m-1]=False
    f(nums,[])
    for j in result:
        print('   ','    '.join([str(k) for k in j]))
solve()
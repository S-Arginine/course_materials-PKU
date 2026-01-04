# Assignment #C: bfs & dp

Updated 1436 GMT+8 Nov 25, 2025

2025 fall, Complied by 金安逊 化学与分子工程学院



**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### sy321迷宫最短路径

bfs, https://sunnywhy.com/sfbj/8/2/321

思路：感觉bfs和dfs没有本质上的区别，迷宫最小路径和晶矿个数，最小连通域这些其实是同一类问题。这题虽然耗费不少时间，但是终于搞懂了到底应该什么时候做回溯操作，什么时候return。回溯的操作应该在判断return的语句之外，即不管有没有return都要把队尾弹出，并且判断是return还是递归应该在并列的分支结构中。

**1h**

代码：

```python
def g():
    n,m=map(int,input().split())
    matrix=[]
    for i in range(n):
        l=list(map(int,input().split()))
        matrix.append(l)
    result,count=[],n*m
    lst=[(-1,0),(0,1),(1,0),(0,-1)]
    def f(x,y,r,c):
        nonlocal result,count
        if matrix[x][y]==0:
            r.append((x,y))
            matrix[x][y]=1
            c+=1
            if x==n-1 and y==m-1:
                if c<count:
                    count=c
                    result=r[:]
                return
            else:
                for dx,dy in lst:
                    xx,yy=x+dx,y+dy
                    if 0<=xx<n and 0<=yy<m:
                        f(xx,yy,r,c)
            matrix[x][y]=0
            r.pop()
    f(0,0,[],0)
    return result
for p,q in g():
    print(f'{p+1} {q+1}')
```



代码运行截图![image-20251126150343600](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251126150343600.png)





### sy324多终点迷宫问题

bfs, https://sunnywhy.com/sfbj/8/2/324

思路：这题一开始真的还停留在递归的思路，结果发现不管怎么优化，总会出现不是最小值的结果，也不知道问题出在哪里。后来不得已只能求助AI，才发现dp既简洁又不会出错，只要构造一个队列，先进先出，把一个点的值赋为四周的值+1，这样就能确保第一次得到的步数一定是最小值。

**2h**

代码：

```python
from collections import deque
def solve():
    n,m=map(int, input().split())
    grid=[list(map(int, input().split())) for _ in range(n)]
    dist=[[-1]*m for _ in range(n)]
    if grid[0][0]==1:
        for row in dist:
            print(' '.join(map(str, row)))
        return
    q=deque()
    q.append((0,0))
    dist[0][0]=0
    directions=[(-1,0),(1,0),(0,-1),(0,1)]
    while q:
        x,y=q.popleft()
        for dx,dy in directions:
            nx,ny=x+dx,y+dy
            if 0<=nx<n and 0<=ny<m:
                if grid[nx][ny]==0 and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    for row in dist:
        print(' '.join(map(str, row)))
solve()
```



![image-20251127215412323](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251127215412323.png)代码运行截图 <mark></mark>





### M02945: 拦截导弹

dp, greedy http://cs101.openjudge.cn/pctbook/M02945

思路：最大递增子序列问题。但是一开始一直没想到从哪个方向出发寻找dp[i]与i之前项之间的关系，后来发现可将dp[i]设为以第i项结尾的最大子序列长度，这样总的结果就是max(dp[i])，递归表达式为dp[i]=max(f(j)+1 for j in range(i)if h[j]>=h[i])。

**1h**

代码：

```python
k = int(input())
h = list(map(int, input().split()))
f = [1] * k
for i in range(k):
    for j in range(i):
        if h[j] >= h[i]:
            f[i] = max(f[i], f[j] + 1)
print(max(f))

```



代码运行截图![image-20251128233219648](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251128233219648.png)





### 189A. Cut Ribbon

brute force/dp, 1300, https://codeforces.com/problemset/problem/189/A

思路：对于背包问题的dp解法还是不太了解，因此只能考虑暴力遍历所有情况（部分贪心），这个方法很容易漏情况。从小到大a,b,c，先考虑在a最多的情况下由a,b和a,c构成，两个都有可能所以取最大值，再考虑a,b,c构成，最后考虑b,c构成，还好这题没卡时间，否则我的brute force很有可能过不了。

**1h**

代码：

```python
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
```



代码运行截图![image-20251126183921449](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251126183921449.png)







### M01384: Piggy-Bank

dp, http://cs101.openjudge.cn/practice/01384/

思路：一个经典恰好完全背包问题，特别的是这里取的是最小值。这类题目在做之前先向AI学习了一下。基本思路是构造一个长度等于重量+1的dp数组，dp[i]表示重量恰好为i的时候背包中的最小价值，初始化为正无穷。对于每一个物品建立从该物品重量到最大重量的循环，表达式为dp[i]=min(dp[i],dp[i-w[k]]+v[k]),w[k],v[k]分别是第k个物体的质量和价值。

**1h**

代码：

```python
t=int(input())
result=[]
for i in range(t):
    weight0,weight1=map(int,input().split())
    W=weight1-weight0
    n=int(input())
    dp=[float('inf')]*(W+1)
    dp[0]=0
    v,w=[],[]
    for j in range(n):
        a,b=map(int,input().split())
        v.append(a)
        w.append(b)
    for j in range(n):
        for k in range(w[j],W+1):
            dp[k]=min(dp[k],dp[k-w[j]]+v[j])
    if dp[W]==float('inf'):
        result.append('This is impossible.')
    else:
        result.append(f'The minimum amount of money in the piggy-bank is {dp[W]}.')
for i in result:
    print(i)
```



![image-20251130160617439](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251130160617439.png)代码运行截图 





### M02766: 最大子矩阵

dp, kadane, http://cs101.openjudge.cn/pctbook/M02766

思路：做之前先让AI复习了一下Kandane算法（求最大子数组的和），其实说来很简单，就是比较前i-1项中的最大子数组和与第i项之和与第i项本身哪个大来决定要不要中断。最大子矩阵其实是个二维的Kandane问题，把矩阵一行中的连续的几个数求和之后的数构成数组，用Kadane算法求最值，然后一行中的连续的几个数选取有$C_n^1+C_n^2+...+C_n^n=2^n-1$种选法最后求最大值即可。这个算法居然没有超时，这让我有些意外。

**2h**

代码：

```python
n=int(input())
l,matrix=[],[]
while True:
    s=input()
    if s:
       l.extend(list(map(int,s.split())))
    if len(l)==n*n:
        break
for i in range(n):
    matrix.append(l[i*n:(i+1)*n])
m=matrix[0][0]
for j in range(n):
    for i in range(j,n):
        global_max=sum(matrix[0][j:i+1])
        current_max=sum(matrix[0][j:i+1])
        for k in range(1,n):
            s=sum(matrix[k][j:i+1])
            current_max=max(current_max+s,s)
            global_max=max(current_max,global_max)
        m=max(global_max,m)
print(m)
```



代码运行截图![image-20251130215406652](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251130215406652.png)





## 2. 学习总结和收获

近来接近期末周，学习压力明显增大，研究代码的时间进一步被挤压，不过在作业中也是有不少收获的。比如bfs和背包（完全背包，恰好背包）问题都是第一次接触，让我对如何构造dp数组，构造一维还是二维有了一个比较粗浅的认识。以及掌握了Kandane算法。虽然最近实在是挤不出时间来，但我在期末考之前应该立下小目标——把各类背包问题，dfs,bfs等问题进行专题的研究和对比，总结出一种代码的范式来。希望能通过努力在期末的机考取得一个理想的分数吧！






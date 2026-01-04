# Assignment #A: 递归、田忌赛马

Updated 2355 GMT+8 Nov 4, 2025

2025 fall, Complied by 金安逊 化学与分子工程学院



>**说明：**
>
>1. **解题与记录：**
>
>  对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. 提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### M018160: 最大连通域面积

dfs similar, http://cs101.openjudge.cn/pctbook/M18160

思路：这题跟上次那道晶矿的个数问题差不多，突破口是将一个==‘W’的点递推到周边8个点，并把判断过的点改成‘.’。有两个点很容易错，一个是要把矩阵扩充，另一个是函数嵌套的变量（跟晶矿那题不一样，这题因为最终返回的是t，所以嵌套的变量也是t）。

**40min**

代码

```python
def f(i,j,m,t):
    if m[i][j]=='W':
        t+=1
        m[i][j]='.'
        return f(i-1,j-1,m,f(i,j-1,m,f(i+1,j-1,m,f(i-1,j,m,f(i+1,j,m,f(i-1,j+1,m,f(i,j+1,m,f(i+1,j+1,m,t))))))))
    else:
        return t
T=int(input())
result=[]
for p in range(T):
    N,M=map(int,input().split())
    matrix=[['.']*(M+2)]
    for q in range(N):
        matrix.append(['.']+list(input())+['.'])
    matrix.append(['.']*(M+2))
    x=0
    for c in range(1,N+1):
        for d in range(1,M+1):
            y=f(c,d,matrix,0)
            if y>x:
                x=y
    result.append(x)
for num in result:
    print(num)
```



代码运行截图![image-20251105230659840](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251105230659840.png)





### sy134: 全排列III 中等

https://sunnywhy.com/sfbj/4/3/134

思路：传统递归题目。与之前的全排列不同的是这里要用字典的形式统计出现重复的数字。但是因为一直没发现把临时列表加到结果里面要深拷贝，所以多耗费了很多时间。

**1h**

代码

```python
from collections import defaultdict
n=int(input())
l=list(map(int,input().split()))
d=defaultdict(int)
re=[]
for i in l:
    d[i]+=1
def f(x,result,s):
    if sum(d.values())==0:
        result.append(s[:])    #这里最容易错的就是要进行一个深拷贝，否则result会跟s改变
        return
    else:
        for key in x.keys():
            if x[key]>0:
                s.append(key)
                x[key]-=1
                f(x,result,s)
                x[key]+=1
                s.pop()
f(d,re,[])
for i in re:
    print(' '.join([str(j)for j in i]))
```



代码运行截图![image-20251113145807279](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251113145807279.png)





### sy136: 组合II 中等

https://sunnywhy.com/sfbj/4/3/136

给定一个长度为的序列，其中有n个互不相同的正整数，再给定一个正整数k，求从序列中任选k个的所有可能结果。

思路：这题和排列类似，用的都是递归和回溯。但不同的是两者的基准条件，排列的基准条件是列表中的元素个数达到要求个数。同时这题琢磨最久的就是如何来避免重复。一开始想使用frozenset，发现无法按照要求的数据输出。后面发现只要设置成每次只考虑它后面的所有元素就可以避免重复，即把函数中的原列表变量改成到末尾的**切片**。

**40min**

代码

```python
n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
result=[]
def f(x,r,s):
    if len(s)==k:
        r.append(s[:])
        return
    else:
        for j in range(len(x)):
            s.append(x[j])
            f(x[j+1:],r,s)
            s.pop()
f(l,result,[])
for i in result:
    print(' '.join([str(j)for j in i]))
```



代码运行截图 ![image-20251113155942712](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251113155942712.png)





### sy137: 组合III 中等

https://sunnywhy.com/sfbj/4/3/137


思路：跟组合II同样类似，把列表改为字典，但是函数调用的对象还是列表（以字典键为元素），这时只要将对象x[j+1:]改为x[j]就可以让函数重复选取，判据是该元素的数目不为0.

**20min**

代码

```python
from collections import defaultdict
n,k=map(int,input().split())
l=sorted(list(map(int,input().split())))
d=defaultdict(int)
for i in l:
    d[i]+=1
l=list(d.keys())
result=[]
def f(x,r,s):
    if len(s)==k:
        r.append(s[:])
        return
    else:
        for j in range(len(x)):
            if d[x[j]]!=0:     #加上不为0的判据
                s.append(x[j])
                d[x[j]]-=1
                f(x[j:],r,s)  #把x[j+1:]改为x[j]即当这个元素本身还没用完时可以再选
                d[x[j]]+=1
                s.pop()
f(l,result,[])
for i in result:
    print(' '.join([str(j)for j in i]))
```



代码运行截图![image-20251113164007983](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251113164007983.png)





### M04123: 马走日

dfs, http://cs101.openjudge.cn/pctbook/M04123

思路：这题跟之前出现过的最大联通域那题有点像，就是从一个点出发向8个方向外延。有所不同的是这题递归的终点是把每个点都遍历了一遍这题大体的代码花了半小时就写出来了，但还是出现了几个细节上的问题，花了好久去发现，比如一开始写出来的代码把统计种数的变量放在了函数变量里面，结果是输出一直爆0，后来查了一下，用了一个nonlocal关键字把k设为全局变量就解决了这个问题。

**2h**

代码

```python
def g():
    T=int(input())
    result=[]
    d=[(1,2),(2,1),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]
    def f(m,x,y):
        nonlocal k
        if sum([sum(_)for _ in m])==0:
            k+=1
            return
        else:
            for dx,dy in d:
                xx,yy=x+dx,y+dy
                if m[xx+2][yy+2]==1:
                    m[xx+2][yy+2]=0
                    f(m,xx,yy)
                    m[xx+2][yy+2]=1
    for i in range(T):
        N,M,X,Y=map(int,input().split())
        ma=[[0]*(M+4),[0]*(M+4)]
        for j in range(N):
            l=[0,0]
            l.extend([1]*M)
            l.extend([0,0])
            ma.append(l)
        ma.append([0]*(M+4))
        ma.append([0]*(M+4))
        k=0
        ma[X+2][Y+2]=0
        f(ma,X,Y)
        result.append(k)
    for num in result:
        print(num)
g()
```



代码运行截图 <mark>![image-20251117183936659](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251117183936659.png)</mark>





### T02287: Tian Ji -- The Horse Racing

greedy, dfs http://cs101.openjudge.cn/pctbook/T02287

思路：一开始想到用递归得到全排列后再一一对比，选出最大值，结果发现超内存了。经过考虑后发现一种简化方法，就是把田忌从大到小排，把国王从小到大排，每比过一次就把田忌的前i个数重新排列，这样可以把全排列的n!变成n次运行且不需要过多存储空间。而最大值一定就在这n种情况里面。（直觉，个人好像无法证明为什么）

**1.5h**

代码

```python
import sys
n=int(input())
l=[]
while n!=0:
    tian=sorted(list(map(int,sys.stdin.readline().strip().split())),reverse=True)
    king=sorted(list(map(int,sys.stdin.readline().strip().split())))
    t=-n
    for i in range(n):
        tian=sorted(tian[:i+1])+tian[i+1:]
        x=0
        for j in range(n):
            if tian[j]>king[j]:
                x+=1
            elif tian[j]<king[j]:
                x-=1
        if x>t:
            t=x
    l.append(t*200)
    n=int(input())
sys.stdout.write('\n'.join([str(i)for i in l])+'\n')
```



代码运行截图 <mark>![image-20251118172030039](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251118172030039.png)</mark>





## 2. 学习总结和收获

这周可以说终于对递归和回溯算法入门了，虽然好几题都是在pythontutor的帮助下才一步步优化。现在已经能大体上把握递归的思路，但是很多细节上的问题还是经常犯错而且很难一下子发现。同时不同类型全排列和组合的密集训练让我对边界条件的控制和字典计数的运用有了更深的认识。但怎么压缩代码纠错的时间还是一个巨大的问题。






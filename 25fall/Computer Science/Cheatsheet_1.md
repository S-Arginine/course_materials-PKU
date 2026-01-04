# Final Exam Cheat Sheet-1

<mark>compiled by 金安逊 化学与分子工程学院</mark>

注：部分为AI生成并参考了一些学长的整理

## 1. 贪心

### 1. 排序

1. M02783 假日酒店（[OpenJudge - 02783:Holiday Hotel](http://cs101.openjudge.cn/practice/02783)）：先对一个指标排序处理，再考虑另一个指标

   ```python
   n=int(input())
   result=[]
   while n>0:
       l=[tuple(map(int,input().split())) for i in range(n)]
       t=0
       l.sort(key=lambda x:x[1])
       l.sort(key=lambda x:x[0])
       min_cost=float('inf')
       for dis,cost in l:
           if cost<min_cost:
               t+=1
               min_cost=cost
       result.append(t)
       n=int(input())
   for i in result:
       print(i)
   ```

2. E28681 奖学金（[OpenJudge - 28681:奖学金](http://cs101.openjudge.cn/practice/28681/)）：用key=lambda x语句进行多层排序

   ```python
   n=int(input())
   result=[]
   for i in range(n):
       a,b,c=map(int,input().split())
       num=i+1
       s=a+b+c
       result.append((s,a,num))
   result=sorted(result,key=lambda x:x[1],reverse=True)
   result=sorted(result,key=lambda x:x[0],reverse=True)
   for i in result[0:5]:
       print(i[2],i[0])
   ```

3. M12559 最大最小数（[OpenJudge - 12559:最大最小整数](http://cs101.openjudge.cn/practice/12559)）：经典<mark>冒泡排序</mark>，确保最前端相同长度的每个部分最大/最小

   ```python
   n=int(input())
   max_result,min_result='',''
   l=input().split()
   l1=l[:]
   while l:
       max_num=l[0]
       for i in range(1,len(l)):
           str1a,str1b=max_num+l[i],l[i]+max_num
           if str1b>str1a:
               max_num=l[i]
       max_result+=max_num
       l.remove(max_num)
   while l1:
       min_num=l1[0]
       for i in range(1,len(l1)):
           str2a,str2b=min_num+l1[i],l1[i]+min_num
           if str2b<str2a:
               min_num=l1[i]
       min_result+=min_num
       l1.remove(min_num)
   print(max_result,min_result)
   ```

#### 一些模板

##### 1.冒泡排序

```python
def bubble_sort(s):
    n=len(s)
    f=True
    for i in range(n-1):
        f=False
        for j in range(n-i-1):
            if s[j]>s[j+1]:
                s[j],s[j+1]=s[j+1],s[j]
                f=True
        if f==False:
            break
    return s
```

##### 2.归并排序：递归

```python
def merge_sort(s):
    if len(s)<=1:
        return s
    mid=len(s)//2
    left=merge_sort(s[:mid])
    right=merge_sort(s[mid:])   #两次递归放在一起，与 hanoi tower 的递归以及 lc-LCR085-括号生成 的递归很相似
    return merge(left,right)
def merge(l,r):
    ans=[]
    i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]:
            ans.append(l[i])
            i+=1
        else:
            ans.append(r[j])
            j+=1
    ans.extend(l[i:])
    ans.extend(r[j:])
    return ans
```

##### 3.快速排序：递归，选基准

```python
def quick_sort(s):
    if len(s)<=1:
        return s
    base=s[0]
    left=[x for x in s[1:] if x<base]
    right=[x for x in s[1:] if x>=base]
    return quick_sort(left)+[base]+quick_sort(right)
```

---

##### 4.lambda函数

```python
sort() #--> 稳定的从小到大排序，如果列表存储的是多元元组，则依次按照每个元组的元素进行排序，且稳定
#如果想自行按照元组的元素顺序排序，可以使用lambda函数
s=[(1,2),(3,1),(4,5),(2,5)]
#按照第二个元素排序
s.sort(key=lambda x:x[1]) #[(3, 1), (1, 2), (2, 5)]
#按照第二个元素为首要升序排序，第一个元素为次要升序排序
s.sort(key=lambda x:(x[1],x[0])) #[(3, 1), (1, 2), (2, 5), (4, 5)]
#按照第二个元素为首要降序排序，第一个元素为次要升序排序
s.sort(key=lambda x:(-x[1],x[0])) #[(2, 5), (4, 5), (1, 2), (3, 1)]
#如果想对数字按照字典序组合排序，得到最大最小整数，可以冒泡可以匿名

s=[9989,998]
#冒泡
for i in range(len(s)-1):
    for j in range(len(s)-i-1):
        if str(s[j])+str(s[j+1])<str(s[j+1])+str(s[j]):
            s[j],s[j+1]=s[j+1],s[j]
#lambda函数
s=sorted(s,key=lambda x: str(x)*10,reverse=True)

#对字典的键值对进行排序，与列表存储元组差不多
d={3:34,2:23,9:33,10:33}
dd=dict(sorted(d.items(),key=lambda x:(x[1],-x[0]))) #{2: 23, 10: 33, 9: 33, 3: 34}
```



### 2. 埃拉托斯特尼筛法

1. M29918 求亲和数（[OpenJudge - 29918:求亲和数](http://cs101.openjudge.cn/practice/29918)）：构建数组，在遍历过程将每个索引为n的元素加上自己的因数。

   ```python
   from math import sqrt
   def f(x):
       l=[]
       for i in range(2,int(sqrt(x))+1):
           if x%i==0:
               l.append(i)
               l.append(x//i)
       return sum(l)+1
   n=int(input())
   lst=[]
   for i in range(1,n+1):
       for j in range(i+1,n+1):
           if f(i)==j and f(j)==i:
               lst.append(str(i)+' '+str(j))
               break
   for item in lst:
       print(item)
   ```

2. CF230B T-Prime（https://codeforces.com/problemset/problem/230/B）：利用埃氏筛之前还要通过模6筛选。

   ```python
   from math import sqrt
   l=[True]*1000001
   l[0:2]=[False]*2
   for i in range(2,1001):
       if l[i]:
           l[i*2:1000001:i]=[False]*(1000000//i-1)
   n=int(input())
   num=list(map(int,input().split()))
   s=[]
   for i in num:
       p=sqrt(i)
       q=int(p)
       if q==p:
           if q==2 or q==3:
               s.append('YES')
           elif q%6==1 or q%6==5:
               if l[q]:
                   s.append('YES')
               else:
                   s.append('NO')
           else:
               s.append('NO')
       else:
           s.append('NO')
   for i in s:
       print(i)
   ```

### 3. 区间合并

1. T29947 校门外的树又来了（[OpenJudge - 29947:校门外的树又来了](http://cs101.openjudge.cn/practice/29947)）：给定若干区间取并集

   ```python
   L,M=map(int,input().split())
   s,l,n=[],[],0
   for i in range(M):
       a,b=map(int,input().split())
       s.append([a,b])
   s.sort()
   for i in s:
       if not l:
           l.append(i)
       else:
           if l[-1][1]>=i[0]-1:
               l[-1][1]=max(i[1],l[-1][1])
           else:
               l.append(i)
   for i in l:
       n+=i[1]-i[0]+1
   print(L+1-n)
   ```

2. M01328 雷达安装（[OpenJudge - 01328:Radar Installation](http://cs101.openjudge.cn/practice/01328/)）：给定区间求交集，统计交集的总数

   ```python
   from math import sqrt
   t,result=0,[]
   while True:
       t+=1
       n,d=map(int,input().split())
       if n==0 and d==0:
           break
       l,i=[],0
       while True:
           s=input()
           if not s:
               break
           else:
               a,b=map(int,s.split())
               l.append([a,b])
           l.sort()
           qujian=[]
       for i in range(n):
           if abs(l[i][1])>d:
               qujian=[]
               break
           else:
               if i==0:
                   x1,y1=l[0][0]-sqrt(d**2-l[0][1]**2),l[0][0]+sqrt(d**2-l[0][1]**2)
                   qujian.append([x1,y1])
               else:
                   x2,y2=l[i][0]-sqrt(d**2-l[i][1]**2),l[i][0]+sqrt(d**2-l[i][1]**2)
                   if x2>y1:
                       qujian.append([x2,y2])
                       x1,y1=x2,y2
                   else:
                       x2,y2=max(x1,x2),min(y1,y2)
                       qujian[-1]=[x2,y2]
                       x1,y1=x2,y2
       if len(qujian)==0:
           result.append(f"Case {t}: -1")
       else:
           result.append(f"Case {t}: {len(qujian)}")
   for i in result:
       print(i)
   ```



## 2. 递归

1. M04147 汉诺塔（http://cs101.openjudge.cn/pctbook/M04147）

   ```python
   import sys
   l=input().split()
   def move(x,a,b,c):
       result=[]
       if x==1:
           result.append(f'1:{a}->{c}')
       else:
           result+=move(x-1,a,c,b)+[f'{x}:{a}->{c}']+move(x-1,b,a,c)
       return result
   sys.stdout.write('\n'.join(move(int(l[0]),l[1],l[2],l[3]))+'\n')
   ```

2. T02754八皇后（http://cs101.openjudge.cn/pctbook/T02754）

   ```python
   col, linel, line2 = set(), set(), set()
   results = []
   def f(x,path):
       if x==8:
           results.append(''.join(map(str,path)))
           return
       for i in range(8):
           if i not in col and x+i not in linel and x-i not in line2:
               col.add(i)
               linel.add(x+i)
               line2.add(x-i)
   
               f(x+1,path+[i+1])
   
               col.remove(i)   #回溯操作
               linel.remove(x+i)
               line2.remove(x-i)
   
   f(0, [])
   
   lst = sorted(results)
   
   n = int(input())
   for _ in range(n):
       b = int(input())
       print(lst[b - 1])
   ```

   

## 3. 动态规划

### 1. 双dp（开两个dp数组）

1. M20744 土豪购物（[OpenJudge - 20744:土豪购物](http://cs101.openjudge.cn/practice/20744/)）：一个表示以第i个结尾最大，未删除，一个表示取到第i个，删除一次。

   ```python
   import math
   l=list(map(int,input().split(',')))
   n=len(l)
   not_del_dp,del_dp=[-math.inf]*n,[-math.inf]*n
   not_del_dp[0]=l[0]
   result=l[0]
   for i in range(1,n):
       not_del_dp[i]=max(l[i],not_del_dp[i-1]+l[i])
       del_dp[i]=max(not_del_dp[i-1],del_dp[i-1]+l[i])
       result=max(result,not_del_dp[i],del_dp[i])
   print(result)
   ```

### 2. 背包问题

<mark>初始化：如果要求恰好装满则为-inf；如果可以不装满为0</mark>

1. **01背包** --> 每个物品只能拿一次

```python
#小偷背包
def zero_one_bag():
    # V-总容量,n-物品个数,
    # cost=[0,     ],price=[0,     ]
    dp=[0]*(V+1)
    for i in range(1,n+1):           #每个物品
        for j in range(V,cost[i]-1,-1):    #逆向遍历每个容量
            dp[j]=max(dp[j],price[i]+dp[j-cost[i]])
    return dp[-1]
```

2. **完全背包** --> 每个物品可以拿无限次

   CF189A 剪彩带（https://codeforces.com/problemset/problem/189/A）：相当于每种价值都为1

```python
#零钱找零
def total_bag():
    dp=[0]*(V+1)
    for i in range(1,n+1):           #每个物品
        for j in range(1,cost[i]+1):       #正向遍历每个容量
            dp[j]=max(dp[j],price[i]+dp[j-cost[i]])
    return dp[-1]
```

3. **多重背包** --> 每个物品的个数有限制,把每个物品的个数拆成1 2 4等转化为01背包

```python
#NBA门票
def many_bag():
    #s=[0,   ]为每个物品的个数   #也可用字典表示
    dp=[0]*(V+1)
    for i in range(1,n+1):
        k=1
        while s[i]>0:
            cnt=min(k,s[i])
            for j in range(V,cnt*cost[i]-1,-1):
                dp[j]=max(dp[j],cnt*price[i]+dp[j-cnt*cost[i]])
            s[i]-=cnt
            k*=2
    return dp[-1]
```

4. **二维费用背包**

```python
def two_dimension_cost(n,V1,V2,cost1,cost2,price):
    dp=[[0]*(V2+1) for _ in range(V1+1)]
    for i in range(n):
        for c1 in range(V1-1,cost1[i]-1,-1):
            for c2 in range(V2-1,cost2[i]-1,-1):
                dp[c1][c2]=max(dp[c1][c2],dp[c1-cost1[i]][c2-cost2[i]]+price[i])
    return dp[-1][-1]
```

### 3. 状态压缩dp

1. T30201 旅行售货商（[OpenJudge - 30201:旅行售货商问题](http://cs101.openjudge.cn/practice/30201/)）：用一个二进制数表示当前途经城市的状态

   ```
   import math
   n=int(input())
   cost=[list(map(int,input().split())) for i in range(n)]
   size=1<<n
   dp=[[math.inf]*n for _ in range(size)]   #dp[i][j]表示在状态i下访问第j个城市时的最小花费
   dp[1][0]=0
   for i in range(1,size):   #遍历所有状态
       if not i&(1>>0):  #第一个城市默认已经访问过，不为1说明不是合法情形
           continue
       for j in range(n):
           if dp[i][j]==math.inf:
               continue
           if not i&(1<<j):
               continue
           for k in range(n):
               if i&(1<<k):
                   continue
               i_=i|(1<<k)
               dp[i_][k]=min(dp[i][j]+cost[j][k],dp[i_][k])
   result=min(dp[size-1][i]+cost[i][0] for i in range(1,n))
   print(result)
   ```

### 4.Kadane算法

oj-最大子矩阵-02766 http://cs101.openjudge.cn/practice/02766/

>Kadane算法
>一种非常高效的算法，用于求解一维数组中 最大子数组和/最大子矩阵和。它能够在 O(n) 时间复杂度内解决问题，广泛应用于许多动态规划问题中。
>避免了计算前缀和数组

```python
def kadane(s): #一维
    curr_max=total_max=s[0]
    for i in range(1,len(s)):
        curr_max=max(curr_max+s[i],s[i])
        total_max=max(total_max,curr_max)
    return total_max
```

```python
def kadane(s): #二维，压缩到一维数组
    curr_max=total_max=s[0]
    for i in range(1,len(s)):
        curr_max=max(curr_max+s[i],s[i])
        total_max=max(total_max,curr_max)
    return total_max
def max_sum_matrix(mat): #上下压缩
    max_sum=-float('inf')
    row,col=len(mat),len(mat[0])
    for top in range(row):
        col_sum=[0]*col
        for bottom in range(top,row):
            for c in range(col):
                col_sum[c]+=s[bottom][c]
            max_sum=max(max_sum,kadane(col_sum))
    return max_sum
```

### 5.前缀和

#### 1.前缀和数组

用于处理**多次查询**从[l,r]的序列之和的问题

```python
s=[int(i) for i in input().split()]
prefix=[s[0]]+[0]*(len(s)-1)
for i in range(1,len(s)):
    prefix[i]=prefix[i-1]+s[i]

distance_l_r=prefix[r]-(prefix[l-1] if l-1>=0 else 0)
```

---

#### 2.前缀和的特殊用法(哈希表)

使用prefix和prefix_map来记录已有的前缀和，从而判断子串和为0的子串个数；或找相同前缀和数字出现的最远位置
例题：

| 题目                          | 链接                                             |
| ----------------------------- | ------------------------------------------------ |
| oj-完美的爱-27141             | http://cs101.openjudge.cn/practice/27141/        |
| cf-Kousuke's Assignment-2033D | https://codeforces.com/problemset/problem/2033/D |

```python
#找出不重叠的和为0的子序列个数，一旦找到就将prefixed集合清空
#cf-Kousuke's Assignment-2033D
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
 
    prefix = 0
    prefixed = {0}
    cnt = 0
    for i in a:
        prefix += i
        if prefix not in prefixed:
            prefixed.add(prefix)
        else:
            cnt += 1
            prefix = 0
            prefixed={0}
    print(cnt)
```

### 6.整数分割问题

#### 1. 把n划分为若干个正整数，**不考虑顺序**（完全背包）

4：4=3+1=2+2=2+1+1=1+1+1+1 共5种

```python
def divide1(n):
    dp=[1]+[0]*n    #把0划分只有0这一种
    for i in range(1,n+1):           #每个数字
        for j in range(i,n+1):             #正向遍历每个容量（每个n）
            dp[j]+=dp[j-i]
    return dp[-1]
```

#### 2. 把n划分为若干个正整数，**考虑顺序**
4：4=3+1=1+3=2+2=2+1+1=1+2+1=1+1+2=1+1+1+1 共8种

```python
def divide2(n):
    dp=[1]+[0]*n
    for i in range(1,n+1):           #每个容量（每个n）
        for j in range(1,i+1):             #每个可能划分出的数字
            dp[i]+=dp[i-j]
    return dp[-1]
```

#### 3. 把n划分为若干个不同的正整数，**不考虑顺序**（01背包）
4：4=3+1 共1种

```python
def divide3(n):
    dp=[1]+[0]*n
    for i in range(1,n+1):
        for j in range(n,i-1,-1):
            dp[j]+=dp[j-i]
    return dp[-1]
```

#### 4. 把n划分为k个正整数，不考虑顺序

```python
#放苹果
#dp[n][k]:把n分成k组
def divide4(n,k):
    dp=[[0]*(k+1) for _ in range(n+1)]
    #每个数字分成1组都是1种
    for i in range(n+1):
        dp[i][1]=1
    for i in range(1,n+1):
        for j in range(2,k+1):
            #i<j时无法划分
            #i>=j时分为两种：若分组中有1，则为dp[i-1][j-1]
            #若无1，先把每组放进去1，则为dp[i-j][j]
            if i>=j:
                dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
    return dp[n][k] #dp[-1][-1]
```

#### 7. 线性dp+滚动数组优化

洛谷P2800 锁妖塔

```python
import sys
import math
def solve():
    n=int(input())
    data=sys.stdin.readline().strip().split()
    l=[int(i) for i in data]
    b,c=[math.inf]*2,[math.inf]*2
    b[0],b[1]=l[0],0
    c[0],c[1]=min(b[0],b[1])+l[1],0
    for i in range(3,n+1):
        d=[math.inf]*2
        d[0]=min(c[0],c[1])+l[i-1]
        d[1]=min(c[0],b[0])
        b,c=c,d
    print(min(c[0],c[1]))
solve()
```



## 4. 搜索

### 1. 深度优先搜索

数据结构为<mark>栈</mark>，算法实践为<mark>递归</mark>

<mark>易错点：backtracking，有回溯操作则必须有退出条件</mark>

#### 1. 全排列

```python
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
```

#### 2. dfs用于矩阵：连通域/路径问题

1. M18160最大连通域面积（http://cs101.openjudge.cn/pctbook/M18160）：

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

   

### 2. 广度优先搜索

数据结构本质为<mark>队列</mark>，算法实践为<mark>动态规划</mark>

#### 1.基础：最小路径问题

1. sy324 多终点迷宫问题（https://sunnywhy.com/sfbj/8/2/324）

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

   

#### 2. 多元bfs（同时将多个点作为起点）

1. LeetCode M542 01矩阵（[542. 01 矩阵 - 力扣（LeetCode）](https://leetcode.cn/problems/01-matrix/description/?envType=problem-list-v2&envId=dynamic-programming)）：把所有0全部入队然后开始bfs

   ```python
   n=int(input())
   mat=[list(map(int,input().split())) for i in range(n)]
   l=[lst[0] for lst in mat]
   n,m=len(l),len(mat[0])
   result=[[-1]*m for j in range(n)]
   from collections import deque
   queue=deque()
   visited=set()
   for i in range(n):
       for j in range(m):
           if mat[i][j]==0:
               result[i][j]=0
               queue.append((i,j))
   directions=[(1,0),(0,1),(-1,0),(0,-1)]
   print(queue)
   while queue:
       c=queue.popleft()  ##灵魂在这里，一定要从队首弹出
       x,y=c[0],c[1]
       for dx,dy in directions:
           xx,yy=x+dx,y+dy
           if 0<=xx<n and 0<=yy<m and (xx,yy) not in visited:
               queue.append((xx,yy))
               visited.add((xx,yy))
               if mat[xx][yy]==1:
                   result[xx][yy]=result[x][y]+1
   print(result)
   ```




### 3.Dijkstra算法

解决单源最短路径问题，用于非负权图，使用`heapq`的最小堆来代替`bfs`中的`deque`，设置`dist`列表更新最短距离。
例题：

```python
#oj-走山路-20106
import heapq
dx,dy=[0,-1,1,0],[-1,0,0,1]
def dijkstra(sx,sy,ex,ey):
    if s[sx][sy]=='#' or s[ex][ey]=='#':
        return 'NO'
    q=[]
    dist=[[float('inf')]*m for _ in range(n)]
    heapq.heappush(q,(0,sx,sy)) #(distance,x,y)
    dist[sx][sy]=0
    while q:
        curr,x,y=heapq.heappop(q) #heappop()
        if (x,y)==(ex,ey):
                return curr

        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if 0<=nx<n and 0<=ny<m and s[nx][ny]!='#':
                new=curr+abs(s[x][y]-s[nx][ny])
                if new<dist[nx][ny]:
                    heapq.heappush(q,(new,nx,ny)) #heappush()
                    dist[nx][ny]=new
    return 'NO'
```



## 5. 并查集

并查集（Union-Find/Disjoint-Set Union, DSU）是一种用于管理一系列**不相交集合**的数据结构。它高效地支持两种核心操作：

- **Find（查询）**：确定某个元素属于哪个子集（或称为“根节点”），可用于判断两个元素是否属于同一集合。
- **Union（合并）**：将两个子集合并成一个集合。

#### 基础代码模板 (Python)

这是一个实现了**路径压缩**和**按秩合并**的高效并查集模板：

```python
class UnionFind:
    def __init__(self, n):
        # 初始化：每个元素的父节点都是自己，每个集合的秩(rank)为0
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # 查找根节点（代表元），同时进行路径压缩
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x]) # 递归找到根，并直接指向它
        return self.parent[x]

    def union(self, x, y):
        # 合并两个元素所在的集合
        root_x = self.find(x)
        root_y = self.find(y)
        
        # 如果已经在同一个集合，直接返回
        if root_x == root_y:
            return
        
        # 按秩合并：将小树挂到大树下
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # 如果两棵树秩相等，任意合并，但作为根的树秩要+1
            self.parent[root_y] = root_x
            self.rank[root_x] += 1

    def is_connected(self, x, y):
        # 判断两个元素是否连通（属于同一集合）
        return self.find(x) == self.find(y)
```

1. sy360 学校班级个数（[晴问算法](https://sunnywhy.com/sfbj/8/2/360)）：将所有班级相同的同学的最终父节点全部指向一个人。

   ```python
   n,m=map(int,input().split())
   parent=[i for i in range(n+1)]
   count=n
   def find(x):
       if parent[x]!=x:
           parent[x]=find(parent[x])
       return parent[x]
   for i in range(m):
       a,b=map(int,input().split())
       a_class=find(a)   #找到最终父节点
       b_class=find(b)
       if a_class!=b_class:
           parent[a_class]=b_class
           count-=1
   print(count)
   ```

   

## 6. 二分查找

1. M08210 河中跳房子（http://cs101.openjudge.cn/practice/08210/）：对所有可能值进行二分查找（每个值对岩石遍历判断是否有可能）

   ```python
   def is_possible(distance,rocks,M):
       removed=0
       prev=0
       for rock in rocks:
           if rock-prev<distance:
               removed+=1
           else:
               prev=rock
       return removed<=M
   def max_shortest_distance(L,N,M,rocks):
       left,right=1,L
       result=0
       while left<=right:    #二分查找
           mid=left+(right-left)//2
           if is_possible(mid,rocks,M):
               result=mid
               left=mid + 1
           else:
               right=mid-1
       return result
   L,N,M=map(int,input().split())
   rocks=[int(input()) for _ in range(N)]
   print(max_shortest_distance(L,N,M,rocks))
   ```

   

## 7. 一些有用的函数

### 1.math模块

####  1. 数论与表示函数

| 函数              | 描述                 | 示例                       |
| :---------------- | :------------------- | :------------------------- |
| `math.ceil(x)`    | 向上取整             | `ceil(3.2) → 4`            |
| `math.floor(x)`   | 向下取整             | `floor(3.8) → 3`           |
| `math.trunc(x)`   | 截断小数部分         | `trunc(-3.7) → -3`         |
| `math.fabs(x)`    | 绝对值（返回浮点数） | `fabs(-5) → 5.0`           |
| `math.fmod(x, y)` | 浮点数取模           | `fmod(10.5, 3) → 1.5`      |
| `math.modf(x)`    | 返回小数和整数部分   | `modf(3.14) → (0.14, 3.0)` |

#### 2. 幂与对数函数

| 函数                  | 描述                 | 示例                 |
| :-------------------- | :------------------- | :------------------- |
| `math.pow(x, y)`      | x的y次幂             | `pow(2, 3) → 8.0`    |
| `math.sqrt(x)`        | 平方根               | `sqrt(9) → 3.0`      |
| `math.exp(x)`         | e的x次幂             | `exp(1) → 2.718...`  |
| `math.log(x[, base])` | 对数（默认自然对数） | `log(100, 10) → 2.0` |
| `math.log10(x)`       | 以10为底的对数       | `log10(1000) → 3.0`  |
| `math.log2(x)`        | 以2为底的对数        | `log2(8) → 3.0`      |

#### 3. 三角函数（参数为弧度）

| 函数               | 描述       | 示例                     |
| :----------------- | :--------- | :----------------------- |
| `math.sin(x)`      | 正弦函数   | `sin(pi/2) → 1.0`        |
| `math.cos(x)`      | 余弦函数   | `cos(0) → 1.0`           |
| `math.tan(x)`      | 正切函数   | `tan(pi/4) → 1.0`        |
| `math.asin(x)`     | 反正弦     | `asin(1) → 1.57...`      |
| `math.acos(x)`     | 反余弦     | `acos(0) → 1.57...`      |
| `math.atan(x)`     | 反正切     | `atan(1) → 0.785...`     |
| `math.atan2(y, x)` | 两点反正切 | `atan2(1, 1) → 0.785...` |

#### 4. 双曲函数

| 函数           | 描述     | 示例                 |
| :------------- | :------- | :------------------- |
| `math.sinh(x)` | 双曲正弦 | `sinh(0) → 0.0`      |
| `math.cosh(x)` | 双曲余弦 | `cosh(0) → 1.0`      |
| `math.tanh(x)` | 双曲正切 | `tanh(1) → 0.761...` |

#### 5. 角度与弧度转换

| 函数              | 描述       | 示例                      |
| :---------------- | :--------- | :------------------------ |
| `math.degrees(x)` | 弧度转角度 | `degrees(pi) → 180.0`     |
| `math.radians(x)` | 角度转弧度 | `radians(180) → 3.141...` |

### 2. heapq模块

1. **heapify(x)** - 将列表原地转为堆
2. **heappush(heap, item)** - 插入元素
3. **heappop(heap)** - 弹出最小值
4. **heappushpop(heap, item)** - 插入后弹出最小值
5. **heapreplace(heap, item)** - 弹出后插入
6. **nlargest(n, iterable, key=None)** - 最大的 n 个元素
7. **nsmallest(n, iterable, key=None)** - 最小的 n 个元素
8. **merge(\*iterables, key=None, reverse=False)** - 合并多个有序序列

### 3. bisect模块

1. **bisect_left(arr,item) - 左侧插入点**（返回索引）
2. **bisect_right() / bisect() - 右侧插入点**
3. **insort_left() - 左侧插入**
4.  **insort_right() / insort() - 右侧插入**



## 8. 矩阵

### 1. 旋转矩阵

1. 小Z的情书

   ```python
   import sys
   def r():       #顺时针旋转：先把主对角线上下交换，再倒置每一列
       for i in range(n):
           for j in range(i+1,n):
               s[i][j],s[j][i]=s[j][i],s[i][j]
       for lst in s:
           lst.reverse()
       return
   def c():
       for i in range(n):
           for j in range(n):
               if s[i][j]!='#':
                   results.append(matrix[i][j])
       return
   n=int(input())
   s=[list(sys.stdin.readline().strip()) for i in range(n)]
   matrix=[list(sys.stdin.readline().strip()) for j in range(n)]
   results=[]
   c()
   for i in range(3):
       r()
       c()
   print(''.join(results))
   ```

   

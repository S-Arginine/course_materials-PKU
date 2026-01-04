# Assignment #9: Mock Exam立冬前一天

Updated 1658 GMT+8 Nov 6, 2025

2025 fall, Complied by 化学与分子工程学院 金安逊



>**说明：**
>
>1. Nov⽉考： <mark>AC-3</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29982:一种等价类划分问题

hashing, http://cs101.openjudge.cn/practice/29982

思路：这题还是很容易错的，首先一开始看错了题目，以为是原数能被k整除。后来又发现漏看了从小到大输出，因此在上面多耗费了不少时间。思路倒是不难，考察字典的分类功能。

**25min**

代码

```python
from collections import defaultdict
L=list(input())
for i in range(len(L)):
    if L[i]==',':
        L[i]=' '
L=''.join(L)
m,n,k=map(int,L.split())
d=defaultdict(list)
for i in range(m+1,n):
    a=i//10000+i//1000%10+i//100%10+i//10%10+i%10
    if a%k==0:
        d[a].append(i)
for k in sorted(d.keys()):
    print(','.join([str(i) for i in d[k]]))
```



代码运行截图![image-20251106185639222](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251106185639222.png)





### E30086:dance

greedy, http://cs101.openjudge.cn/practice/30086

思路：瞪眼法贪心。把身高从小到大排列发现只要索引为2N与2N+1之差<=D就是可配对的必要条件。

**15min**

代码

```python
N,D=map(int,input().split())
l=sorted(list(map(int,input().split())))
flag='Yes'
for i in range(N):
    if l[2*i+1]-l[2*i]>D:
        flag='No'
        break
print(flag)
```



代码运行截图![image-20251106190057978](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251106190057978.png)





### M25570: 洋葱

matrices, http://cs101.openjudge.cn/practice/25570

思路：这题考察的矩阵有一定难度。比较麻烦的是要体现“剥皮”这个动态过程，即先将外围一圈求和，再在原矩阵的基础上做删除操作。这里每从列表中删除一个元素的时间复杂度是O(n)，不知有没有更快的方法？

**20min**

代码

```python
n=int(input())
matrix=[]
for i in range(n):
    matrix.append(list(map(int,input().split())))
a=0
while len(matrix)>0:
    if len(matrix)>2:
        s=sum(matrix[0])+sum(matrix[-1])
        for i in range(1,len(matrix)-1):
            s+=matrix[i][0]+matrix[i][-1]
        if s>a:
            a=s
        del matrix[0]
        del matrix[-1]
        for i in range(len(matrix)):
            del matrix[i][0]
            del matrix[i][-1]
    elif len(matrix)==2:
        s=sum(matrix[0])+sum(matrix[-1])
        if s>a:
            a=s
        break
    else:
        s=sum(matrix[0])
        if s>a:
            a=s
        break
print(a)
```



代码运行截图![image-20251106190517038](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251106190517038.png)





### M28906:数的划分

dfs, dp, http://cs101.openjudge.cn/practice/28906


思路：这题的思路看出来就很简单，如果没看出来就一直被卡死了。我一开始看出要和i-1,j-1建立关系，但是一直想不明白其他要怎么处理。后来咨询AI终于发现了，原来给每个数都减去1就可以转换成i-j,j的情况。感觉这点对于数学思维欠缺的我来说有点困难。。

**2h**

代码

```python
n,k=map(int, input().split())
dp=[[0]*(k+1) for _ in range(n+1)]
dp[0][0]=1
for i in range(1,n+1):
    for j in range(1,k+1):
        if i>=j:
            dp[i][j]=dp[i-1][j-1]+dp[i-j][j]
print(dp[n][k])
```

下面这种做法用的是dfs，难点在于给dfs函数设置3个参数，可画一个树形图辅助理解。

```python
def solve():
    n,k=map(int,input().split())
    result=0
    def dfs(start,end,t):
        nonlocal result
        if t==1:
            result+=1
            return
        for i in range(start,end//t+1):
            dfs(i,end-i,t-1)
    dfs(1,n,k)
    print(result)
solve()
```

代码运行截图 <mark>（至少包含有"Accepted"）</mark>





### M29896:购物

greedy, http://cs101.openjudge.cn/practice/29896

思路：典型贪心问题，但是我觉得有一种递归思想在里面。根据课上讲的思路，维护一个目前硬币所能覆盖的最大数max_val，这时新增的硬币必须为小于等于max_val+1的最大值c，此时max_val可以扩大到max_val+c的范围且保证完全覆盖。考场上没能想到可以建立一个中间值max_val来求局部最优，但是如果想到了这一点这题似乎就没什么难度了。

**15min**

代码

```python
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
```



代码运行截图 ![image-20251111162747597](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251111162747597.png)





### T25353:排队

greedy, http://cs101.openjudge.cn/practice/25353

思路：上课时没听明白，回寝之后听了一遍回放还是没完全理解，于是决定选择性放弃，不准备在超过能力范围的题目上面花费过多时间。



代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

离期末机考只剩6周不到的时间，各门功课的压力都在增大，我准备转变策略，专攻中等难度的题目，不再在过难题上花费太多时间了（<1h）。同时平时刷题的量也要相应加上去。希望老师能在每日选做里面多加一些贴近期末考试中等难度的题目！






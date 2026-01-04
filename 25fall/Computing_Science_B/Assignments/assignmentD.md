# Assignment #D: Mock Exam下元节

Updated 1729 GMT+8 Dec 4, 2025

2025 fall, Complied by <mark>金安逊 化学与分子工程学院</mark>



>**说明：**
>
>1. Dec⽉考： <mark>AC1（1WA，1MLE）</mark> 。考试题⽬都在“题库（包括计概、数算题目）”⾥⾯，按照数字题号能找到，可以重新提交。作业中提交⾃⼰最满意版本的代码和截图。
>
>2. 解题与记录：对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>3. 提交安排：提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
> 
>4. 延迟提交：如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### E29945:神秘数字的宇宙旅行 

implementation, http://cs101.openjudge.cn/practice/29945

思路：

**3min**

代码

```python
n=int(input())
while n>1:
    if n%2==0:
        print(f'{n}/2={n//2}')
        n=n//2
    else:
        print(f'{n}*3+1={n*3+1}')
        n=n*3+1
print('End')
```



代码运行截图![image-20251205162708990](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251205162708990.png)





### E29946:删数问题

monotonic stack, greedy, http://cs101.openjudge.cn/practice/29946

思路：这题纯属题目的问题，题意没说清楚，一开始以为0放在开头是无效的，结果一直WA，后来考完了才知道原来0也算，并且输出为int()之后的结果。这题属于瞪眼法贪心，只要确保证数的第i位一定是前n-i个数中最小的即可。

**1h**

代码

```python
l=list(input())
lst=[int(i) for i in l]
k=int(input())
n=len(lst)-k
result=[]
record=0
while n>0:
    min_num=10
    for i in range(record,k+1):
        if lst[i]<min_num:
            min_num=lst[i]
            record=i+1
    result.append(min_num)
    k+=1
    n-=1
print(int(''.join([str(i)for i in result])))
```



代码运行截图![image-20251205163720161](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251205163720161.png)





### E30091:缺德的图书馆管理员

greedy, http://cs101.openjudge.cn/practice/30091

思路：贪心题感觉有点看运气，像这题就花了半天时间才看出来是否折返不影响结果。

**30min**

代码

```python
l=int(input())
n=int(input())
nums=sorted(list(map(int,input().split())))
mi=max(min(nums[i],l+1-nums[i]) for i in range(n))
ma=max(max(nums[0],l+1-nums[0]),max(nums[-1],l+1-nums[-1]))
print(f'{mi} {ma}')
```



代码运行截图![image-20251208222949106](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251208222949106.png)





### M27371:Playfair密码

simulation，string，matrix, http://cs101.openjudge.cn/practice/27371


思路：论难度这题比第二题还简单，其实只要在理解清楚题意的基础上inplementation就行了，要做的这么几件事：处理密钥、生成密钥矩阵、标记每个元素的坐标、处理并分组需要加密的字符串、分3种情况查找相应的密文。但是很容易疏忽，**比如我在考场上好不容易写出来，结果因为处理字符串那步忘记pop导致陷入死循环，最后超内存了**，非常可惜！

**1h**

代码

```python
from collections import deque
k=list(input())
keyword=[]
for i in range(len(k)):
    if k[i]=='j':
        k[i]='i'
    if k[i] not in keyword:
        keyword.append(k[i])
for i in range(97,123):
    if chr(i)!='j':
        if chr(i) not in keyword:
            keyword.append(chr(i))
matrix=[[0]*5 for i in range(5)]
n=0
d=dict()
for i in range(5):
    for j in range(5):
        if n<len(keyword):
            d[keyword[n]]=(i,j)
            matrix[i][j]=keyword[n]
            n+=1
def f(x):
    while x>=5:
        x-=5
    return x
n=int(input())
result=[]
for i in range(n):
    string=deque(input())
    for j in range(len(string)):
        if string[j]=='j':
            string[j]='i'
    s=[]
    r=[]
    while string:
        if len(string)==1:
            st=(string[0],'x') if string[0]!='x' else (string[0],'q')
            s.append(st)
            string.popleft()
        else:
            a,b=string[0],string[1]
            if a==b:
                sm='x' if a!='x' else 'q'
                D=string.popleft()
                string.appendleft(sm)
                string.appendleft(D)
            else:
                s.append((a,b))
                string.popleft()
                string.popleft()
    for j in s:
        if d[j[0]][0]==d[j[1]][0]:
            r.append(matrix[d[j[0]][0]][f(d[j[0]][1]+1)])
            r.append(matrix[d[j[1]][0]][f(d[j[1]][1]+1)])
        elif d[j[0]][1]==d[j[1]][1]:
            r.append(matrix[f(d[j[0]][0]+1)][d[j[1]][1]])
            r.append(matrix[f(d[j[1]][0]+1)][d[j[1]][1]])
        else:
            r.append(matrix[d[j[0]][0]][d[j[1]][1]])
            r.append(matrix[d[j[1]][0]][d[j[0]][1]])
    result.append(''.join(r))
for i in result:
    print(i)
```



代码运行截图![image-20251205170626878](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251205170626878.png)





### T30201:旅行售货商问题

dp,dfs, http://cs101.openjudge.cn/practice/30201

思路：这题的dp做法一开始没想到，后面请教同学才了解到要用状态压缩dp，就是每个状态可以用一个二进制数字表示，而状态之间的改变通过位运算进行。dp[i] [j]表示在状态i，停留在第j个城市时的最小花费。但是第一遍做的时候惨遭TLE，后面在第一重循环内部加了一个判断条件就AC了。

**2h**

代码

```python
import math
n=int(input())
cost=[list(map(int,input().split())) for i in range(n)]
size=1<<n
dp=[[math.inf]*n for _ in range(size)]
dp[1][0]=0
for i in range(1,size):
    if not i&(1>>0):
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



代码运行截图![image-20251209165506760](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251209165506760.png)





### T30204:小P的LLM推理加速

greedy, http://cs101.openjudge.cn/practice/30204

思路：这题实在是超出范围，没什么思路，而且最近时间非常紧，故**未完成**。



代码

```python

```



代码运行截图 <mark>（至少包含有"Accepted"）</mark>





## 2. 学习总结和收获

本周最大的收获是了解了状态压缩dp还有位运算。以及开始复习之前做过的题了，发现之前的很多思路都忘得差不多了，希望在期末考之前把所有题型的思路都过一遍。

希望期末考题的题面稍微简洁一些，表述清楚一些，能少一些搞心态但又难度不高的题！






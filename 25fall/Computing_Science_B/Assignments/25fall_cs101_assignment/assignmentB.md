# Assignment #B: dp

Updated 1448 GMT+8 Nov 18, 2025

2025 fall, Complied by 金安逊 化学与分子工程学院

**说明：**

1）请把每个题目解题思路（可选），源码Python, 或者C++（已经在Codeforces/Openjudge上AC），截图（包含Accepted），填写到下面作业模版中（推荐使用 typora https://typoraio.cn ，或者用word）。AC 或者没有AC，都请标上每个题目大致花费时间。

2）提交时候先提交pdf文件，再把md或者doc文件上传到右侧“作业评论”。Canvas需要有同学清晰头像、提交文件有pdf、"作业评论"区有上传的md或者doc附件。

3）如果不能在截止前提交作业，请写明原因。



## 1. 题目

### LuoguP1255 数楼梯

dp, bfs, https://www.luogu.com.cn/problem/P1255

思路：这题其实就是个斐波那契数列问题。dp表达式为dp[i]=dp[i-1]+dp[i-2].

**5min**

代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0],dp[1]=1,1
for i in range(2,n+1):
    dp[i]=dp[i-1]+dp[i-2]
print(dp[n])
```



代码运行截图 ![image-20251119184156254](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251119184156254.png)





### 27528: 跳台阶

dp, http://cs101.openjudge.cn/practice/27528/

思路：这题与上题类似，但dp表达式变成了从dp[0]+...+dp[i-1]=dp[i].

**10min**

代码：

```python
n=int(input())
dp=[0]*(n+1)
dp[0],dp[1]=1,1
for i in range(2,n+1):
    for j in range(0,i):
        dp[i]+=dp[j]
print(dp[n])
```



代码运行截图![image-20251119185733807](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251119185733807.png)





### M23421:《算法图解》小偷背包问题

dp, http://cs101.openjudge.cn/pctbook/M23421/

思路：这题一开始想用贪心，写了一下发现贪心好像不那么好写，跟之前的挖矿不太一样，这里的商品不可再分。因此切换成动态规划，这里dp状态转移方程就想了好久，后来发现只要构筑一个长度为weight+1的列表dp，dp[i]=max(dp[i-k]+dp[k] for k in range(0,i//2+1) if i-k!=k)即可，说白了就是把重量两两拆分后取最大值。但是代码纠错同样花了不少时间。

**1.5h**

代码：

```python
import sys
n,b=map(int,input().split())
d={}
price=list(map(int,sys.stdin.readline().split()))
weight=list(map(int,sys.stdin.readline().split()))
for i in range(n):
    d[weight[i]]=price[i]
dp=[0]*(b+1)
for key in d.keys():
    if key>b:
        del d[key]
weight=sorted(list(d.keys()))
for i in weight:
    dp[i]=d[i]
for i in range(1,b+1):
    l=[]
    for k in range(0,i//2+1):
        if i-k!=k:
            l.append(dp[i-k]+dp[k])
    dp[i]=max(l)
print(dp[b])
```



代码运行截图 ![image-20251119210401830](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251119210401830.png)





### M5.最长回文子串

dp, two pointers, string, https://leetcode.cn/problems/longest-palindromic-substring/

思路：这题想了半天dp没想出来，只能用上常规思路。分奇偶两种情况讨论，奇数长度时判断s[i-k],s[i+k]是否相等，偶数长度时取索引值+0.5，同样让指针往对称的两边移动判断对称的元素是否相等。设置两个全局变量实时存放字符串的最大长度和结果。但是这个思路还是有很多细节问题容易出错，比如中间的一些边界怎么控制等等，修正了好久。

**1.5h**

代码：

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        l=len(s)
        max1=0
        result=''
        for i in range(l):
            count1=1
            m,n=i,i
            for j in range(min(i+1,l-i)):
                if s[i-j]==s[i+j]:
                    count1=2*j+1
                    m,n=i-j,i+j
                else:
                    break
            if count1>max1:
                result=s[m:n+1]
                max1=count1
        for i in range(l-1):
            x=i+0.5
            count2=0
            m,n=i,i
            for j in range(min(i+1,l-i-1)):
                a,b=int(x-0.5-j),int(x+0.5+j)
                if s[a]==s[b]:
                    count2=2*j+2
                    m,n=a,b
                else:
                    break
            if count2>max1:
                result=s[m:n+1]
                max1=count2
        return result
```



代码运行截图![image-20251120170231598](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251120170231598.png)







### 474D. Flowers

dp, 1700 https://codeforces.com/problemset/problem/474/D

思路：感受到难度1700题的压迫感了。首先被难住的就是如何寻找递推关系，一开始没想到只用考虑加在末尾，觉得很复杂还想着用组合数。后面发现每次变化只要考虑加在队尾，那么dp[i]=dp[i-k]+dp[i-1]。但是这样还是超时，求助群友才发现原来求和本身的操作也具有很大的时间复杂度，需要把求和的时间也换成“空间”，即使用列表存储“前缀和”来减小时间复杂度。

**2h**

代码：

```python
t,k=map(int,input().split())
e=10**9+7
result=[]
num=[]
for i in range(t):
    a,b=map(int,input().split())
    num.append((a,b))
c=max(i[1]for i in num)
dp=[0]*(c+1)
dp[0]=1
dp_sum=[0]*(c+1)
dp_sum[0]=1
for i in range(1,c+1):
    dp[i]+=dp[i-1]
    if i>=k:
        dp[i]+=dp[i-k]
    if dp[i]>=e:
        dp[i]-=e
    if i>=1:
        dp_sum[i]=dp_sum[i-1]+dp[i]
    if dp_sum[i]>=e:
        dp_sum[i]-=e
for a,b in num:
    s=dp_sum[b]-dp_sum[a-1]
    s=s%e
    result.append(s)
for i in result:
    print(i)
```



代码运行截图![image-20251121222936662](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251121222936662.png)





### M198.打家劫舍

dp, https://leetcode.cn/problems/house-robber/

思路：这题比上题简单不少，主要时间还是花在找递推关系上面。基本思路是：先建立dp的前3项。如果第i-1项没算在内，则dp[i]=dp[i-2]+nums[i-1]，但如果第i项算在内的话，dp[i]=max(dp[i-1],dp[i-2]+nums[i-1])。

**40min**

代码：

```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums)+1)
        for i in range(1,len(nums)+1):
            if i==1:
                dp[i]=nums[0]
            elif i==2:
                dp[i]=max(nums[0],nums[1])
            elif i==3:
                dp[i]=max(nums[1],nums[0]+nums[2])
            else:
                if dp[i-1]-dp[i-3]!=nums[i-2]:
                    dp[i]=dp[i-2]+nums[i-1]
                else:
                    dp[i]=max(dp[i-2]+nums[i-1],dp[i-1])
        return dp[-1]
```



代码运行截图![image-20251123160333442](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251123160333442.png)





## 2. 学习总结和收获

这周最大的收获就是彻底理解了“用空间换时间”的思想，如何避免重复解决相同子问题，动态规划甚至掌握得比递归好多了（递归至今还有些地方没想清楚）。但是最长回文字串那题好像没想明白怎么用dp，用一般方法虽然做出来但不够简洁而且花了很多时间，希望老师课上把作业点拨一下。






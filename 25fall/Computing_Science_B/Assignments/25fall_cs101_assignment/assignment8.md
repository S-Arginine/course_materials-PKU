# Assignment #8: 递归

Updated 1315 GMT+8 Oct 21, 2025

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

### M04147汉诺塔问题(Tower of Hanoi)

dfs, http://cs101.openjudge.cn/pctbook/M04147

思路：这是我独立完成的第一个递归题，心里还是很有成就感的，特别是看到仅仅10行的代码和简单的分支结构，给人一种简洁之美。一开始一直想不清楚a,b,c的相对位置会改变应该怎么处理，后面写了代码才发现这正是递归算法的精妙所在，只需锁定第n次和第n-1次的关系设置函数的变量，就能解决这个问题。你不需要想清楚具体的变换，剩下的交给递归本身去一次次迭代就行了。

**1h**

代码

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



代码运行截图![image-20251028214528664](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251028214528664.png)





### M05585: 晶矿的个数

matrices, dfs similar, http://cs101.openjudge.cn/pctbook/M05585

思路：这题明显比上一题抽象很多，加上我对dfs还属于一知半解的状态，因此花费了大量时间思考怎么构造递归（还好这题对时间复杂度要求不高）。我的思路是在原矩阵的基础上进行修改，把所有上下左右相邻的点全部“归一化”，这样只要统计执行的“归一化”次数，它就是矿的数目。

**2h**

代码

```python
k=int(input())
t=[]
def f(lst,x,y,m):
    if lst[x][y]==m:
        lst[x][y]='0'
        return f(f(f(f(lst,x,y+1,m),x+1,y,m),x,y-1,m),x-1,y,m)
    else:
        return lst
for i in range(k):
    n = int(input())
    matrix=[['0']*(n+2)]
    for j in range(n):
        l=['0']
        l+=list(input())
        l.append('0')
        matrix.append(l)
    matrix.append(['0']*(n+2))
    R,B=0,0
    for p in range(1,n+1):
        for q in range(1,n+1):
            if matrix[p][q]=='r':
                matrix=f(matrix,p,q,'r')
                R+=1
            elif matrix[p][q]=='b':
                matrix=f(matrix,p,q,'b')
                B+=1
    t.append([R,B])
for i in t:
    print(f'{i[0]} {i[1]}')
```



代码运行截图 ![image-20251029211504054](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251029211504054.png)





### M02786: Pell数列

dfs, dp, http://cs101.openjudge.cn/pctbook/M02786/

思路：现在的题目想要独立完成还是挺困难的，第一次花五分钟写了个递归，结果稳稳超时。第二次改成一般的循环，结果也是超时。去问了AI，然后学到了原来del list[index]的时间复杂度是$O(n)$。第三次改成双端队列，依然超时。最后才醒悟，原来求模本身的运算量也是很大的，特别是到十万项之后数额巨大。最后把求模并入递推运算终于AC。

**1h**

代码

```python
import sys
from functools import lru_cache
from collections import deque
n=int(input())
out=[]
@lru_cache(maxsize=None)
def pell(x):
    lst=deque([0,1])
    if x==1:
        return 1
    else:
        for j in range(1,x):
            a=lst[1]*2+lst[0]
            if a>=32767:
                a=a%32767
            lst.append(a)
            lst.popleft()
        return lst[1]
for i in range(n):
    k=int(input())
    out.append(pell(k))
sys.stdout.write('\n'.join(map(str,out))+'\n')
```



代码运行截图![image-20251030222952371](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251030222952371.png)





### M46.全排列

backtracking, https://leetcode.cn/problems/permutations/


思路：感觉初学递归还是很难想清楚递归的每一步应该做什么，因为这非常考验一种逆向思维。目前想到的最好的解决方法是想清楚函数的自变量和值分别是什么，再想知道了n-1的值后再做什么操作就可以得到n，最后考虑边界条件即第一次调用该函数的情况，并用第二次调用来验证递归的正确性。

**1h**

代码

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        from copy import deepcopy
        def f(x):
            if len(x)==1:
                return [x]
            else:
                s=[]
                for i in range(len(x)):
                    l=deepcopy(x)
                    a=l.pop(i)
                    m=f(l)
                    for j in m:
                        j.append(a)
                    s+=m
                return s
        return f(nums)
```



代码运行截图![image-20251101223354210](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251101223354210.png)





### T02754: 八皇后

dfs and similar, http://cs101.openjudge.cn/pctbook/T02754

思路：这题对于初学递归的我还是太有挑战了，一开始写了一个大致的过程，但是一直想不清楚中间的细节以及该通过什么样的方式回溯，最后向AI取经了，才知道应该把每个有占用的索引放入一个集合而因为每个i对应不同种情况，所以切换i的时候要把前一种情况的去除掉。



代码

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

            col.remove(i)
            linel.remove(x+i)
            line2.remove(x-i)

f(0, [])

lst = sorted(results)

n = int(input())
for _ in range(n):
    b = int(input())
    print(lst[b - 1])
```



代码运行截图![image-20251102160008155](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251102160008155.png)





### T01958 Strange Towers of Hanoi

http://cs101.openjudge.cn/practice/01958/

思路：这题给了思路点拨就很好做了在，f4(x)的函数中间加一个遍历算法找出最小次数，base case 同样设为x=1。但是如果不给思路点拨感觉又很难做TT。

**30min**

代码

```python
def f3(x):
    return 2**x-1
def f4(x):
    if x>1:
        l=[]
        for i in range(1,x):
            l.append(f4(x-i)*2+f3(i))
        return min(l)
    elif x==1:
        return 1
lst=[f4(j) for j in range(1,13)]
for j in lst:
    print(j)
```



代码运行截图![image-20251102141603963](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251102141603963.png)





## 2. 学习总结和收获

这周因为要准备期中考，分配给研究代码的时间没有以前那么久了，所以对于回溯问题还是搞得不是特别懂，希望老师下节课能放慢节奏，再系统复习一下递归这块！






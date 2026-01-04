# Assignment #6: 矩阵、贪心

Updated 1432 GMT+8 Oct 14, 2025

2025 fall, Complied by 金安逊 化学与分钟工程学院



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

### M18211: 军备竞赛

greedy, two pointers, http://cs101.openjudge.cn/pctbook/M18211



思路：这题方向很容易找，就是当钱够的话不停买最便宜的，钱不够的话先卖最贵的，但是有些控制条件非常容易搞错，比如要控制m不能小于n，还要确保双指针不能重合，光是优化就花了半天时间。

**1h**

代码

```python
p=int(input())
l=sorted(list(map(int,input().split())))
m,n,k=0,0,-1
for i in l:
    if i>l[k]:
        break
    else:
        if p-i>=0:
            p-=i
            m+=1
        else:
            p+=l[k]
            k-=1
            n+=1
            if m-n<0:
                n-=1
                break
            else:
                p-=i
                m+=1
print(m-n)
```



代码运行截图![image-20251015081906487](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251015081906487.png)





### M21554: 排队做实验

greedy, http://cs101.openjudge.cn/pctbook/M21554/



思路：根据简单观察可发现时间越短越要放到前面做，将问题转化为对一组数据进行排序。这里对相同数据的排序有点棘手，没有马上想到，后来发现只要把每个排过的数变成0就不会影响了。

**20min**

代码

```python
n=int(input())
s=list(map(int,input().split()))
sorted_s=sorted(s)
l,su=[],0
x=n-1
for i in sorted_s:
    su+=x*i
    x-=1
    for j in range(n):
        if s[j]==i:
            l.append(str(j+1))
            s[j]=0
            break
print(' '.join(l))
print(f'{su/n:.2f}')
```



代码运行截图 ![image-20251015202112918](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251015202112918.png)





### E23555: 节省存储的矩阵乘法

implementation, matrices, http://cs101.openjudge.cn/pctbook/E23555



思路：不需考虑运行时长的限制，较易，但是需要注意到判断元素是否在字典里的时间复杂度是$O(1)$，所以用字典的话更快些。但是因为 对矩阵乘法不熟练，多耗了不少时间。

**30min**

代码

```python
from collections import defaultdict
n,m1,m2=map(int,input().split())
X,Y,Z=defaultdict(int),defaultdict(int),defaultdict(int)
for i in range(m1):
    row1,col1,val1=map(int,input().split())
    X[(row1,col1)]=val1
for i in range(m2):
    row2,col2,val2=map(int,input().split())
    Y[(row2,col2)]=val2
for row in range(n):
    for col in range(n):
        for i in range(n):
            if (row,i) in X and (i,col) in Y:
                Z[(row,col)]+=X[(row,i)]*Y[(i,col)]
for i in Z.keys():
    print(i[0],i[1],Z[i])
```



代码运行截图![image-20251016181717097](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251016181717097.png)





### M12558: 岛屿周⻓

matices, http://cs101.openjudge.cn/pctbook/M12558


思路：经过简单尝试发现某个位置周边有几个‘0’，其贡献的周长就加几。但是代码上有好几个细节没注意，所以优化和纠错花了一些时间。

**30min**

代码

```python
n,m=map(int,input().split())
A=[[0*i for i in range(m+2)]]
for i in range(n):
    A.append([0])
    A[i+1].extend(list(map(int,input().split())))
    A[i+1].append(0)
A.append([0*i for i in range(m+2)])
l=0
for i in range(1,n+1):
    for j in range(1,m+1):
        x=0
        if A[i][j]==1:
            if A[i-1][j]==0:
                x+=1
            if A[i][j-1]==0:
                x+=1
            if A[i+1][j]==0:
                x+=1
            if A[i][j+1]==0:
                x+=1
        l+=x
print(l)
```



代码运行截图 ![image-20251017171814978](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251017171814978.png)





### M01328: Radar Installation

greedy, http://cs101.openjudge.cn/practice/01328/



思路：这题一开始想尝试先用最外围的岛屿确定雷达的位置，但是发现后面情况实在太多讨论不过来。不得已去问了下AI，AI一提示我是区间合并，我就恍然大悟了，校园外的树那题是取并集，这题是取交集，取出来几个交集就有几个雷达。但是中间一些小细节卡了我很久比如如何根据x的值对区间进行排序，如何控制y超过d的时候直接终止循环输出-1等等，感觉还得在细节上下功夫。

**2h**

代码

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



代码运行截图![image-20251018103121501](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251018103121501.png)





### 545C. Woodcutters

dp, greedy, 1500, https://codeforces.com/problemset/problem/545/C



思路：这题充分说明了审题的重要性，一开始就浪费了15分钟，代码写好才发现题目看错了，每棵树都是占据一点我没看到。后来纠正了以后，优化又花了不少时间。其实思路不难，左侧和右侧的可能情况分别考虑即可。

**40min**

代码

```python
from collections import defaultdict
d=defaultdict(int)
n=int(input())
X,qujian,num=[],[],0
for i in range(n):
    x,h=map(int,input().split())
    d[x]=h
    X.append(x)
for i in range(n):
    if i==0:
        qujian.append([X[i]-d[X[i]],X[i]])
        num+=1
    elif 1<=i<=n-2:
        if X[i]-d[X[i]]>max(qujian[-1][1],X[i-1]):
            num+=1
            qujian.append([X[i]-d[X[i]],X[i]])
        else:
            if X[i]+d[X[i]]<X[i+1]:
                num+=1
                qujian.append([X[i],X[i]+d[X[i]]])
    elif i==n-1:
        num+=1
print(num)
```



代码运行截图![image-20251019175249041](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251019175249041.png)







## 2. 学习总结和收获

这周收获还是蛮大的，首先是学会了矩阵和矩阵的乘法（其实把它写成二维形式就很容易理解了，就是A的第i行和B的第j列一对一相乘再相加得到了C[i] [j]）,其次是对于区间覆盖的一类题目基本掌握，还有对双指针也加深了了解，不过对指针什么时候停下来的条件控制还是很容易弄错。

在现阶段给代码找错误的时间已经远远超出了写代码的时间，并且80%以上的错误都来自于分支结构if的条件有误或不全面，现在还在慢慢摸索如何避免这样的问题。






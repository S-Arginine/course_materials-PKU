# Assignment #2: 语法练习

Updated 1335 GMT+8 Sep 16, 2025

2025 fall, Complied by <mark>同学的姓名、院系</mark>



**作业的各项评分细则及对应的得分**

| 标准                                 | 等级                                                         | 得分 |
| ------------------------------------ | ------------------------------------------------------------ | ---- |
| 按时提交                             | 完全按时提交：1分<br/>提交有请假说明：0.5分<br/>未提交：0分  | 1 分 |
| 源码、耗时（可选）、解题思路（可选） | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于2个：0分 | 1 分 |
| AC代码截图                           | 提交了4个或更多题目且包含所有必要信息：1分<br/>提交了2个或以上题目但不足4个：0.5分<br/>少于：0分 | 1 分 |
| 清晰头像、PDF文件、MD/DOC附件        | 包含清晰的Canvas头像、PDF文件以及MD或DOC格式的附件：1分<br/>缺少上述三项中的任意一项：0.5分<br/>缺失两项或以上：0分 | 1 分 |
| 学习总结和个人收获                   | 提交了学习总结和个人收获：1分<br/>未提交学习总结或内容不详：0分 | 1 分 |
| 总得分： 5                           | 总分满分：5分                                                |      |

>
>
>
>**说明：**
>
>1. **解题与记录：**
>
>   对于每一个题目，请提供其解题思路（可选），并附上使用Python或C++编写的源代码（确保已在OpenJudge， Codeforces，LeetCode等平台上获得Accepted）。请将这些信息连同显示“Accepted”的截图一起填写到下方的作业模板中。（推荐使用Typora https://typoraio.cn 进行编辑，当然你也可以选择Word。）无论题目是否已通过，请标明每个题目大致花费的时间。
>
>2. **课程平台：**课程网站位于Canvas平台（https://pku.instructure.com ）。该平台将在<mark>第2周</mark>选课结束后正式启用。在平台启用前，请先完成作业并将作业妥善保存。待Canvas平台激活后，再上传你的作业。
>
>3. **提交安排：**提交时，请首先上传PDF格式的文件，并将.md或.doc格式的文件作为附件上传至右侧的“作业评论”区。确保你的Canvas账户有一个清晰可见的本人头像，提交的文件为PDF格式，并且“作业评论”区包含上传的.md或.doc附件。
>
>4. **延迟提交：**如果你预计无法在截止日期前提交作业，请提前告知具体原因。这有助于我们了解情况并可能为你提供适当的延期或其他帮助。  
>
>请按照上述指导认真准备和提交作业，以保证顺利完成课程要求。





## 1. 题目

### 263A. Beautiful Matrix

implementation, 800, https://codeforces.com/problemset/problem/263/A



思路：运用二维列表的由元素查找索引的功能，将问题转化为求索引之间的绝对值。

**30min**

代码

```python
matrix=[input().split() for _ in range(5)]
def index(x,y):
    for i in range(len(x)):
        for j in range(len(x[i])):
            if x[i][j]==y:
                return [i,j]
a=index(matrix,'1')[0]
b=index(matrix,'1')[1]
print(abs(a-2)+abs(b-2))
```



代码运行截图 ![image-20250924212721089](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250924212721089.png)





### 1328A. Divisibility Problem

math, 800, https://codeforces.com/problemset/problem/1328/A



思路：较简单，需将问题转化为求余数。由于其只能加不能减故要分能整除和不能整除两种情况讨论

**15min**

代码

```python
n=int(input())
l=[]
for i in range(n):
    num_list=list(map(int,input().split()))
    a=num_list[0]
    b=num_list[1]
    c=a%b
    d=b-c
    if c!=0:
        l.append(d)
    elif c==0:
        l.append(0)
for num in l:
    print(num)
```



代码运行截图 ![image-20250925150346719](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250925150346719.png)





### 427A. Police Recruits

implementation, 800, https://codeforces.com/problemset/problem/427/A



思路：这是个数学问题，看着简单，其实想了半天都没有头绪。后来发现问题可以转化为统计两个不同的量a,b，a>=b时不作改动，而b>a时作差然后将两者归零，再重新开始新的循环。

**60min**

代码

```python
n=int(input())
l=list(map(int,input().split()))
a,b,c=0,0,0
for i in range(n):
    if l[i]<=0:
        b-=l[i]
    elif l[i]>0:
        a+=l[i]
    if a<=b:
        c+=b-a
        a,b=0,0
print(c)
```



代码运行截图 <mark>![image-20250925162519809](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250925162519809.png)</mark>





### E02808: 校门外的树

implementation, http://cs101.openjudge.cn/pctbook/E02808/


思路：经过多次尝试，发现代数运算不方便。再发现序号可以对应于列表的索引值，于是把L+1棵树抽象成长度为L+1的列表，再将“砍树”抽象为改变列表的元素。

**40min**

代码

```python
l1=input().split()
L=int(l1[0])
M=int(l1[1])
list1=[]
for i in range(0,L+1):
    list1.append(1)
for i in range(0,M):
    l2=input().split()
    a=int(l2[0])
    b=int(l2[1])
    for p in range(a,b+1):
        list1[p]=0
new_list=[x for x in list1 if x==1]
print(len(new_list))

```



代码运行截图 ![image-20250923181144796](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250923181144796.png)





### sy60: 水仙花数II

implementation, https://sunnywhy.com/sfbj/3/1/60



思路：定义一个函数来判断其是否为“水仙花”数，再用遍历区间内所有元素的方法筛选出水仙花数。

**20min**

代码

```python
def f(n):
    a,b,c=n//100,n//10%10,n%10
    if a**3+b**3+c**3==n:
        return True
    else:
        return False
l=list(map(int,input().split()))
x,y=l[0],l[1]
num_list=[]
for i in range(x,y+1):
    if f(i):
        num_list.append(str(i))
if len(num_list)==0:
    print('NO')
else:
    print(' '.join(num_list))
```



代码运行截图 ![image-20250925164838384](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250925164838384.png)





### M01922: Ride to School

implementation, http://cs101.openjudge.cn/pctbook/M01922/



思路：这题并没有特别难但是转化花了我不少时间。首先一开始没发现先出发的轨迹一定不会产生干扰，然后后面又看了好久才发现只需要找到除了先出发的之外到达终点最短的时间。其实这个问题从始至终都只是一个筛选的问题，最关键的是要找到筛选的最佳条件。

**2h**

代码

```python
import math
l3=[]
i=int(input())
while i!=0:
    a,b=[],[]
    for j in range(i):
        l1=list(map(int,input().split()))
        if l1[1]>=0:
            a.append(l1[0])
            b.append(l1[1])
    l2 = [4500/a[k]*3.6+b[k] for k in range(len(a))]
    t=min(l2)
    l3.append(math.ceil(t))
    i=int(input())
for num in l3:
    print(num)
```



代码运行截图 ![image-20250926230618001](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250926230618001.png)





## 2. 学习总结和收获

感觉编程题越做到后面越考验问题的转化能力而非语法和理论知识。虽然我几乎是零基础，但是学到现在我还是自信的认为凭借我现有的语法知识完成Medium题应该不成问题，但是做题时还是会碰到各种各样的障碍，真正想把难题做出来还是需要个把小时。我觉得接下来的工作主要还是在题目中不断总结，寻找一些易错点和语法模式。希望我后面能继续保持每天至少3题的训练量，继续加油！






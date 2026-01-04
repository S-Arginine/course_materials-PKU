# Assignment #7: 矩阵、队列、贪心

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

### M12560: 生存游戏

matrices, http://cs101.openjudge.cn/pctbook/M12560/

思路：这题思路不难，就是根据索引找出所有的邻居。但是有个地方很容易错，就是不能在原来的矩阵上面修改，需要用deepcopy，否则会影响后续结果。一开始没考虑到这一点，修改代码耗费大量时间。

**40min**

代码

```python
import copy
def g(x,y):
    lst=[ma[x-1][y-1],ma[x][y-1],ma[x+1][y-1],ma[x-1][y],ma[x+1][y],ma[x-1][y+1],ma[x][y+1],ma[x+1][y+1]]
    return lst.count(1)
n,m=map(int,input().split())
ma=[[-1 for i in range(m+2)]]
for i in range(n):
    ma.append([-1])
    ma[i+1].extend(list(map(int,input().split())))
    ma[i+1].append(-1)
ma.append([-1 for j in range(m+2)])
ma1=copy.deepcopy(ma)
for p in range(1,n+1):
    for q in range(1,m+1):
        if ma[p][q]==0:
            if g(p,q)==3:
                ma1[p][q]=1
            else:
                ma1[p][q]=0
        elif ma[p][q]==1:
            if g(p,q)<2 or g(p,q)>3:
                ma1[p][q]=0
            else:
                ma1[p][q]=1
for i in range(1,n+1):
    l=[str(ma1[i][j]) for j in range(1,m+1)]
    print(' '.join(l))
```



代码运行截图 ![image-20251021162418465](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251021162418465.png)





### M04133:垃圾炸弹

matrices, http://cs101.openjudge.cn/pctbook/M04133/

思路：这题考察的就是基础的矩阵查找。一开始就按照最直接的方法把每个点都遍历一遍再找出最优解，想这样先试试，本来以为包要超时的，结果还AC了，再仔细看才发现这题的输入数据比较少，他不是想在时间上面卡你。

**30min**

代码

```python
d=int(input())
n=int(input())
di={}
for p in range(n):
    x,y,i=map(int,input().split())
    di[(x,y)]=i
max_num,t=0,0
for i in range(1025):
    for j in range(1025):
        s=0
        for key in di.keys():
            a,b=key[0],key[1]
            if i-d<=a<=i+d and j-d<=b<=j+d:
                s+=di[key]
        if s>max_num:
            max_num,t=s,1
        elif s==max_num:
            t+=1
print(t,max_num)
```



代码运行截图![image-20251022223704525](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251022223704525.png)





### M02746: 约瑟夫问题

implementation, queue, http://cs101.openjudge.cn/pctbook/M02746/

思路：因为队列不太会用所以用了个集合的方法，但是易错点在于你在循环开始前需要判断元素在不在集合中，如果不在就不算次数

**40min**

代码

```python
lst=[]
while True:
    n,m=map(int,input().split())
    if n==m==0:
        break
    else:
        l=set(range(1,n+1))
        s,i=1,1  #次数，索引
        while len(l)>1:
            if i>n:
                i=1
            if i not in l:
                i+=1
            else:
                if s%m==0:
                    l.remove(i)
                    s+=1
                    i+=1
                else:
                    s+=1
                    i+=1
    lst.append(list(l)[0])
for i in lst:
    print(i)
```



代码运行截图![image-20251023164208702](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251023164208702.png)





### M26976:摆动序列

greedy, http://cs101.openjudge.cn/pctbook/M26976/


思路：一开始确实没什么头绪，后来把一组数列用阶梯状的形象化表示画在纸上就能找到规律了，只要找到所有“极值点”并把它们连起来就是所要的最大摆动数列。<mark>这个结论其实可以证明：</mark>假如还存在更多的数满足题意，那它必定会出现在两个极值点之间，这与摆动数列的定义矛盾。但是前面好几次提交都是**WA**，在群里请教了同学才发现我漏掉了一种重要的情况，就是有相邻的数相等的时候，这时应当把所有相等数合并成一个作为极值点。

**2h**

代码

```python
n=int(input())
l=list(map(int,input().split()))
l1=[l[0]]
if n>1:
    for i in range(1,n):
        if l[i]!=l[i-1]:
            l1.append(l[i])
t=2
if len(l1)==1 or len(l1)==2:
    print(len(l1))
else:
    for i in range(1,len(l1)-1):
        a1,a2,a3=l1[i-1],l1[i],l1[i+1]
        if (a2-a1)*(a3-a2)<0:
            t+=1
    print(t)
```



代码运行截图![image-20251024211710834](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251024211710834.png)





### T26971:分发糖果

greedy, http://cs101.openjudge.cn/pctbook/T26971/

思路：贪心算法的难度确实名不虚传，这题我一开始的想法是把原数列分成一段一段的，对每一段进行处理，后来发现端点处太麻烦了，怎么都写不清楚。实在是不得已去请教了AI，后来看到要用两次遍历就恍然大悟了，原来在一次遍历同时兼顾左右两侧是不现实的，那就把问题分成两个部分，先处理右侧大于左侧，再反过来看左侧大于右侧，这样就把所有的麻烦省了。

**2h**

代码

```python
n=int(input())
l=list(map(int,input().split()))
l1=l[::-1]
c=[1]*n
for i in range(1,n):
    if l[i]>l[i-1]:
        c[i]=c[i-1]+1
c1=c[::-1]
for i in range(1,n):
    if l1[i]>l1[i-1]:
        c1[i]=max(c1[i],c1[i-1]+1)
print(sum(c1))
```



代码运行截图![image-20251025185407669](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251025185407669.png)





### 1868A. Fill in the Matrix

constructive algorithms, implementation, 1300, https://codeforces.com/problemset/problem/1868/A

思路：这题有半小时都花在理解题意上面了。不过题意理解以后这题应该比上面两题简单一些。只要找到规律就行了。一开始我发现只要行数充足s就是个定值，如果行数不够的话从缺0，缺1...一直往上面考虑就行了（特殊情况是m=1的时候）。对于满足条件的一种矩阵，我发现<mark>双端队列</mark>特别好用，只要每次把队尾的元素提到队首即可得到新的一行。

**1h40min**

代码

```python
from collections import deque
t=int(input())
ls=[]  #放s
l=[]   #放矩阵
for i in range(t):
    n,m=map(int,input().split())
    if m==1:
        ls.append(0)
        l.append([[0]]*n)
    else:
        dq=deque(sorted(range(m),reverse=True))
        matrix=[]
        ls.append(min(n+1,m))
        for j in range(n):
            if j<m-1:
                a=dq.pop()
                dq.appendleft(a)
                matrix.append(list(dq))
            else:
                matrix.append(matrix[-1])
        l.append(matrix)
for p in range(t):
    print(ls[p])
    for q in l[p]:
        print(' '.join(map(str,q)))
```



代码运行截图![image-20251026093959694](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251026093959694.png)





## 2. 学习总结和收获

<mark>有个疑问</mark>，垃圾炸弹和约瑟夫那两题能不能用贪心而不用implementation?（如果出题者要卡时间的话）

希望老师上课能讲讲一些贪心难题的思考方向或者常见手段！因为即使能想出来也需要耗费大量时间（比如摆动数列和分糖果），在考场上很难完成！

这周收获还挺大的，主要是掌握了双端队列的用法，以及复习了一下以前留下的深拷贝的漏洞。对于集合的哈希在时间上的优越性有了更直观的认识（不用集合TLE，用集合就AC）






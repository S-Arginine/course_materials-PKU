# Assignment #4: T-primes + 贪心

Updated 1814 GMT+8 Sep 30, 2025

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

### 34B. Sale

greedy, sorting, 900, https://codeforces.com/problemset/problem/34/B



思路：不管他能不能拿得下，只要让他每次都尽可能拿绝对值大的负数而不拿正数即可

**10min**

代码

```python
def f(x):
    m=0
    for i in x:
        if i<=0:
            m+=1
    return m
l=list(map(int,input().split()))
a,b,n=l[0],l[1],0
num_list=list(map(int,input().split()))
if b>=f(num_list):
    for j in num_list:
        if j<=0:
            n+=-j
else:
    for k in range(b):
        n+=-(sorted(num_list)[k])
print(n)
```



代码运行截图![image-20251003192627019](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251003192627019.png)





### 160A. Twins

greedy, sortings, 900, https://codeforces.com/problemset/problem/160/A



思路：典型greedy，只要每次都先取出剩余硬币中最大的就行了。但是我一开始提交的时候循环语句用的是for i in [list]一直没通过，可能是这个语句不能用于重复的元素？

**20min**

代码

```python
n=int(input())
l=sorted(list(map(int,input().split())),reverse=True)
a,b=0,0
while b<=sum(l):
    a+=1
    b+=l[0]
    del l[0]
print(a)
```



代码运行截图![image-20251003192237219](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251003192237219.png)





### 1879B. Chips on the Board

constructive algorithms, greedy, 900, https://codeforces.com/problemset/problem/1879/B



思路：这题需要看出捷径，一开始觉得很复杂，尝试了好久，后来发现问题可以转化成每个列表中的最小值分别与另外一个列表中的所有元素相加之后再取最小值，那样问题就简化很多了。但是花了半天才看出来😫

**30min**

代码

```python
n=int(input())
l=[]    #储存每一组测试数据的结果
for i in range(n):
    a=int(input())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    x,y=min(l1),min(l2)
    num1=sum(l1)+y*a
    num2=sum(l2)+x*a
    num=min(num1,num2)
    l.append(num)
for i in l:
    print(i)
```



代码运行截图![image-20251003203933286](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251003203933286.png)





### M01017: 装箱问题

greedy, http://cs101.openjudge.cn/pctbook/M01017/


思路：思路比较直接，就是从大到小，先确保有大的盒子的包裹利用率尽可能高，再解决小的，但是操作起来非常麻烦，一不留神就会把代码的顺序搞错，或者忘记讨论。几经周折终于AC，内心还是很有成就感的~~

**2h**

代码

```python
from math import ceil
flag=True
x=[]
while flag:
    l=list(map(int,input().split()))
    a=l[5]+l[4]+l[3]+l[2]//4
    l[0]=max(0,l[0]-l[4]*11)
    if l[1]-l[3]*5>0:
        l[1]-=l[3]*5
    else:
        l[0]=max(0,l[0]-4*(l[3]*5-l[1]))
        l[1]=0
    if l[2]%4==1:
        a+=1
        if l[1]-5>0:
            l[1]-=5
            l[0]=max(0,l[0]-7)
        else:
            l[0]=max(0,l[0]-(27-4*l[1]))
            l[1]=0
    elif l[2]%4==2:
        a+=1
        if l[1]-3>0:
            l[1]-=3
            l[0]=max(0,l[0]-6)
        else:
            l[0]=max(0,l[0]-(18-4*l[1]))
            l[1]=0
    elif l[2]%4==3:
        a+=1
        if l[1]-1>0:
            l[1]-=1
            l[0]=max(0,l[0]-5)
        else:
            l[0]=max(0,l[0]-(9-4*l[1]))
            l[1]=0
    if l[1]!=0:
        if l[1]%9==0:
            a+=l[1]//9
        else:
            a+=l[1]//9+1
            l[0]=max(0,l[0]-(36-l[1]%9*4))
    if l[0]!=0:
        a+=ceil(l[0]/36)
    if a==0:
        flag=False
    else:
        x.append(a)
for i in x:
    print(i)
```



代码运行截图![image-20251003233038544](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251003233038544.png)





### M01008: Maya Calendar

implementation, http://cs101.openjudge.cn/practice/01008/



思路：一开始花了大量时间研究正则表达式，后面发现已知格式的可以直接用split加上切片解决。后面的过程虽然繁琐但思路是简单的，第一次提交又是WA，后来发现跟上面那题一样，还是整除要讨论的问题。这下吃一堑长一智了。

**1.5h**

代码

```python
n=int(input())
l=[]
d1={'pop':1,'no':2,'zip':3,'zotz':4,'tzec':5,'xul':6,'yoxkin':7,'mol':8,'chen':9,'yax':10,
    'zac':11,'ceh':12,'mac':13,'kankin':14,'muan':15,'pax':16,'koyab':17,'cumhu':18,'uayet':19}
l1=['imix','ik','akbal','kan','chicchan','cimi','manik','lamat','muluk','ok','chuen','eb','ben','ix','mem','cib','caban','eznab','canac','ahau']*13
l2=[str(i) for i in range(1,14)]*20
def g(x):
    return l2[x-1]+' '+l1[x-1]
for i in range(n):
    haab=input()
    date,mon,year=int(haab.split('.')[0]),d1[haab.split('.')[1].split()[0]],int(haab.split('.')[1].split()[1])
    days=date+1+(mon-1)*20+year*365
    yearr=days//260
    if days%260==0:
        tzolkin=g(days%260)+' '+str(yearr-1)
    else:
        tzolkin=g(days%260)+' '+str(yearr)
    l.append(tzolkin)
print(n)
for i in l:
    print(i)
```



代码运行截图![image-20251005101203450](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251005101203450.png)





### 230B. T-primes（选做）

binary search, implementation, math, number theory, 1300, http://codeforces.com/problemset/problem/230/B



思路：已经尽力了，因为没学筛所以优化了好几次都是超时，这段代码是目前我能做到的最简版本了。后面还要继续努力。

**2h**

代码

```python
from math import sqrt
def g(x):
    if x==2 or x==3 or x==5 or x==7 or x==11 or x==13 or x==17 or x==19:
        return True
    elif x%2==0 or x%3==0 or x%5==0 or x%7==0 or x%11==0 or x%13==0 or x%17==0 or x%19==0:
        return False
    else:
        done=True
        for j in range(19,int(x**0.5)+1,6):
            p=j+4
            if x%j==0 or x%p==0:
                done=False
        return done
n=int(input())
l=list(map(int,input().split()))
lst=[]
def f(x):
    if int(x)==x:
        return True
    else:
        return False
for i in l:
    a=sqrt(i)
    if f(a) and a>=2:
        if g(a):
            lst.append('YES')
        else:
            lst.append('NO')
    else:
        lst.append('NO')
for k in lst:
    print(k)
```



代码运行截图![image-20251007164147450](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20251007164147450.png)





## 2. 学习总结和收获

现在作业耗时明显增加，到了现阶段，还在靠吃老本用简单的分支和循环结构已经AC 不了多少题目了。后面还需要把一部分精力投入高难度算法的学习中。压力大是正常的，尽量用book the flight这本书做好预习吧






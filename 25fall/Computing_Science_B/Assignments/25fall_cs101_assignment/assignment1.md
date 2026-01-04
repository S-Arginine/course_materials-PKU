# Assignment #1: 自主学习

Updated 1306 GMT+8 Sep 14, 2025

2025 fall, Complied by **金安逊 化学与分子工程学院**

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

### E02733: 判断闰年

http://cs101.openjudge.cn/pctbook/E02733/



思路：运用分支结构，依次判断所有可能是闰年的情况：整百年份需能整除400，整十年份需能整除4.

时间：5min

代码

```python
a=int(input())
if a%100==0:
    if a%400==0:
        print('Y')
    else:
        print('N')
else:
    if a%4==0:
        print('Y')
    else:
        print('N')
```



代码运行截图 ![image-20250919185622845](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919185622845.png)





### E02750: 鸡兔同笼

http://cs101.openjudge.cn/pctbook/E02750/



思路：易知奇数条腿不符题意，偶数条腿全是鸡时数目最多，全是兔子时数目最少。若不能被四整除，就把一只兔子换成一只鸡。

时间：4min

代码

```python
a=int(input())
if a%2 !=0 or a<0 or a>=32768:
    print('0 0')
elif a%4==0:
    print(int(a/4),int(a/2))
else:
    print(int((a+2)/4),int(a/2))
```



代码运行截图 ![image-20250919190234078](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919190234078.png)





### 50A. Domino piling

greedy, math, 800, http://codeforces.com/problemset/problem/50/A

时间：10min

思路：分类讨论，偶数比较直接，奇数经简单尝试发现无论什么样的M*N都可以拆分成一个3×3和一个偶数×偶数的板，再化归就可以了。

代码

```python
num_list=input().split()
M=int(num_list[0])
N=int(num_list[1])
if M%2==0 or N%2==0:
    print(int(M*N/2))
else:
    print(int((M*N-1)/2))
```



代码运行截图 ![image-20250919195114980](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919195114980.png)





### 1A. Theatre Square

math, 1000, https://codeforces.com/problemset/problem/1/A



思路：将问题转化为分别将长和宽除以小正方形的面积并向上取整。

时间：12min

代码

```python
data_list=list(map(int,input().split()))
def quzheng(x):
    y=int(x)    
if x==y:        
return y    
else:        
return y+1
a=quzheng(data_list[0]/data_list[2])
b=quzheng(data_list[1]/data_list[2])
print(a*b)
```



代码运行截图 ![image-20250919191822773](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919191822773.png)





### 112A. Petya and Strings

implementation, strings, 1000, http://codeforces.com/problemset/problem/112/A



思路：由于不考虑大小写，先将字符串统一为小写。再用列表的检索功能对每个字母逐一比较

时间：18min

代码

```python
list_1=list(input().lower())
list_2=list(input().lower())
for i in range(0,len(list_1)):
    if list_1[i]>list_2[i]:
        print('1')
        break
    if list_1[i]<list_2[i]:
        print('-1')
        break
    else:
        if i==len(list_1)-1:
            print('0')
```



代码运行截图 ![image-20250919201202578](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919201202578.png)





### 231A. Team

bruteforce, greedy, 800, http://codeforces.com/problemset/problem/231/A



思路：将每行输入的3个数转化为列表，再统计每个列表中”1“出现的个数即可。

时间：5min

代码

```python
n=int(input())
m=0
for i in range(0,n):
    num_list=input().split()
    if num_list.count('1')>=2:
        m+=1
print(m)
```



代码运行截图![image-20250919203704208](C:\Users\金安逊\AppData\Roaming\Typora\typora-user-images\image-20250919203704208.png)





## 2. 学习总结和收获

大致掌握了简单的分支结构和循环结构。学会了如join(),split(),lower(),append(),map()等函数的常见用法，对列表的创建和索引方法也有所掌握。但是还不能较快地找到最简洁的代码表现方式。

OpenJudge另外做了10道Easy题，但都不是很熟练，在一步步慢慢学习。






# Final Exam Cheat Sheet-2

compiled by <mark>金安逊 化学与分子工程学院</mark>

注：大部分为AI生成，但经过筛选

## 强制保留n位小数

```python
print(f'{a:.nf}')   #a必须为浮点型或整型
```

## 标签体系（Tags）

本书使⽤标签来标识题⽬主要考察的算法或数据结构。常⻅标签包括：

- 搜索类：dfs, bfs, brute force
- 分治类：binary search, recursion
- 优化类：dp, greedy
- 数据结构类：stack, tree, graph, dict, set
- 基础类：implementation, math, strings, matrices, sorting
- 技巧类：two pointers, number theory, physics

## 编程细节与易错点

- **变量初始化**：使⽤前确保变量已正确初始化，尤其是布尔标志、计数器、累加器等。
- **多组数据处理**：若题⽬包含多组测试数据，注意每次循环后重置相关变量和数据结构，避免状态残留。
- **DFS 回溯**：进⼊下⼀层后修改了状态，回退时需恢复原状（如标记数组 visited 的撤销）。
- **遍历与修改**：避免在遍历 list 的同时对其进⾏增删操作，建议使⽤副本或记录待操作项。
- **数据类型注意**：
  - 字符串排序按字典序，整数排序按数值⼤⼩；
  - 注意类型转换（如 int() 、 str() ）避免隐式错误。
- **Python 缩进规范**：缩进决定代码块结构，混⽤空格与 Tab 可能导致逻辑错误或语法错误。
- **深拷⻉ vs 浅拷⻉**：
  - 修改嵌套对象时，浅拷⻉可能导致意外共享；
  - 必要时使⽤ copy.deepcopy() 避免副作⽤。

## ASCII码表（十进制+字符）

- <mark>获取ASCII码：ord()</mark>
- <mark>获取编码对应的字符：chr()</mark>

### 控制字符 (0-31, 127)

| Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 0    | NUL  | 7    | BEL  | 14   | SO   | 21   | NAK  | 28   | FS   |
| 1    | SOH  | 8    | BS   | 15   | SI   | 22   | SYN  | 29   | GS   |
| 2    | STX  | 9    | TAB  | 16   | DLE  | 23   | ETB  | 30   | RS   |
| 3    | ETX  | 10   | LF   | 17   | DC1  | 24   | CAN  | 31   | US   |
| 4    | EOT  | 11   | VT   | 18   | DC2  | 25   | EM   | 127  | DEL  |
| 5    | ENQ  | 12   | FF   | 19   | DC3  | 26   | SUB  |      |      |
| 6    | ACK  | 13   | CR   | 20   | DC4  | 27   | ESC  |      |      |

### 可打印字符 (32-126)

#### 符号与数字 (32-63)

| Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 32   | 空格 | 39   | '    | 46   | .    | 53   | 5    | 60   | <    |
| 33   | !    | 40   | (    | 47   | /    | 54   | 6    | 61   | =    |
| 34   | "    | 41   | )    | 48   | 0    | 55   | 7    | 62   | >    |
| 35   | #    | 42   | *    | 49   | 1    | 56   | 8    | 63   | ?    |
| 36   | $    | 43   | +    | 50   | 2    | 57   | 9    |      |      |
| 37   | %    | 44   | ,    | 51   | 3    | 58   | :    |      |      |
| 38   | &    | 45   | -    | 52   | 4    | 59   | ;    |      |      |

#### 大写字母与部分符号 (64-95)

| Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 64   | @    | 71   | G    | 78   | N    | 85   | U    | 92   | \    |
| 65   | A    | 72   | H    | 79   | O    | 86   | V    | 93   | ]    |
| 66   | B    | 73   | I    | 80   | P    | 87   | W    | 94   | ^    |
| 67   | C    | 74   | J    | 81   | Q    | 88   | X    | 95   | _    |
| 68   | D    | 75   | K    | 82   | R    | 89   | Y    |      |      |
| 69   | E    | 76   | L    | 83   | S    | 90   | Z    |      |      |
| 70   | F    | 77   | M    | 84   | T    | 91   | [    |      |      |

#### 小写字母与符号 (96-126)

| Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char | Dec  | Char |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 96   | `    | 103  | g    | 110  | n    | 117  | u    | 124  | \|   |
| 97   | a    | 104  | h    | 111  | o    | 118  | v    | 125  | }    |
| 98   | b    | 105  | i    | 112  | p    | 119  | w    | 126  | ~    |
| 99   | c    | 106  | j    | 113  | q    | 120  | x    |      |      |
| 100  | d    | 107  | k    | 114  | r    | 121  | y    |      |      |
| 101  | e    | 108  | l    | 115  | s    | 122  | z    |      |      |
| 102  | f    | 109  | m    | 116  | t    | 123  | {    |      |      |

## Python 集合变换函数大全

### 一、集合创建与基本操作

#### 1. **创建集合**

```python
# 空集合
s1 = set()  # 注意：不能用 {} 创建空集合，{} 创建的是字典
s2 = {1, 2, 3}  # 非空集合

# 从其他可迭代对象创建
s3 = set([1, 2, 2, 3, 3])  # {1, 2, 3}
s4 = set("hello")  # {'h', 'e', 'l', 'o'}
s5 = set({"a": 1, "b": 2})  # {'a', 'b'} - 只取键

# 不可变集合（frozenset）
fs = frozenset([1, 2, 3])  # 不可变，可用作字典键
```



#### 2. **添加元素**

```python
s = {1, 2, 3}

# add() - 添加单个元素
s.add(4)  # {1, 2, 3, 4}
s.add(2)  # 已存在，无变化

# update() - 添加多个元素
s.update([5, 6, 7])  # {1, 2, 3, 4, 5, 6, 7}
s.update({8, 9})  # 添加集合
s.update("ab")  # 添加字符串字符 {'a', 'b', ...}
```



#### 3. **删除元素**

```python
s = {1, 2, 3, 4, 5, 6}

# remove() - 删除指定元素（不存在则报错）
s.remove(3)  # {1, 2, 4, 5, 6}

# discard() - 删除指定元素（不存在不报错）
s.discard(2)  # {1, 4, 5, 6}
s.discard(99)  # 不报错

# pop() - 随机删除并返回一个元素
item = s.pop()  # 随机删除一个

# clear() - 清空集合
s.clear()  # set()
```



### 二、集合运算（返回新集合）

#### 1. **并集（Union）**

```python
a = {1, 2, 3}
b = {3, 4, 5}

# union() 方法
c = a.union(b)  # {1, 2, 3, 4, 5}

# | 运算符
c = a | b  # {1, 2, 3, 4, 5}

# 多个集合
d = {5, 6, 7}
e = a.union(b, d)  # {1, 2, 3, 4, 5, 6, 7}
```



#### 2. **交集（Intersection）**

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# intersection() 方法
c = a.intersection(b)  # {3, 4}

# & 运算符
c = a & b  # {3, 4}

# 多个集合
c = {2, 3, 4}
d = {3, 4, 5}
e = a.intersection(b, c, d)  # {3, 4}
```



#### 3. **差集（Difference）**

```python
a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7}

# difference() 方法
c = a.difference(b)  # {1, 2, 3} (在a中但不在b中)

# - 运算符
c = a - b  # {1, 2, 3}

# 多个集合
c = {3, 4, 5}
d = {5, 6, 7}
e = a.difference(b, c, d)  # {1, 2}
```



##  二分查找

> 1. 初始化：
>    - 设置左边界 `left` 为 0，右边界 `right` 为数据集的最后一个索引。
> 2. 查找过程：
>    - 计算中间位置 `mid`。
>    - 如果中间位置的元素等于目标元素，返回其索引。
>    - 如果中间位置的元素小于目标元素，调整左边界 `left` 为 `mid + 1`。
>    - 如果中间位置的元素大于目标元素，调整右边界 `right` 为 `mid - 1`。
>    - 重复上述步骤，直到找到目标元素或左边界超过右边界。
> 3. 未找到目标元素：
>    - 如果左边界超过右边界，返回 -1。

### 一、核心函数详解

#### 1. **bisect_left() - 左侧插入点**

```py
import bisect

# 在有序列表中查找插入位置，如果元素已存在，插入到相同元素的左侧
arr = [1, 2, 4, 4, 5, 6, 7]

# 查找插入点（返回索引）
pos = bisect.bisect_left(arr, 4)  # 2 - 在第一个4的位置
print(f"插入位置: {pos}")

pos = bisect.bisect_left(arr, 3)  # 2 - 应该插入到4的位置（左侧）
print(f"插入位置: {pos}")

pos = bisect.bisect_left(arr, 0)  # 0 - 插入到最前面
print(f"插入位置: {pos}")

pos = bisect.bisect_left(arr, 8)  # 7 - 插入到最后
print(f"插入位置: {pos}")
```



#### 2. **bisect_right() / bisect() - 右侧插入点**

```py
import bisect

arr = [1, 2, 4, 4, 5, 6, 7]

# 查找插入位置，如果元素已存在，插入到相同元素的右侧
pos = bisect.bisect_right(arr, 4)  # 4 - 在最后一个4的后面
print(f"插入位置: {pos}")

pos = bisect.bisect(arr, 4)  # bisect是bisect_right的别名
print(f"插入位置: {pos}")

pos = bisect.bisect_right(arr, 3)  # 2 - 和bisect_left一样（因为3不存在）
print(f"插入位置: {pos}")
```



#### 3. **insort_left() - 左侧插入**

```py
import bisect

arr = [1, 2, 4, 4, 5, 6, 7]

# 插入元素，保持列表有序（插入到相等元素的左侧）
bisect.insort_left(arr, 4)  # 在第一个4的位置插入
print(arr)  # [1, 2, 4, 4, 4, 5, 6, 7]

bisect.insort_left(arr, 3)  # 插入不存在的元素
print(arr)  # [1, 2, 3, 4, 4, 4, 5, 6, 7]
```



#### 4. **insort_right() / insort() - 右侧插入**

```python
import bisect

arr = [1, 2, 4, 4, 5, 6, 7]

# 插入元素，保持列表有序（插入到相等元素的右侧）
bisect.insort_right(arr, 4)  # 在最后一个4的后面插入
print(arr)  # [1, 2, 4, 4, 4, 5, 6, 7]

bisect.insort(arr, 4)  # insort是insort_right的别名
print(arr)  # [1, 2, 4, 4, 4, 4, 5, 6, 7]
```



### 二、参数详解

所有函数都支持以下参数：

```python
bisect.bisect_left(a, x, lo=0, hi=len(a))
bisect.bisect_right(a, x, lo=0, hi=len(a))
bisect.insort_left(a, x, lo=0, hi=len(a))
bisect.insort_right(a, x, lo=0, hi=len(a))
```

- `a`: 有序列表
- `x`: 要查找/插入的值
- `lo`: 查找范围的起始索引（默认为0）
- `hi`: 查找范围的结束索引（默认为列表长度）



## 按数组特定元素排序的多种方法

### 一、使用 `sorted()` 函数（最常用）

#### 基本用法：按数组第二个元素排序

```python
# 示例数据：每个数组有3个元素
arrays = [
    [1, 5, 3],
    [2, 3, 8],
    [3, 8, 1],
    [4, 1, 4]
]

# 按每个数组的第二个元素（索引1）排序
sorted_by_second = sorted(arrays, key=lambda x: x[1])
print("按第二个元素排序:")
for arr in sorted_by_second:
    print(arr)
# 输出：
# [4, 1, 4]    # 第二个元素是1
# [2, 3, 8]    # 第二个元素是3
# [1, 5, 3]    # 第二个元素是5
# [3, 8, 1]    # 第二个元素是8
```

#### 按任意索引位置排序

```python
arrays = [
    ['Alice', 25, 'Engineer'],
    ['Bob', 30, 'Doctor'],
    ['Charlie', 22, 'Student'],
    ['David', 30, 'Teacher']
]

# 1. 按年龄（索引1）排序
sorted_by_age = sorted(arrays, key=lambda x: x[1])
print("按年龄排序:", sorted_by_age)

# 2. 按姓名（索引0）排序
sorted_by_name = sorted(arrays, key=lambda x: x[0])
print("按姓名排序:", sorted_by_name)

# 3. 按职业（索引2）排序
sorted_by_job = sorted(arrays, key=lambda x: x[2])
print("按职业排序:", sorted_by_job)
```

### 二、数值相同时稳定排序

1. **Python的`sort()`和`sorted()`是稳定排序**

2. **相同元素的相对顺序保持不变**

3. **这个特性让多级排序变得简单**：

   ```python
   # 想要：先按A，再按B，再按C
   data.sort(key=lambda x: x['C'])
   data.sort(key=lambda x: x['B'])
   data.sort(key=lambda x: x['A'])
   ```
   
4. **性能不受影响**：稳定排序不一定比不稳定排序慢

5. **大多数时候这是优点**：保持顺序通常是期望的行为



## 字典按值排序的多种方法

### 一、基础方法：使用 `sorted()` 和 `lambda`

#### 1. **按键值对排序（返回元组列表）**

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

# 按值升序排序
sorted_by_value = sorted(scores.items(), key=lambda x: x[1])
print("按值升序:", sorted_by_value)
# 输出: [('Charlie', 78), ('Alice', 85), ('Bob', 92), ('David', 95)]

# 按值降序排序
sorted_by_value_desc = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print("按值降序:", sorted_by_value_desc)
# 输出: [('David', 95), ('Bob', 92), ('Alice', 85), ('Charlie', 78)]
```

#### 2. **只获取排序后的键**

```python
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 95}

# 按键升序
sorted_keys = sorted(scores)
print("按键升序:", sorted_keys)
# 输出: ['Alice', 'Bob', 'Charlie', 'David']

# 按值升序排序键
keys_by_value = sorted(scores, key=lambda x: scores[x])
print("按值排序键:", keys_by_value)
# 输出: ['Charlie', 'Alice', 'Bob', 'David']

# 按值降序排序键
keys_by_value_desc = sorted(scores, key=lambda x: scores[x], reverse=True)
print("按值降序键:", keys_by_value_desc)
# 输出: ['David', 'Bob', 'Alice', 'Charlie']
```

### 二、总结对比表

| 需求           | 代码                                               | 返回类型   |
| :------------- | :------------------------------------------------- | :--------- |
| 按值排序键值对 | `sorted(dict.items(), key=lambda x: x[1])`         | 列表(元组) |
| 只按键排序     | `sorted(dict)` 或 `sorted(dict.keys())`            | 列表(键)   |
| 按值排序键     | `sorted(dict, key=dict.get)`                       | 列表(键)   |
| 保留为有序字典 | `dict(sorted(dict.items(), key=lambda x: x[1]))`   | 字典       |
| 使用itemgetter | `sorted(dict.items(), key=itemgetter(1))`          | 列表(元组) |
| 多级排序       | `sorted(dict.items(), key=lambda x: (x[1], x[0]))` | 列表(元组) |



## `heapq` 模块完全指南

`heapq` 是 Python 的**堆队列算法**（最小堆）的标准库实现。让我们详细讲解所有功能：

### 一、基本概念：最小堆

`heapq` 实现的是**最小堆**：

- 堆顶元素永远是最小的
- 父节点 ≤ 子节点
- 用**列表**实现，但需要调用 heapq 函数来维护堆性质

### 二、所有函数详解（共 8 个）

#### 1. **heapify(x)** - 将列表原地转为堆

```python
import heapq

# 普通列表
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print("原始列表:", arr)  # [3, 1, 4, 1, 5, 9, 2, 6]

# 转为堆（原地修改，时间复杂度 O(n)）
heapq.heapify(arr)
print("堆化后:", arr)    # [1, 1, 2, 3, 5, 9, 4, 6]

# 验证堆性质：arr[0] 是最小值
print("最小值:", arr[0])  # 1
```



#### 2. **heappush(heap, item)** - 插入元素

```python
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
print("插入后:", heap)  # [1, 2, 8, 5]

# 插入复杂元素（元组会自动按第一个元素比较）
heap = []
heapq.heappush(heap, (3, 'task3'))
heapq.heappush(heap, (1, 'task1'))
heapq.heappush(heap, (2, 'task2'))
print("元组堆:", heap)  # [(1, 'task1'), (3, 'task3'), (2, 'task2')]
```



#### 3. **heappop(heap)** - 弹出最小值

```python
heap = [1, 3, 5, 7, 9, 2, 4]
heapq.heapify(heap)

print("弹出前:", heap)        # [1, 3, 2, 7, 9, 5, 4]
min_val = heapq.heappop(heap)
print("弹出值:", min_val)      # 1
print("弹出后堆:", heap)       # [2, 3, 4, 7, 9, 5]

# 连续弹出得到排序序列
sorted_list = []
while heap:
    sorted_list.append(heapq.heappop(heap))
print("排序结果:", sorted_list)  # [2, 3, 4, 5, 7, 9]
```



#### 4. **heappushpop(heap, item)** - 插入后弹出最小值

```python
# 比先 push 再 pop 更高效
heap = [2, 3, 5]
heapq.heapify(heap)

# 插入 4 然后弹出最小值
result = heapq.heappushpop(heap, 4)
print("弹出值:", result)    # 2（最小值）
print("堆状态:", heap)      # [3, 4, 5]

# 插入的值比最小值还小
result = heapq.heappushpop(heap, 1)
print("弹出值:", result)    # 1（插入的值）
print("堆状态:", heap)      # [3, 4, 5]
```



#### 5. **heapreplace(heap, item)** - 弹出后插入

```python
# 先弹出最小值，再插入新值（与 heappushpop 顺序相反）
heap = [2, 3, 5]
heapq.heapify(heap)

# 弹出最小值，然后插入 4
result = heapq.heapreplace(heap, 4)
print("弹出值:", result)    # 2
print("堆状态:", heap)      # [3, 4, 5]

# 对比 heappushpop 和 heapreplace 的区别
heap1 = [10, 20, 30]
heap2 = [10, 20, 30]

val1 = heapq.heappushpop(heap1, 5)   # 先插入5，再弹出最小值
val2 = heapq.heapreplace(heap2, 5)   # 先弹出最小值，再插入5

print(f"heappushpop: 弹出{val1}, 堆{heap1}")  # 弹出5, 堆[10, 20, 30]
print(f"heapreplace: 弹出{val2}, 堆{heap2}")  # 弹出10, 堆[5, 20, 30]
```



#### 6. **nlargest(n, iterable, key=None)** - 最大的 n 个元素

```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 最大的3个元素
largest = heapq.nlargest(3, nums)
print("最大的3个:", largest)  # [42, 37, 23]

# 最大的3个元素（带key函数）
students = [
    {'name': 'Alice', 'score': 85},
    {'name': 'Bob', 'score': 92},
    {'name': 'Charlie', 'score': 78},
    {'name': 'David', 'score': 95},
    {'name': 'Eve', 'score': 88}
]

# 按分数取最高的2个
top_students = heapq.nlargest(2, students, key=lambda x: x['score'])
print("最高分2人:", top_students)
# [{'name': 'David', 'score': 95}, {'name': 'Bob', 'score': 92}]
```



#### 7. **nsmallest(n, iterable, key=None)** - 最小的 n 个元素

```python
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 最小的3个元素
smallest = heapq.nsmallest(3, nums)
print("最小的3个:", smallest)  # [-4, 1, 2]

# 最小的3个元素（带key函数）
products = [
    {'name': 'A', 'price': 100},
    {'name': 'B', 'price': 50},
    {'name': 'C', 'price': 200},
    {'name': 'D', 'price': 30},
    {'name': 'E', 'price': 150}
]

cheapest = heapq.nsmallest(2, products, key=lambda x: x['price'])
print("最便宜的2个:", cheapest)
# [{'name': 'D', 'price': 30}, {'name': 'B', 'price': 50}]
```



#### 8. **merge(\*iterables, key=None, reverse=False)** - 合并多个有序序列

```python
# 合并多个有序序列（归并排序的思想）
sorted1 = [1, 3, 5, 7]
sorted2 = [2, 4, 6, 8]
sorted3 = [0, 10, 20]

merged = list(heapq.merge(sorted1, sorted2, sorted3))
print("合并结果:", merged)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 20]

# 合并文件内容（惰性迭代，节省内存）
def merge_files(file1, file2, output):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output, 'w') as out:
        for line in heapq.merge(f1, f2):
            out.write(line)
```



### 三、高级技巧和注意事项

#### 1. **如何实现最大堆？**

由于 `heapq` 只提供最小堆，可以用负数实现最大堆：

```python
# 最大堆技巧：存储负数
nums = [3, 1, 4, 1, 5]
max_heap = []

for num in nums:
    heapq.heappush(max_heap, -num)  # 存负数

# 获取最大值
max_val = -heapq.heappop(max_heap)
print("最大值:", max_val)  # 5

# 或者使用元组
max_heap = []
for num in nums:
    heapq.heappush(max_heap, (-num, num))  # (-优先级, 实际值)
```



## 埃氏筛模板

### 算法步骤：

1. 创建一个长度为 n+1*n*+1 的布尔数组 `is_prime`，初始化所有元素为 `True`（表示假设所有数都是质数）。将索引 0 和 1 设为 `False`（因为它们不是质数）。
2. 从 p=2*p*=2 开始，循环到 n*n*：
   - 如果 `is_prime[p]` 为 `True`，则 p*p* 是质数。
   - 然后将 p*p* 的所有倍数（从 p2*p*2 开始到 n*n*）标记为 `False`（即合数）。
3. 遍历完成后，所有 `is_prime[i]` 为 `True` 的 i*i* 就是质数。

### 时间复杂度：

- 时间复杂度为 O*(*n*loglog*n*)，空间复杂度为 O(n)。

### Python 实现：

```python
def sieve_of_eratosthenes(n):
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for p in range(2, int(n ** 0.5) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
    primes = [i for i, prime in enumerate(is_prime) if prime]
    return primes

# 示例：找出小于 30 的质数
print(sieve_of_eratosthenes(30))  # 输出 [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

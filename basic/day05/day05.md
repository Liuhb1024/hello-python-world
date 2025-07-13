# 今日目标
- 理解什么是模块（module）、包（package）和导入（import）
- 学会拆分代码到多个文件，做到"结构清晰、复用方便"
- 掌握 Python 的常用标准库：random、datetime、os 等
- 实战项目：构建一个"简易工具包"，模块化地封装多个功能

## 一、模块和包详解（基础 + 工程实践）

### 什么是模块（module）？
模块就是一个 .py 文件，里面可以定义函数、类、变量。
模块的作用就是：把代码逻辑分开，方便复用和维护。

✅ 示例：math_utils.py

```python
def add(x, y):
    return x + y
```

然后在主程序中用：

```python
from math_utils import add
print(add(3, 5))  # 输出 8
```

### 什么是包（package）？
包就是一个包含 __init__.py 的文件夹。
这个文件夹中可以放多个模块文件，让你组织一组相关功能。

✅ 文件结构示例：

```
my_project/
├── main.py
└── tools/
    ├── __init__.py
    ├── math_utils.py
    └── string_utils.py
```

### 如何导入模块？

| 导入方式 | 写法 | 使用方式 |
|----------|------|----------|
| 导入整个模块 | `import math_utils` | `math_utils.add()` |
| 导入某个函数 | `from math_utils import add` | `add()` |
| 改名 | `import math_utils as mu` | `mu.add()` |

## 二、Python 标准库精讲（内置的工具箱）

Python 有很多自带的强大工具，叫做"标准库"，不需要安装就能用！

### datetime 日期时间工具

```python
import datetime

now = datetime.datetime.now()
print("现在时间是：", now)

today = datetime.date.today()
print("今天是：", today)

# 字符串转时间
dt = datetime.datetime.strptime("2025-07-01", "%Y-%m-%d")
print("转化后时间对象：", dt)
```

### random 随机数生成器

```python
import random

print(random.randint(1, 100))   # 生成 1~100 的整数
print(random.choice(['a', 'b', 'c']))  # 随机选一个元素
print(random.sample(range(10), 3))  # 随机取多个不重复的
```

### os 与文件/路径操作

```python
import os

print(os.getcwd())  # 获取当前目录
os.mkdir("test_folder")  # 创建文件夹
os.remove("test.txt")    # 删除文件

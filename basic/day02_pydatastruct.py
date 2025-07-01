"""
Day 2: Python Data Structures
"""
# 一、列表 list：有序】可变的元素集合
fruits = ['apple', 'banana', 'cherry']
print(fruits)  # 输出: ['apple', 'banana', 'cherry']
print(fruits[0])  # 输出: apple
fruits.append('orange')  # 添加元素
fruits.remove('banana')  # 删除元素
print(len(fruits))  # 输出: 3
# 常见操作：
# 遍历 
for fruit in fruits:
    print(fruit)
# 切片
print(fruits[1:3])  # 输出: ['cherry', 'orange']
# 排序
fruits.sort()  # 排序
print(fruits)  # 输出: ['apple', 'cherry', 'orange']

# 二、元组 tuple：有序】不可变的元素集合
point = (10, 20)
print(point)  # 输出: (10, 20)
print(point[0])  # 输出: 10
# 元组的元素不可修改
# 下面的代码给我抛出异常
try:
    point[0] = 15  # 会报错，因为元组是不可变的
except TypeError as e:
    print(f"Error: {e}")
# 常用于函数返回多个值、或者固定坐标场景

# 三、集合 set：无序】不重复的元素集合
colors = {'red', 'green', 'blue'}
print(colors)  # 输出: {'red', 'green', 'blue'}
colors.add('yellow')  # 添加元素
colors.remove('green')  # 删除元素
colors.add('red')  # 添加重复元素不会报错
print(colors)  # 输出: {'red', 'blue', 'yellow'}
# 常用于去重、集合运算

# 四、字典 dict：无序】键值对集合
student = {'name': 'Alice', 'age': 20, 'grade': 'A'}
print(student)
print(student['name'])  # 输出: Alice
student['grade'] = 'B'  # 修改值
student['gender'] = 'man'  # 添加新键值对
print(student)  

"""
dict + list 练习：学生成绩管理系统
💼 目标：
创建一个程序：
让用户输入学生姓名与成绩；
将学生信息保存在一个列表中；
最后打印所有学生的平均分。
"""

students = []  # 用于存储学生信息的列表

while True:
    name = input("请输入学生姓名（输入 q 退出）")
    if name == 'q':
        break
    socre = float(input(f"请输入{name}的成绩："))
    student_info = {'name': name, 'score': socre}
    students.append(student_info)  # 将学生信息添加到列表中

total = 0
for score in students:
    print(f"学生姓名：{score['name']}，成绩：{score['score']}")
    total += score['score']  # 累加成绩

average_score = total / len(students) if students else 0  # 计算平均分
print(f"所有学生的平均分是：{average_score:.2f}")  # 输出平均分，保留两位小数

def input_students():
    students = []
    while True:
        name = input("请输入学生姓名（输入 q 退出）：")
        if name.lower() == 'q':
            break
        score = float(input(f"请输入 {name} 的成绩："))
        students.append({'name': name, 'score': score})
    return students

def calculate_average(students):
    total = sum(s['score'] for s in students)
    return total / len(students) if students else 0

def display_students(students):
    for s in students:
        print(f"学生姓名：{s['name']}，成绩：{s['score']}")

# 主程序
students = input_students()
display_students(students)
avg = calculate_average(students)
print(f"平均分是：{avg:.2f}")

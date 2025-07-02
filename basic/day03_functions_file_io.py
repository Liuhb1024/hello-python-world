"""
day03_functions_file_io
"""
# 一、函数基础
def greet(name):
    """
    打招呼函数
    :param name: 姓名
    :return: None
    """
    return f"Hello, {name}!"

message = greet("Alice")
print(message)  # 输出: None，因为 greet 函数没有返回值

#  二、字符串处理技巧
s = " Hello,  World! "
print(s.strip())  # 去除首尾空格
print(s.lower())  # 转为小写
print(s.upper())  # 转为大写
print(s.replace("World", "Python"))  # 替换字符串
print(s.split(","))  # 分割字符串
print(s.find("World"))  # 查找子字符串位置

name = "Alice"
score = 95
print(f"{name} 的成绩是 {score}")  # 格式化字符串

# 三、文件读写
# 创建一个文本文件并写入内容
with open("./basic/day03_scores.txt", "w", encoding="utf-8") as f:
    f.write("Alice, 95\n")
    f.write("Bob, 85\n")
    f.write("Charlie, 90\n")
# 读取文件内容
with open("./basic/day03_scores.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())  # strip() 去除行末换行符

"""
🛠️ 实战项目：学生成绩持久化系统 v2
    🧱 功能目标：
    接收学生姓名和成绩；
    把数据写入 students.txt 文件中；
    程序结束后能读取并显示所有成绩和平均分。
"""
def input_student_scores(name, score):
    with open("./basic/day03_score.txt", "a", encoding="utf-8") as f:
        f.write(f"{name}, {score}\n")

def read_student_scores():
    students = []
    try:
        with open("./basic/day03_score.txt", "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split()
                students.append({'name': name, 'score': float(score)})
            return students
    except FileNotFoundError:
        print("文件不存在，返回空列表")

def calculate_average(students):
    total = sum(s['score'] for s in students)
    return total / len(students) if students else 0

while True:
    name = input("请输入学生姓名（输入 q 退出）：")
    if name.lower() == 'q':
        break
    score = float(input(f"请输入 {name} 的成绩："))
    input_student_scores(name, score)

students = read_student_scores()
for s in students:
    print(f"学生姓名：{s['name']}，成绩：{s['score']}")
average_score = calculate_average(students)
print(f"所有学生的平均分是：{average_score:.2f}")  # 输出平均分，保留两位小数
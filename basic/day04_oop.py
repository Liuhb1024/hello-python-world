"""
day04:OOP
"""
# 一、类和对象的基本写法
class student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def say_hello(self):
        print(f"你好，我是{self.name},成绩是{self.score}")

s1 = student("张三", 95)
s1.say_hello()

"""
一个学生类创建 Student
要求：
    属性：姓名、年龄、成绩
    方法：
    introduce()：输出介绍自己
    is_passed()：判断成绩是否及格（>= 60）
"""

class Student:
    def __init__(self,name,age,score):
        self.name = name
        self.age = age
        self.score = score

    def is_passed(self):
        if self.score >= 60:
            print("已通过考试") 
        else:
            print("未通过考试")
        
    def introduce(self):
        print(f"我是{self.name},{self.age}岁，考试成绩是{self.score}")

stu = Student("小红", 18, 100)
stu.introduce()
stu.is_passed()

stu2 = Student("小蓝", 19, 45)
stu2.introduce()     # 输出：我是 小蓝，19 岁，考试成绩是 45
stu2.is_passed()     # 输出：考试未通过。

"""
模拟一个班级，添加多个学生，并统计平均成绩。
"""
class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)
    
    def average_score(self):
        if not self.students:
            return 0
        total_score = sum(s.score for s in self.students)
        return total_score / len(self.students)
    
s1 = student("张三", 90)
s2 = student("李四", 80)
cls = Classroom()
cls.add_student(s1)
cls.add_student(s2)
print(f"班级平均分：{cls.average_score():.2f}")

"""
Task:
请输入你的名字: 张三
请输入你的年龄: 20
你好，张三，你是成年人。
"""

def isAdult(age):
    if age >= 18:
        level = '成年人'
    elif age > 0 and age < 18:
        level = "未成年人"
    else:
        print("请重新输入，年龄应该为不为负数的整数")
    return level

print("请输入您的姓名：")
name = input()
print("请输入您的年龄：")
age = int(input())
level = isAdult(age)


print(f"您好！{name},你是{level}")
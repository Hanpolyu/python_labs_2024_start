import json

# 打开并读取JSON文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 获取学生列表
students = data.get('students', [])

# 列出所有学生
for student in students:
    print(f"ID: {student['id']}")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grades: {student['grades']}")
    print()  # 空行分隔每个学生的信息

# print the second student's name
print(students[1]['name'])
print(students[1]['age'])
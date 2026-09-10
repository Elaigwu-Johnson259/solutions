# Date: 10-9-2026
#Exercise_1
student = {"name" : "Alice", "age" : 20, "courses" : ["Math", "Physics"]}
print(student.get("name"))
print(student.get("age"))


#Exercise_2
student["gpa"] = 3.9
student["age"] = (20 +1)
print(student)


#Exercise_3
print(student.get("scholarship", "not eligible"))


#Exercise_4
num1 = {1, 2, 3, 4, 4, 5}
print(num1)
num1.add(6)
num2 = {4, 5, 6, 7}
num3 = num1 & num2
print(num3)

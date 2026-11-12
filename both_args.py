def student_record(name, age, gender, /, *, school, course, level):
    print("Name:", name)
    print("Age:", age)
    print("Gender:", gender)
    print("School:", school)
    print("Course:", course)
    print("Level:", level)

student1 = student_record("Alice", 20, "Female", school="XYZ University", course="Computer Science", level="Undergraduate")
student2 = student_record("Bob", 22, "Male", school="ABC College", course="Mathematics", level="Graduate")
student3 = student_record("Charlie", 19, "male", school="LMN Institute", level="Undergraduate", course="Physics")
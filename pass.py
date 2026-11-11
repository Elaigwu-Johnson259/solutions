def register_student():
    pass

def display_message():
    print("Student registration is coming soon!")

register_student()
display_message()

print("ELIXS registration module loaded.")



def register_student(name, age, course, /):
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)

register_student("Johnson", 25, "Doctor\n")
register_student("Elaigwu", 30, "AI Engineer")
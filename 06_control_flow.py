#Date: 10-9-2026
#Exercise_1
score = 85
if score >= 90:
    print("Excellent")
elif score >= 70 and score <= 89:
    print("Good")
else:
    print("Needs Improvement")



#Exercise_2
age = 20
vote = ("Can Vote") if age >= 18  else ("Cannot Vote")
print(vote)



# Exercise_3
role = input("Are you an admin, editor, author, or guest? \n Enter your role: ")
match role:
    case "admin":
        print("Full access")
    case "editor" | "author":
        print("Write access")
    case "guest":
        print("Read access")
    case _:
        print("No access")


#Exercise_4
items = []
if items:
    print("Items Present")
else:
    print("Empty List")


#Date: 15-9-2026
#Exercise_1
class User:
    def __init__(self, first_name, last_name, username):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username

    def describe_user(self):
        print(f"{self.first_name}\n{self.last_name}\n{self.username}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name} your username is {self.username}, You are welcome onboard!")

#Exercise_2
user1 = User("Elaigwu", "Johnson", "Elly Johnson 259")
user1.describe_user()
user1.greet_user()


#Exercise_3
class Admin(User):
    def __init__(self, first_name, last_name, username):
        super().__init__(first_name, last_name, username)
    
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user"
        ]
    def show_privileges(self):
        print(f"{self.privileges}")

admin1 = Admin("victoria", "abah", "victoria122")

admin1.show_privileges()


# TODO: Exercise 3
# Create a child class named 'Admin' that inherits from 'User'.
# Add an attribute 'privileges' initialized as a list: ["can add post", "can delete post", "can ban user"].
# Add a method 'show_privileges' that prints the admin's privileges.
# Instantiate an Admin object and" call 'show_privileges()'.

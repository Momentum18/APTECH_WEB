"""
class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def greeting(self):
        print(f"Hello {self.fname} and how are you doing? {self.lname}")


class Michael(Person):
    def walk(self):
        print(f"Am walking")

    def eat(self):
        print("I eat")

m1 = Michael("Billy", "Jack")
m1.greeting()
"""


#SCHOOL MANAGEMENT SYSTEM

print("-----------------------SCHOOL MANAGEMENT SYSTEM-------------------------")


def student():
    while True:
        fullname = input("Enter your full name: ")
        email = input("Enter your email: ")
        phone_num = int(input("Enter your phone number: "))
        course = input("Enter your course of study: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        print(f"Welcome to Aptech {fullname}")

        print(f"\nHello {fullname}, please confirm your information before you proceed")

        print(f"your full name is {fullname}")
        print(f"your email is {email}")
        try:
            print(f"your phone number is {phone_num}")
        except ValueError:
            print("Enter your value in integer")

        print(f"your course of study is {course}")

        conf = input("Is the above information correct? type Y or N: ")

        if conf.lower() == "y":
            print("\nYou may proceed to Login details")

            user1 = input("Enter your username: ")
            pass1 = input("Enter your password: ")

            if user1 == username and pass1 == password:
                print("Your login was successful")

            else:
                print("your username or password is incorrect")
                break

        else:
            print("please kindly register")
            break

student()



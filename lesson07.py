students = ["Alex", "Bola", "Miracle", "Amir", "Christiana"]

'''
for newstudent in students:
    if 'Alex' in newstudent:
        print("Alex is part of the list")

for x in range(len(students)):
    print(x)
 '''

# Error handlings in python:
'''
try:
    name = input('Enter your name: ')
    age = int(input('Enter your age: '))
    print(f"Welcome {name}")
    print(f"Your age is {age}")


except ValueError:
    print("Please enter a number value")
'''
# DRY PRINCIPLE(Don't repeat yourself):

# dictionary

students = {
    "name": "Adeola",
    "age": 27,
    "grade": 3.6
}

print(students)
students["age"] = 40
students.update({"grade": "4.0"})

print(students["age"])
print(students.keys())
print(students.values())
print(students.items())

if "age" in students:
    print("Age is present")

for new in students.items():
    print(students)

# FUNCTIONS IN PYTHON:


def hello():
    name = input("Enter your name: ")
    print(f"Good afternoon {name}")

hello()


def addition(num, num1):
    return num + num1

print(addition(7, 40))


def loan():
    print("----------------------ZETA LOAN------------------------")
    name = input("Enter your name: ")
    print(f"Welcome {name} to ZETA LOAN APP ")

    BVN = True
    salary = True
    marital_status = True
    children = int(input("How many children do you have?: "))

    if BVN and salary and marital_status and children == 1:
        print("You are eligible for a loan")
    else:
        print('You are not eligible')


loan()


# LAMBDA FUNCTION:
x = lambda a : a + 10
print(x(5))
x = lambda a, b, c : a * b * c
print(x(5, 4, 6))

def multi(a, b, c):
    return a * b * c
print(multi(5, 4, 6))


# OBJECT ORIENTED PROGRAM in python programming:


class Myobj:
    x = 5
    
print(Myobj.x)


class Person:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color


p1 = Person("Adeola", 30, "black")
print(p1.name)
print(p1.age)
print(p1.color)


class Samsung:
    def __init__(phone, brand, color, camera):
        phone.brand = brand
        phone.color = color
        phone.camera = camera

    def specs(phone):
        print(f"This is a {phone.color} Samsung Galaxy {phone.brand} with {phone.camera} pixel camera")


ph = Samsung("S10", "White", 5.0)
ph.specs()


def myPrintFunction(name):
    print(f"Good Afternoon {name}")


myPrintFunction("Michael")


def best_Friend(names):
    print(f"Thank you {names} for turning up for my graduation ceremony ")


best_Friend("Spencer")


class Loan:
    def __init__(self, BVN, salary, age, marital_status, children):
        self.BVN = BVN
        self.salary = salary
        self.age = age
        self.marital_status = marital_status
        self.children = children

    def validate_method(self):
        if self.BVN == "Yes" and self.salary >= 40000 and self.age >= 18 and self.marital_status == "Married" and self.children == 1:
            print("You are eligible for the Loan package")
        else:
            print("You are not eligible for the Loan package")


l1 = Loan("Yes", 50000, 27, "Married", 1)
l1.validate_method()


class Choir:
    def __init__(self, age, part, experience, gender, mar_status, working_class, color):
        self.age = age
        self.part = part
        self.experience = experience
        self.gender = gender
        self.mar_status = mar_status
        self.working_class = working_class
        self.color = color

    def member_verification(self):
        if self.age >= 18 and self.part == "Tenor" and self.experience >= 5 and self.gender == "Male" and self.mar_status == "Single" and self.working_class == "Working" and self.color == "black":
            print(f"You are most qualify to join this choir")
        else:
            print(f"You are not qualify to join the choir")


member = Choir(20, "Tenor", 6, "Male", "Single", "Working", "black")
member.member_verification()



class Church:
    def __init__(self, denomination, status, age, color, gender, marit_status):
        self.denomination = denomination
        self.status = status
        self.age = age
        self.color = color
        self.gender = gender
        self.marit_status = marit_status

    def ver_member(self):
        if self.denomination == "catholic" and self.status == "baptised" and self.age >= 20 and self.color == "white" and self.gender == "male" and self.marit_status == "Married":
            print(f"You are welcome to the church ")
        else:
            print(f"You are not qualified to be a member ")


members = Church("catholic", "baptised", 24, "white", "male", "Married")
members.ver_member()



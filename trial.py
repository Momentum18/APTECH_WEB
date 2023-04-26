print("-----------------------SCHOOL MANAGEMENT SYSTEM--------------------------")


def student():

    while True:
        full_name = input("Enter your fullname: ")
        email = input("Enter your email: ")
        phone_num = int(input("Enter your phone number: "))
        course = input("Enter your course: ")
        department = input("Enter your department: ")
        age = int(input("Enter your age: "))
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        print("\nconfirm your information below")

        print(f"\nYour fullname is {full_name}")
        print(f"Your email is {email}")

        try:
            print(f"your phone number is {phone_num}")

        except ValueError:
            print(f"your phone number must be an integer")

        print(f"Your course is {course}")
        print(f"Your department is {department}")

        try:
            print(f"your age is {age}")

        except ValueError:
            print(f"your age must be an integer")

        conf = input("is the information above correct? Y or N: ")

        if conf.lower() == 'y':
            print("proceed to login details")

            user1 = input("Enter your username: ")
            pass1 = input("Enter your password: ")

            if user1 == username and pass1 == password:
                print("Your login was successful")

            else:
                print("Your username or password is incorrect")
                break

        else:
            print("Reregister your details")
            break

student()





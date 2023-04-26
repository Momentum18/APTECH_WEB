num = 1
while num <=10:
    print(num)
    num += 1
    continue


name = input("Enter your name: ")
print(f"Welcome {name}")
print("help")


while True:
    command = input(">>> ")
    help = """
    Help command

    type help - to show this help option
    type start - to start the car
    type stop - to stop the car
    type break - to press the brake
    type horn - to horn
    """
    if command == "help":
        print(help)
    elif command == "start":
        print("Car Started")
    else:
        print("Thank you")







'''
sum = 0
firstnumber = 1
secondnumber = 10
for i in range(firstnumber, secondnumber + 1):
    sum += i

print(sum)
'''
'''
result = 0
for i in range(1,11):
    result += i
print(result)
'''
'''

user = input("Enter your message: ")
print(user[::-1])
'''
'''
def reversed(string):
    return (string[::-1])
print(reversed("This is me"))
'''

'''
age = int(input("Enter your age: "))
age2 = int(input("Enter your age: "))
'''
'''
def greater_or_smaller(x,y):
    if x<y:
        return x
    else:
        return y
'''

def num():
    num1 = int(input("Enter number1: "))
    num2 = int(input("Enter number2: "))
    if num1 < num2:
        print(f"{num1} is less than {num2}")
    else:
        print(f"{num1} is greater than {num2}")


num()



'''
#CALCULATOR PROGRAM
num1 = int(input("enter first number: "))
symbols = input("enter Math symbols: ")
num2 = int(input("enter second number :"))

import time
if symbols == '+':
    time.sleep(3)
    print(f"the answer is {num1 + num2}")

elif symbols == '-':
    time.sleep(3)
    print(f"the answer is {num1 - num2}")

elif symbols == '*':
    time.sleep(3)
    print(f"the answer is {num1 * num2}")

elif symbols == '/':
    time.sleep(3)
    print(f"the answer is {num1 / num2}")

elif symbols == '**':
    time.sleep(3)
    print(f"the answer is {num1 ** num2}")

elif symbols == '//':
    time.sleep(3)
    print(f"the answer is {num1 // num2}")

elif symbols == '%':
    time.sleep(3)
    print(f"the answer is {num1 % num2}")

else:
    time.sleep(3)
    print("Enter the correct Mathematical symbols")
    print("Thank you for your time")
    print("CM Tech")
    '''






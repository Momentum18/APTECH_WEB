print("Hello")
name = "Michael"
number = 9

value = "true"
value = True

print(name)
print("welcome dear "+name)
print("welcome dear",name)
print("welcome dear", name, "your number is", number)
print("welcome dear {0} your number is {1}".format(name,number))
name="APTECH"
print("This is ", name)

#string formatting
print ("This is %s and number is %d" %(name, number))

'''
calculate this expr using python program
1. xab + 2ab => (x*a*b) + (2*a*b)
2. x2y/ab-3ac => ((x**2)*y)/((a*b)-(3*a*c))
3. square root of 81
4. find the result 8 exponential 4
Given x=7, a=1, b=5, c=2, y=1
'''
import math

x=7
a=1
b=5
c=2
y=1

eqtn1=((x*a*b) + (2*a*b))
print(eqtn1)

eqtn2=((x**2)*y)/((a*b)-(3*a*c))
print(eqtn2)

print(math.sqrt(81))
print(math.pow(8,4))

rad_val=math.radians(60)
print(math.cos(rad_val))

print(math.cos(math.radians(45)))

'''
-b+/-sqrt(b2-4ac)/2a => -b+sqrt((b**2)-(4*a*c))/2*a
given values 
a=1, b=5, c=4
'''
import math

a=1
b=5
c=4

#solving for (+)

eqtn3 = (b**2)-(4*a*c)
print(eqtn3)

eqtn4 = -b
print(eqtn4)

eqtn5 = 2*a
print(eqtn5)

print(math.sqrt(9))
eqtn6 = ((eqtn4)+(3)/eqtn5)
print(eqtn6)

#solving for (-)
eqtn7 = ((eqtn4)-(3)/eqtn5)
print(eqtn7)

'''
-b+/-sqrt(b2-4ac)/2a => -b+sqrt((b**2)-(4*a*c))/2*a
given values 
a=1, b=5, c=4
'''
import cmath

a=1
b=5
c=4

#solving for (+)
eqt1=(b**2)-(4*a*c)
print(eqt1)

eqt2=2*a
print(eqt2)

eqt3=(-b+(cmath.sqrt(eqt1)))/eqt2
print(eqt3)

#solving for (-)
eqt4=(-b-(cmath.sqrt(eqt1)))/eqt2
print(eqt4)

'''
Assignment forms in python
Basic Assignment:
Example:
'''
var=90
#sequence assignment
a,b,c=3,6,8
print(b)

#tuple assignment
(x,y)=(5,6)
print(x)
print(y)

#list assignment
[o,i]=['hello','hey']
print(o)

#multiple assignment
x=y=z=10
print(z)

#Augmented assignment
s=6
s+=10
s-=4
print(s)

#Extended sequence unpacking
y,*w,l='hello'
#y goes for 'h', w goes for 'ell' and l goes for 'o'
print(w)

#Relational operators

text='This is Aptech'

#Range
print(text[0: :2])

text='This is Aptech'
print('James'*2)
print('James'+'World')
print('%s'%(text))

#slicing
print(text[8])
print(text[-6])

#Range
print(text[2:6])
print(text[0:])
print(text[:])

#skip
print(text[1: :2])
print(text[1: :3])

#escape Characters
txt='Hey\nThere'
print(txt)

txt2='Hey\tThere'
print(txt2)

txt3='Hey\sThere'
print(txt3)

txt4='Hey\vThere'
print(txt4)

txt5='Hey\rThere'
print(txt5)

txt6='Hey\aThere'
print(txt6)

txt7='Hey\b\bThere'
print(txt7)

#Raw strings
print(r'\n')

#String methods and functions
sample="Friday"
print(len(sample))
print(sample.capitalize())
print(sample.upper())
print(sample.lower())
print(sample.count('i'))
print(sample.isupper())
print(sample.islower())
print(sample.isdigit())
print(sample.isalnum())

user=input("Enter your name:")
print("welcome dear", user)

#Casefold(): converts strings into lowercase
txt="Hello, And Welcome To My World!"
x=txt.casefold()
print(x)

'''
Center(): returns a centered string.
print the word "banana", taking up the space of 20 characters, with "banana" in the middle:
'''
txt="banana"
x=txt.center(20)
print(x)

#or
txt="banana"
x=txt.center(20, "O")
print(x)

#using encode()
txt="My name is Michael"
x=txt.encode()
print(x)

#endswith()
txt="Hello welcome to my world."
x=txt.endswith(".")
print(x)

#check if the strings end with ("my world.")
txt="Hello welcome to my world."
x=txt.endswith("my world.")
print(x)

#expandtabs
txt= "H\te\tl\tl\to"
print(txt)
print(txt.expandtabs())
print(txt.expandtabs(2))
print(txt.expandtabs(4))
print(txt.expandtabs(10))

'''
find()
Where in the text is the word "welcome"?:
'''
txt="Hello, welcome to my world."
x=txt.find("welcome")
print(x)

#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt="Hello, welcome to my world."
x=txt.find("e", 5, 10)
print(x)

'''
format():
# Insert the price inside the placeholder, the price should be in fixed point, two decimal format:
'''
txt="For only {price:.2f} dollars!"
print(txt.format(price=49))

#using different placeholder values:
txt1="My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2="My name is {0}, I'm {1}".format("John", 36)
txt3="My name is {}, I'm {}".format("John", 36)
print(txt1)
print(txt2)
print(txt3)

'''
index()
Where in the text is the word "welcome"?:
'''
txt="Hello, welcome to my world."
x=txt.index("welcome")
print(x)

'''
The index() method finds the first occurrence of the specified value.
The index() method returns -1 if the value is not found
The index() method is almost the same as index() method, the only difference is that index() method raises an exception if the value is not found.
'''

#Where in the text is the first occurrence of the letter "e" when you only search between position 5 and 10?:
txt="Hello, welcome to my world."
x=txt.index("e", 5, 10)
print(x)

'''
ISASCII
check if all the characters in the text are ascii characters:
'''
txt="Company123"
x=txt.isascii()
print(x)

'''
isdecimal()
check if all characters in the unicode object are decimals:
'''
txt="\u0033" #unicode for 3
x=txt.isdecimal()
print(x)

a="\u0030" #unicode for 0
b="\u0047" #unicode for G
print(a.isdecimal())
print(b.isdecimal())

#List Object:
fruits=['Mango', 'Apple', 'Orange', 'Pawpaw']
Cars=['Mercedes','Toyota']

print(fruits [0] [3])
print(fruits [0:-1])
print(fruits [ : :2])
print(fruits+Cars)

#list methods
print(max(fruits))

#minimum
print(min(fruits))

fruits.extend(Cars)
print(fruits)

#pop: holds the value
print(fruits.pop(4))

#Reverse: reverses the order of the element
fruits.reverse()
print(fruits)

#Insert: Allows you to add an element in a list. need to specify
Cars.insert(1,'BMW')
print(Cars)

#append: does same with insert but only add at the end of the list
Cars.append('Honda')
print(Cars)

#Remove: does same with pop just that remove takes the name and pop takes index number
Cars.remove('Honda')
print(Cars)

#sort: sorts the elements
Cars.sort()
print(Cars)

#index:gives the index position
print(fruits.index('Mango'))

#clear: is to clear the list
Cars.clear()
print(Cars)

#del: will wipe all
del(Cars)


#tuple:for every element of tuple, you end wit a comma
tuple_val=('a', 1, 45, 'ab',)
print(tuple_val)

#python dictionary element:
student_dict={'su@gmail.com':'subomi', 'adex@yahoo.com': 'Adeola'}
student_dict['ay@yahoo.com']='Ayomide'
student_dict['alex@hotmail.co.uk']='Alexandar'

print(student_dict)

num=int(input('Enter a digit:'))
if num%2==0:
	print(num,'is even')
else:
	print(num,'is odd')

'''
>=70 - A
>=60 - B
>=50 - C
>=40 - D
>=30 - E
<30 - F
'''

score=int(input('Enter your score:'))
if score>100:
	print('Invalid Entry')
elif score>=70:
	print('Grade is A')
elif score>=60:
	print('Grade is B')
elif score>=50:
	print('Grade is C')
elif score>=40:
	print('Grade is D')
elif score>=30:
	print('Grade is E')
elif score<30 and score>0:
	print('Grade is F')


sideA = int(input('Enter your sideA: '))
sideB = int(input('Enter your sideB: '))
sideC = int(input('Enter your sideC: '))
if sideA==sideB==sideC:
	print('Triangle is equilateral')

elif sideA!=sideB and sideA!=sideC and sideB!=sideC:
	print('Triangle is scalene')
else:
	print('Triangle is isosceles')

for i in range(1, 4, 2):
	print('Hello world ', i)

for i in range(5):
	if i%2!=0:
		print('Hello world ',i)


namelist=[]
for i in range(3):
	name=input('Enter your name: ')
	namelist.append(name)
print(namelist)


side1=int(input("Enter side1: "))
side2=int(input("Enter side2: "))
side3=int(input("Enter side3: "))

if side1==side2==side3:
	print("The triangle is equilateral")
elif side1!=side2 and side1!=side3 and side2!=side3:
	print("The triangle is Scalene")
else:
	print("The triangle is issosceles")
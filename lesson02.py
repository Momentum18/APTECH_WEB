#python dictionary element:
student_dict={'su@gmail.com':'subomi', 'adex@yahoo.com': 'Adeola'}
student_dict['ay@yahoo.com']='Ayomide'
student_dict['alex@hotmail.co.uk']='Alexandar'

word={'Noun': 'Name of person, animal, place or thing', 'Verb': 'An action word'}

print(student_dict.get('su@gmail.com'))
print(student_dict.items())
print(student_dict.keys())
print(student_dict.values())

#update: is used to merge two dictionaries together
student_dict.update(word)
print(student_dict)
student_dict.pop('Verb')
print(student_dict)

#popitem automatically remove the last item even without specifying
student_dict.popitem()
print(student_dict)

val=student_dict.get('ay@yahoo.com')
print(val[2])

student_dupl=student_dict.copy()
print(student_dupl)

#tuple:for every element of tuple, you end wit a comma
tuple_val=('a', 1, 45, 'ab',)
print(tuple_val)

new_list=list(tuple_val)
print(new_list)

set_val1=set(('a','b','c'))
set_val2=set(('a','d','c'))
print(set_val1.intersection(set_val2))
print(set_val1.union(set_val2))
print(set_val1.difference(set_val2))
#union will be a,b,c,d, while defferences will be b,d

letters={'a','b','c','d'}
print(dict.fromkeys(letters,1))


'''name=input('Enter your name:')
if name.isupper():
	print(name, 'is in capital letter')
else:
	print(name, 'is not in capital letter')
'''

email=input('Enter your name:')
age=input('Enter your age:')
if email.upper():
    if 'm' in email:
        print(email,'starts with capital letter')
    else:
        print(email,'invalid entry')
else:
    print(email,'invalid entry')


num=int(input('Enter a digit:'))
if num%2==0:
	print(num,'is even')
else:
	print(num,'is odd')

score = int(input('Enter your score:'))
if score >= 70 and score <= 100:
    print('Grade is A')
elif score >= 60:
    print('Grade is B')
elif score >= 50:
    print('Grade is C')
elif score >= 40:
    print('Grade is D')
elif score >= 30:
    print('Grade is E')
elif score < 30:
    print('Grade is F')
else:
    print('Invalid Entry')


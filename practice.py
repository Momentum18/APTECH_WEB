'''
i = 1
while i < 6:
    print(i)
    i += 1
'''

'''
i = 1
while i < 6:
    print(i)
    if i == 4:
        break
    i += 1
'''
i = 1
while i < 6:
    i += 1
    if i == 5:
        continue
    print(i)

name = ["Michael", "Chioma", "Emmanuel", "Richard"]
last_name = ["Ukut", "Isaiah", "Ukut", "Isaiah"]
for x in name:
    for y in last_name:
        print(x, y)


def my_function(fname, lname):
    print(fname, "", lname)


my_function("Michael", "Ukut")

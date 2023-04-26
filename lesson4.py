thislist = ["banana","cherry","orange"]
print(thislist)

thislist = list(("banana","cherry","orange"))
print(thislist)

print(thislist[1])

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
print(thislist[2:5])

thislist[3] = "pawpaw"
print(thislist)

thislist = ["apple","banana","cherry","orange","kiwi","melon","mango"]
tropical = ["tree","grass"]
thislist.extend(tropical)
print(thislist)

thistuple = ("vehicle","car")
thislist.extend(thistuple)
print(thislist)

user = ["Hello, world"]
for x in user:
    print(user)

thislist.sort()
print(thislist)

thislist.sort(reverse=True)
print(thislist)

'''
thislist.sort(key=str.lower,reverse=True)
this will sort the list with capital letters and arrange it alphabetically not minding 
the capital letter before sorting them in order
'''
thislist = ["orange","kiwi","zango","banana"]
thislist.sort(key=str.lower,reverse=True)
print(thislist)

# list methods and their their example Assignment:
#Append(): Adds an elememt at the end of the list

list = ["Mango", "Cherry", "orange", "apple"]
list.append("pineapple")
print(list)

#count: returns the number of times the value("x") appears in the list:
print('count is',list.count("orange"))

#index(): returns the index of the first element with the special value
x = list.index("Cherry")
print(x)

#extend(): Add the element of a list (or any iterable), to the end of the current list
list = ["Mango", "Cherry", "orange", "apple"]
cars = ["volvo", "toyota", "corolla"]
list.extend(cars)
print(list)

#insert(): Adds an element at the specified position:
list.insert(3,"pawpaw")
print(list)

#pop(): Removes the element at the specified position:
list.pop(3)
print(list)

#copy(): returns a copy of the list:
x = list.copy()
print(list)

#sort: sorts the list:
list.sort(key=str.lower)
print(list)

list.sort(key=str.lower,reverse=True)
print(list)

#remove(): removes the item with the specified value:
list.remove("corolla")
print(list)

#clear(): removes all the elements from the list:
list.clear()
print(list)


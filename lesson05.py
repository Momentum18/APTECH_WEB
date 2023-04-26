# tuple: a comma is used for a list after the item has been inserted e.g ("banana",)
# converting tuple to list, then adding an item and also coverting the newly list into tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

g = tuple(("a", "b", "c"))
f = ("a", "b", "c")

# unpacking tuples
x = ("apple", "banana", "cherry")
a, b, c = x
print(a)
print(b)
print(c)

# cherry,beans,yam,sweet potato and 3

mylist = ["apple", "banana", "cherry", ["rice", "beans",["yam", "cocoyam", ["irish potato", "sweet potato"]]], [1, 2, 3]]
print(mylist[2],mylist[3][1],mylist[3][2][0],mylist[3][2][2][1],mylist[4][2])

x = -4
y = abs(x)
print(x)
print(y)
print(abs(-4))

username = "Alan"
print(f"Hello {username}")



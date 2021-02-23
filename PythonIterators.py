import os
os.system("cls")

# Python Iterators
mytuple = ("apple", "banana", "cherry", "orange", "mango", "carrot")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print()

mystr = "Benjamin"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print()

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry", "orange", "mango", "carrot")

for x in mytuple:
    print(x)
print()


mytuple1 =  "carrot"

for x1 in mytuple1:
    print(x1)
print()
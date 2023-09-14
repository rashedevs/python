# print("Hello quant fintech, see yeah")
# ok
"""ok there are jkkkkkkkkkkkkkkkkkkkkkkkkkk"""

# b = """ok there are jkkkkkkkkkkkkkkkkkkkkkkkkkk"""
# print(b)

# import random
# print(random.randrange(1, 3))

# c = "okcvbd"
# print(len(c))
# print(c[2])
# print("a" in c)

# for x in "banana":
#     print(x)

# txt = "The best things in life are free!"
# if "free" in txt:
#     print("yes, free is present")

# txt = "The best things in life are free!"
# if "lifoo" not in txt:
#     print("not in txt")

# removing white spaces from start/end using strip()
# a = " Hello, World!   "
# print(a.strip())

# The replace() method replaces a string with another string.
# a = "Hello, World!"
# print(a.replace("Hello", "Hi"))

# The split() method splits the string into substrings if it finds instances of the separator
# a = "Hello, World!"
# print(a.split(","))  # returns ['Hello', ' World!']

# we can combine strings and numbers by using the format() method!
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item no {} for {} dollars."
# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))

# Chapter: List

# thislist = ["apple", "banana", "apple", "cherry"]
# print(len(thislist))
# print(type(thislist))

# list (constructor):
# newList = list(("apple", "banana", "apple", "cherry", "banana", "cherry"))
# print(newList)
# print(
#     newList[2:5]
# )
# The search will start at index 2 (included) and end at index 5 (not included).
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(newList[-4:-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)

# replace one value with multiple
# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)

# insert new item using index
# thislist = ["apple", "banana", "cherry"]
# thislist.insert(2, "watermelon")

# To add an item to the end of the list, use the append() method:
# thislist.append("orange")
# print(thislist)

# To append elements from another list to the current list, use the extend() method.
# thislist = ["apple", "banana", "cherry"]
# tropical = ["mango", "pineapple", "papaya"]
# thistuple = ("kiwi", "orange")  # tuple
# we can add any iterable object also (tuples, sets, dictionaries etc)
# tropical.extend(thistuple)
# print(tropical)

# The remove() method removes the specified item.
# thislist = ["apple", "banana", "cherry", "banana"]
# thislist.remove("banana")
# remove() will remove the first element if there is same more
# print(thislist)

# The pop() method removes the specified index.
# thislist = ["apple", "banana", "cherry"]
# thislist.pop(1)
# print(thislist)

# The del keyword also removes the specified index or whole list:
# thislist = ["apple", "banana", "cherry"]
# del thislist[0]
# del thislist
# print(thislist)

# The clear() method empties the list.
# thislist = ["apple", "banana", "cherry"]
# thislist.clear()  # o/p ===> []
# print(thislist)

# loop in lists
# thislist = ["apple", "banana", "cherry"]
# for x in thislist:
#     print(x)

# Use the range() and len() functions to create a suitable iterable.
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))
# for iterable in range(len(thislist)):
#     print(thislist[iterable])

# Using while loop
# thislist = ["apple", "banana", "cherry"]
# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1

# Looping Using List Comprehension: can find the output using shortest code
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

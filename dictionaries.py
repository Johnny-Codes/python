# Python Dictionaries

# A Dictionary is a collection which is ordered (as of Python version 3.7),
# changeable and indexed. In Python dictionaries are written with curly
# brackets, and they have keys and values.

# Create and print an empty dictionary:
empty_dict = {}
print(empty_dict)

# Create and print a dictionary:
new_dict = {
    "name": "Johnny",
    "age": 30,
    "state": "TX"
}
print(new_dict)

# Accessing Items:

# You can access the items of a dictionary by referring to its key name, inside
# square brackets:
x = new_dict["state"]
print(x)

# There is also a method called get() that will give you the same result:
y = new_dict.get("state")
print(y)

# The difference between new_dict["model"] and new_dict.get("model") is that
# the first one returns the value of the item with the specified key, while
# the second one returns None if the key does not exist. You can also specify
# a default value to be returned in the case the key does not exist:
z = new_dict.get("age", 0)
print(z)

# Change Values:
new_dict["age"] = 21
print(new_dict)

new_dict.update({"age": 36})
print(new_dict)

# Loop Through a Dictionary:
for key in new_dict:
    print(key)

for value in new_dict.values():
    print(value)

for key, value in new_dict.items():
    print(key, value)

# Check if Key Exists:
if "age" in new_dict:
    print("Yes, 'age' is one of the keys in the new_dict dictionary")

# Adding Items:
new_dict["city"] = "Houston"
print(new_dict)

# Removing Items:
new_dict.pop("city")
print(new_dict)

# The popitem() method removes the last inserted item
new_dict.popitem()
print(new_dict)

# The del keyword removes the item with the specified key name:
del new_dict["age"]
print(new_dict)

# The del keyword can also delete the dictionary completely:
# del new_dict
# print(new_dict)

# The clear() method empties the dictionary:
new_dict.clear()
print(new_dict)

# Copy a Dictionary:
new_dict2 = new_dict.copy()
print(new_dict2)

# Nested Dictionaries:
nested_dict = {
    "child 1": {
        "name": "Jake",
        "year": 2004
    },
    "child 2": {
        "name": "Jason",
        "year": 2007
    },
    "child 3": {
        "name": "Janet",
        "year": 2011
    }
}
print(nested_dict)

# Create a Dictionary that Contains List Values:
new_dict3 = {
    "parent": "Johnny",
    "age": 36,
    "state": "TX",
    "children": ["Jake", "Jason", "Janet"]
}
print(new_dict3)

# Create a Dictionary that Contains Dictionary Values:
new_dict4 = {
    "parent": "Johnny",
    "age": 36,
    "state": "TX",
    "children": nested_dict,
}
print(new_dict4)
print(new_dict4["children"]["child 1"]["name"])

# Advanced Dictionary Methods:
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary

employees = [
    ("John", "Male"),
    ("Jane", "Female"),
    ("Joe", "Male"),
    ("Jill", "Female")
]

employees_dict = dict(employees)
print(employees_dict)

# With dictionary comprehension
employees_dict = {key: value for key, value in employees}
print(employees_dict)

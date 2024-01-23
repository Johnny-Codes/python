# Python Dictionaries

# References:
# https://docs.python.org/3/c-api/dict.html
# https://docs.python.org/3/tutorial/datastructures.html

# A Dictionary is a collection which is ordered (as of Python version 3.7),
# changeable and indexed. In Python dictionaries are written with curly
# brackets, and they have keys and values.

# Method		Description
# clear()		Removes all the elements from the dictionary
# copy()		Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()			Returns the value of the specified key
# items()		Returns a list containing a tuple for each key value pair
# keys()		Returns a list containing the dictionary's keys
# pop()			Removes the element with the specified key
# popitem()		Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()		Updates the dictionary with the specified key-value pairs
# values()		Returns a list of all the values in the dictionary
# del <dict>	Deletes a dictionary from memory

# Create and print an empty dictionary

empty_dict = {}
print("empty_dict:", empty_dict)

# Add item to dictionary

empty_dict["not"] = "empty now"
print("empty_dict:", empty_dict)
empty_dict[2] = "second key and value"
print("empty_dict:", empty_dict)
empty_dict[3] = 3
print("empty_dict:", empty_dict)

# Clear a dictionary

empty_dict.clear()
print("cleared empty_dict:", empty_dict)

# Delete a dictionary entirely

del empty_dict
print("deleted empty_dict returns error", empty_dict)

# Create a dictionary with initial values:
new_dict = {"name": "Johnny", "age": 30, "state": "TX"}

# Accessing Items:

# You can access the items of a dictionary by referring to its key name, inside
# square brackets:

new_dict["state"]
x = new_dict["state"]
print("new_dict key: state, value:", x)

# There is also a method called get() that will give you the same result:
y = new_dict.get("state")
print("y:", y)

# If you use the .get() method and you want to return a value if the key
# does not exist, you can pass a default value like so:

new_dict.get("age", 0)

new_dict.get("city", "Houston")

# What is the difference between new_dict["state"] and new_dict.get("state")?
# When accessing the dictionary with new_dict["state"] syntax, if the key does
# not exist, python will throw a Key Error. The .get() method simply will not
# return anything. Both methods have their place in certain circumstances.

# Change Values:

new_dict["age"] = 21
print("new_dict:", new_dict)

new_dict.update({"age": 36})
print("new_dict:", new_dict)

# Adding Items:

new_dict["city"] = "Houston"
print("new_dict:", new_dict)

# Removing Items:

new_dict.pop("city")
print("new_dict", new_dict)

# The popitem() method removes the last inserted item

new_dict.popitem()
print("new_dict", new_dict)

# The del keyword removes the item with the specified key name:
# *As mentioned previously, you can delete an entire dictionary as well

del new_dict["age"]
print("new_dict deleted:", new_dict)

# Copy a Dictionary:

new_dict2 = new_dict.copy()
print(new_dict2)

# Nested Dictionaries:

users = {
    1: {"name": "Jake", "birth_year": 2004},
    2: {"name": "Jason", "birth_year": 2007},
    3: {"name": "Janet", "birth_year": 2011},
}
print(users)

# Accessing Nested Dictionaries:

print(users[1]["name"])

# Create a Dictionary that Contains List Values:

new_dict = {
    "parent": "Johnny",
    "age": 36,
    "state": "TX",
    "children": ["Jake", "Jason", "Janet"],
}
print("new_dict:", new_dict)

# Create a Dictionary that Contains Dictionary Values:

new_dict = {
    "parent": "Johnny",
    "age": 36,
    "state": "TX",
    "children": users,
}
print("new_dict:", new_dict)
print(new_dict["children"][1]["name"])

# Advanced Dictionary Methods:
# Python has a set of built-in methods that you can use on dictionaries.

# using fromkeys()

list_of_keys = ["name", "age", "state"]
new_dict = dict.fromkeys(list_of_keys)
print("new_dict fromkeys():", new_dict)

new_dict = {"name": "Johnny", "age": 36, "state": "TX"}

new_dict.setdefault("age", 30)
print("age added:", new_dict)

new_dict.setdefault("gender", "male")
print("gender added:", new_dict)

print(new_dict)

# Loop Through a Dictionary:

for key in new_dict:
    print("key:", key)

for value in new_dict.values():
    print("value:", value)

for key, value in new_dict.items():
    print(f"key: {key} - value: {value}")

# Check if Key Exists:

if "age" in new_dict:
    print(f"age = {age}")

# Create a dictionary from a list of tuples

employees = [("John", "Male"), ("Jane", "Female"), ("Joe", "Male"), ("Jill", "Female")]

employees_dict = dict(employees)
print("employee_dict:", employees_dict)

# With dictionary comprehension

employees_dict = {key: value for key, value in employees}
print(employees_dict)

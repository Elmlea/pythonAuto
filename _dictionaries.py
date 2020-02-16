# DICTIONARY BASICS

myCat = {'size': 'sleek', 'colour': 'bronze', 'disposition': 'loud'}
# Syntax is as above.  {'key': 'value', 'key': 'value'}

# Access the value using the name of the key rather than an index
print('My cat has ' + myCat['colour'] + ' fur.')

# Dictionaries are unordered; if they have the same
# key value pairs they are identical, even in the wrong order

# Adding to a dictionary is done like this:
myCat['name'] = 'Ripley'

# this will add a key called name and a value called Ripley
# Variables can be used as well, as long as a string or integer

# DICTIONARY METHODS
# Keys, values and items methods return list like values,
# and can be used to iterate a for loop
spam = {'colour': 'red', 'age': '42'}

for v in spam.values():
    print(v)
for k in spam.keys():
    print(k)

# items() returns a tuple of each key and its value
for i in spam.items():
    print(i)

# To get things as a list, pass it to the list() function
print(list(spam.keys()))
# This will return a list of the key entries

# MULTIPLE ASSIGNMENT
# We can use multiple assignment in a dictionary

for k, v in spam.items():
    print('Key: ' + k + ' Value: ' + v)

# We can also check if things exist in a dictionary:
print('name' in spam.keys())
print('colour' in spam.keys())

# GET METHOD
# Used to check if a key exists in a dictionary before accessing
# the associated value.  It's also passed a fallback number.
picnicItems = {'apples': '5', 'cups': '2'}
print('I am bringing ' + str(picnicItems.get('cups', 0)) + ' cups.')
print('I am bringing ' + str(picnicItems.get('eggs', 0)) + ' eggs.')

# SETDEFAULT METHOD
# Used to set an automatic default for any keys
spam.setdefault('height': '172cm')
# This sets an initial default; it will not overwrite

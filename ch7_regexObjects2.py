print("Regex Objects 2 - Grouping\n")

print("We import the re module first, using 'import re'\n")

import re

print("We make groups in our regular expressions by using parenthesis.")
print("We use parenthesis like:")
print(r"(\d\d\d)-(\d\d\d-\d\d\d\d)")
print("The first group will be group 1, and so on.")
print("\nPassing 0 to the group method, or nothing, will return all matched text.")

print(r">>> phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)'")
print(">>> mo = phoneNumRegex.search('My number is 123-456-2342')")

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search("My number is 123-456-2342")
# NOTE: Think of the Syntax
# var = re.compile(r'string'), so the var is now a Regex
# var.search(arg); does arg appear as the regex?
# returns the regex value.


print("\nWe then pass the group method on mo to separate it as")
print("per the grouping specified in the re.compile statement.")
print()
print("mo.group(1) should return the first grouping, which is the first 3 digits")

print(mo.group(1))

print("\nWe'll now print mo.group(0), mo.group(1), and mo.group(2)")
print(mo.group(0))
print(mo.group(1))
print(mo.group(2))

print("\nFinally, calling the groups (note plural!) method pulls them out as a tuple.")
print("We call mo.groups(), and print it below:")
print(mo.groups())
print("\nNow, we can use this for multiple assignment.")
print("For example:")
print(">>> areaCode, mainNumber = mo.groups()")

areaCode, mainNumber = mo.groups()

print("\nNow we can print them individually from the tuple:")
print("printing areaCode then mainNumber:")
print(areaCode)
print(mainNumber)

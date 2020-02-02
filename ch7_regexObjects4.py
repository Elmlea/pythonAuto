import re

print("Another use of | is to match multiple patterns.\n")

print("""If you want to match Batman, Batmobile, Batcopter, Batboat,
you could use the regular expression:
>>> batRegex = re.compile(r"Bat(man|mobile|copter|boat)"))""")
batRegex = re.compile(r"Bat(man|mobile|copter|boat)")
# NOTE: The syntax:
# NOTE: Pass the string to search, and call the method search
# NOTE: on the regular expression
# NOTE: eg:

print("\nCall SEARCH on the regex, passing the string to search as")
print("an argument; eg:")
print(">>> mo = batRegex.search(r'I like the Batmobile best')")
print("mo.group() should return 'Batmobile'")
print()
mo = batRegex.search(r'I like the Batmobile best.')
print(mo.group())

print("\nAsking for group(1) will return 'mobile' as the first group")
print("because it's the first element from the options in parenthesis")
print(">>> print(mo.group(1))")

print(mo.group(1))

print("""So the method group() returns the entire matching string;
which is 'Bat' followed by any of the options in parenthesis.

The method group(1) returns the matching element from the first group,
which is the part in parenthesis.""")

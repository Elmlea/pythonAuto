import re

print("Regex Objects 5 - Optional Matching\n")
print("""Use the '?' character when we want to optionally match an
expression.  We still separate the regex by groups; the '?'
follows the group that is optional.""")
print()
print("""For example, we can define a regular expression:
batRegex = re.compile(r'Bat(wo)?man')""")

batRegex = re.compile(r"Bat(wo)?man")

print("We define a match object:")
print("mo1 = batRegex.search('The Adventures of Batman!')\n")

mo1 = batRegex.search("The Adventures of Batman!")

print("""Now we can call the group method to see what matched:
print(mo1.group())""")

print(mo1.group())

print("""print(mo1.group(1)) returns NONE because the optional
group wasn't filled in our 'Batman' example.""")

print(mo1.group(1))

print("""
If we reset things to:
mo2 = batRegex.search('The Adventures of Batwoman!')
... then mo2.group() should return 'Batwoman...'
""")

mo2 = batRegex.search("The Adventures of Batwoman!")
print(mo2.group())

print("""
... and mo2.group(1) should return 'wo'...
""")

print(mo2.group(1))

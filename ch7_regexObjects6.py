print("Regex Objects 6 - Matching Zero or More\n")

print("""Use an asterisk to mark a group (the preceding group) as
'match zero or more;' it can occur multiple times.  For example:

>>> batRegex = re.compile(r'Bat(wo)*man')

... means the 'wo' can be repeated as many times as we like and it'll
still be returned as a match.

If we set:

mo1 = batRegex.search('Batman')
mo2 = batRegex.search('Batwoman')
mo3 = batRegex.search('Batwowowowoman')

then call moX.group() on each, we'll get
'Batman'
'Batwoman'
'Batwowowowoman'
.. as output:
""")

import re

batRegex = re.compile(r"Bat(wo)*man")
mo1 = batRegex.search('Batman')
mo2 = batRegex.search('Batwoman')
mo3 = batRegex.search('Batwowowowoman')

print(mo1.group())
print(mo2.group())
print(mo3.group())

print("""
... and calling moX.group(1) should return:
None (no match!)
wo (1 x wo)
wo - only one, as it's the SAME group repeated many times!
""")

print(mo1.group(1))
print(mo2.group(1))
print(mo3.group(1))

print("""
As an alternative, we can use the + sign to show that a group must
appear at least once.  In the examples above, the 'Batman' case will
not match as there's no 'wo.'

* ---> optional group, zero or more
+ ---> non-optional group; one or more
""")

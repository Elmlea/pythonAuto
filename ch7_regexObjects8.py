print("Regex Objects 8 - the findall method")
print("""
Calling findall instead of search will return a list of strings, where
each element is a match.

For example:
phoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d\d')
mo1 = phoneNumRegex.search('My number is 01361 127828 and work
is 01361 7652345.')

This match object will only match the first string, so printing
mo1.group() will just return the first number:
""")

import re
phoneNumRegex = re.compile(r'\d\d\d\d\d-\d\d\d\d\d\d')
mo1 = phoneNumRegex.search("My number is 01361-127828, work is 01361-876543.")

print(mo1.group())

print("""
If we use findall instead, it returns a list of strings, where each string is
a match.  This only happens if there are no groups defined in the regex.

mo1 = phoneNumRegex.findall("My number is 01361-127828, work is 01361-876543.")

This match object contains a list of strings which we can show by:
print(mo1)

There's no need to call the groups method; the list has no groups.
""")

mo1 = phoneNumRegex.findall("My number is 01361-127828, work is 01361-876543.")
print(mo1)

print("""
However, if the regex has groups, then the findall method returns a list of tuples,
the contents of which are the contents of each group that was returned.

For example, if we re-write the phoneNumRegex:

phoneNumRegex = re.compile(r"(\d\d\d\d\d)-(\d\d\d\d\d\d)")
mo1 = phoneNumRegex.findall("My number is 01363-176876, my work is 01671-767234,
and my fax is 01989-789872")

... then call print(mo1), we should get a list of tuples, where each tuple
contains the area code and main number.
""")

phoneNumRegex = re.compile(r"(\d\d\d\d\d)-(\d\d\d\d\d\d)")
mo1 = phoneNumRegex.findall("My number is 01363-176876, my work is 01671-767234, and my fax is 01989-789872")

print(mo1)

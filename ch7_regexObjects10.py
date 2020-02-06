print("Regex Objects 10 - Wildcards\n")
print("""The dot . charater is a wildcard, and matches everything
except a newline.

For example:
atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')

Printing mo1 will return a list of all the matches.  You can't call the
group method on it because there are no groups
""")

import re

atRegex = re.compile(r'.at')
mo1 = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo1)

print("""
Matching absolutely anything can be done with .*

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = nameRegex.search('First Name: Mark Last Name: Wharry')

Group 1 will return Mark, group 2 Wharry.  Group() will put both if __name__ == '__main__':
a list.

This does greedy matching, so will match as much as it can, not just the first
element.
""")

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo1 = nameRegex.search("First Name: Mark Last Name: Wharry")
print(mo1)
print(mo1.group(1))
print(mo1.group(2))
print(mo1.groups())

print("""
To even match a newline, we use the DOTALL argument:
noNewlineRegex = re.compile('.*')
mo2 = noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')


Printing mo2.group() will only print the result up to the first newline:
""")

noNewlineRegex = re.compile(".*")
mo2 = noNewlineRegex.search("Serve the public trust.\nProtect the innocent.")
print(mo2.group())

print("""
Using the dotall arguement:

newLineRegex = re.compile('.*', re.DOTALL)
mo3 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')

Printing mo3.group() will show all the matched string:
""")

newLineRegex = re.compile('.*', re.DOTALL)
mo3 = newLineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.')
print(mo3.group())

print("""
There are other second arguements, like I to ignore case:
re.compile(r'Fish', re.I)
""")

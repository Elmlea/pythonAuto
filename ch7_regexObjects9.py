print("Regex Objects 9 - Location\n")
print("""The caret and dollar symbols can be used to declare that a
match within a regex must occur at the start or the end of the searched text.

For example:
beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')

Printing mo1 will show its details, including the span across which it found
a match.

Calling the group() method on it will show "Hello" as a match.

Below, we'll run:
print(mo1)
print(mo1.group())
""")

import re

beginsWithHello = re.compile(r'^Hello')
mo1 = beginsWithHello.search('Hello world!')
print(mo1)
print(mo1.group())

print("""
We can also set up a regex that has to end with a number, by using \d$

endWithNumber = re.compile(r'\d$')
mo2 = endsWithNumber.search('Your number is 42')

Printing mo2 will show the details of the match object, while printing
mo2.group() will show the trailing number.
""")

endsWithNumber = re.compile(r'\d$')
mo2 = endsWithNumber.search('Your number is 42')
print(mo2)
print(mo2.group())

print("""
We can combine these, and add our previous terms.  To serch for a string
that starts and ends with a number ***(ie is only numbers)***, we'd use:

wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1234456777')
""")

wholeStringIsNum = re.compile(r'^\d+$')
mo3 = wholeStringIsNum.search('1234456777')
print(mo3)
print(mo3.group())

print("""
To remember the order, remember carrots cost dollars!""")

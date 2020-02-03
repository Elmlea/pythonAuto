print("Character Classes")
print("""
Think of character classes as shorthand.  \d is the same as
(0|1|2|3|4|5|6|7|8|9), and [0-5] is better than (0|1|2|3|4|5).

The chapter examples is:
xmasRegex = re.compile(r'\d+\s\w+')

This will match text that has one of more digits (\d+), then a
whitespace character (\s), then one or more "word" characters
(\w+), which includes letters, digits, and underscores.

Running:

xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7
swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')

... will return a list with each element like '12 drummers.'
""")

import re
xmasRegex = re.compile(r'\d+\s\w+')
mo1 = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo1)

print("""
You can define your own character classes with square brackets inside
the regex definition.  For example, to find vowels:

vowelRegex = re.compile(f'[aeiouAEIOU]')

... when used with findall, this will return all the vowels in order
in a list.  Called like:
vowelRegex.findall('Robocop eats baby food.  BABY FOOD!')
""")

vowelRegex = re.compile(f'[aeiouAEIOU]')
print(vowelRegex.findall('Robocop eats baby food.  BABY FOOD!'))

print("""
You can define ranges too; [a-zA-Z0-9] is all upper and lower case letters,
plus all numbers.

Lastly, you can put a ^ inside the openeing square bracket to define a negative
class; which includes all the characters NOT in the brackets.

Important point; there's no need to use escape characters within the square
brackets.
""")

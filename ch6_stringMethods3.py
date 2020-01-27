print("Split and Join string methods have syntax worth remembering.")
print("""Call the method on the string you want to use to split or join the strings.
You also pass the argument of the strings you want to join, or string you want to split.

For example, ','.join(['fish', 'guppy'])

.. will use the ',' character to join the strings in the list.  You ***must*** pass a list
of strings to the join method.

It should output fish,guppy""")

print(','.join(['fish','guppy']))

print("""Key lesson: call it on a string value, and pass it a list value.  It then
joins the strings in the list value using the string value it's called on as a joiner.""")

print("""
The split string method is similar but opposite.  Call it on a string and pass it a string.
It takes the string passed as the delimiter to split the string, and returns a list.
If you don't pass it a delimiter, it uses white space.

For example, 'I am learning Python'.split() should return a list with each word in it:""")

print('I am learning Python'.split())

print("""
So JOIN is called on a string value and passed a list, and returns a string where each
item in the list is joined by the string value it was called on.

SPLIT is called on a string and passed a string as a delimiter, and returns a list containing items
from the first string, split whenever the string passed occurs.""")

print("\nSplit should work on a multi-line string.  We'll define spam as:")
spam = """Hello there,
I am a multi line string.
I hope this works."""
print(spam)
print("\nNow, we call spam.split('\\n')\nNote we have to put the newline escape char in quotes!")
print(spam.split('\n'))
print("\nThis returns a list that we can now manipulate!")

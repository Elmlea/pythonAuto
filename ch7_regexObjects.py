import re

print("""Passing a string value representing your regular expression
to re.compile() returns a regex object.  This is like making a template.""")

# NOTE: We want the phone number pattern from the previous exercise.
# \d represents a digit character.
# \d\d\d-\d\d\d-\d\d\d\d is the format for 123-456-1234.

print("\n>>> phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d)")
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
print("""
This creates a Regex object.  r makes this a raw string, so
escape characters \ are ignored.  Remember, we've made a template
matching that orientation of digits, and called it phoneNumRegex
""")

message = "Hello, my number is 415-555-9999"

print("We store a message: ''" + message + "'")
print("\nNow we run the search method on our regex object.")
print("By running >>> mo = phoneNumRegex.search(message)")

mo = phoneNumRegex.search(message)

print("\nThe result is stored in mo, and we call the group method to display.")
print("Syntax is mo.group()")
print("Phone number found: " + mo.group())

"""Review of Regular Expression Matching
While there are several steps to using regular expressions in Python,
each step is fairly simple.

1. Import the regex module with import re.
2. Create a Regex object with the re.compile() function. (Remember to use a raw string.)
3. Pass the string you want to search into the Regex object’s search() method. This returns a Match object.
4. Call the Match object’s group() method to return a string of the actual matched text."""

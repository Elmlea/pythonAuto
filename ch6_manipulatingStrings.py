# Ways with strings

# use double quotes to allow you to use non-escaped single quotes
print("That is Alice's cat")

# \ is the start of all escape characters.  \n is newline
print("Hello!\nHow are you?\nI\'m doing fine!")

# if you need to print \, mark the string as raw
print(r"The escape character begins with \!")

# triple quotes allow you to use tabs, newlines and quotes in a string over
# multiple lines
print("""Hello everyone,

It's very nice to see you all here.

Sincerely, Bob""") # note Atom formatting colours

"""Multi-line strings, set up with triple quotes, are a perfectly
valid way to put comments in that explain something that needs more than
one line. Hurrah!"""

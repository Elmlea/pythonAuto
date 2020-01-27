print("How are you?")
feeling = input()

if feeling.lower() == 'great':
    print("I feel great too!")
else:
    print("Hope the rest of the day is good.")

print("There are lots of string methods.")
print("""islower and isupper return boolean values based on whether the whole
string is upper case or lower case""")

# islower on variables
print("\nFor example, setting spam = 'Hello World!'")
spam = "Hello world!"
print("... then calling islower on it with the syntax spam.islower()")
print(spam.islower())
print("... returns false because it has a capital H.\n")

# islower on strings
print("""We don't need to call it on variables.  I'll call it now on
abc123, using the syntax print('abc123'.islower())""")
print('abc123'.islower())
print("... there it's true, because the only letters are lower case.\n")

# chains of method calls
print("""We can chain these method calls, like islower() and isupper() together.
Remember as well that upper() returns the string in upper case, and lower()
returns it in lower case.""")
print("\nThese return Boolean values.  For example:")
print("\nCalling 'hello'.upper().lower().isupper()....")
print('hello'.upper().lower().isupper())
print("... returns False.")
print("""This is because we first call upper() to make it all upper case,
then call lower() to make it all lower case, then call isupper() to check
if it's all upper case or not; and it's not!""")

# other string methods
print("\nThere are other string methods, such as:")
print("isalpha()   - checks if it's alpabetic characters only")
print("isalnum()   - checks if it's alphanumeric")
print("isdecimal() - checks if it's just numbers")
print("isspace()   - checks if it's just spaces")
print("istitle()   - checks if it's only Words With Initial Capitals")

print("There are more string methods:")
print("endswith() and startswith() are good alternatives to ==")
print("For example, we set spam = 'Hello World!'")

spam = 'Hello World!'

print("Remember title case?  We can call spam.istitle() to check...")
print(spam.istitle())
print("... that returns True.\n")

print("If we now call startswith('Hello'), using the syntax spam.startswith('Hello')")
print(spam.startswith('Hello'))
print("That shows true.\n")

print("""We could probably run some of these method calls together.
If we run spam.startswith('hello'), it should return False as it's case sensitive.""")
print(spam.startswith('hello'))
print("Yay, it worked!")
print("\n Now, let's try calling spam.lower().startswith('hello')")
print(spam.lower().startswith('hello'))
print("... which should return True, as we've asked to run the 'startswith' on the lower case version.")

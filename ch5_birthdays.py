birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 12'}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    if name == "":
        break

    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their brithday?")
        bday = input()
        birthdays[name] = bday
        print("Birthday database updated.")

# Important to remember; keys(), values() and items() are METHODS
# Use them on dictionaries like dictName.keys()

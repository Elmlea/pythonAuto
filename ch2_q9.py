# planned output is 'Hello' if spam = 1
# 'Howdy' if spam = 2
# 'Greetings' if it's anything else

spam = input("What would you like to store in spam? :>")
if str(spam) == "1":
    print("Hello!  You stored " + str(spam) + " in spam.")
elif str(spam) == "2":
    print("Howdy!  You stored " + str(spam) + " in spam.")
else:
    print("Greetings!  You stored " +str(spam) + " in spam.")

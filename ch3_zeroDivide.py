def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError: # is this a name for the exception clause?
        print("Error: Invalid Arguement.")

print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

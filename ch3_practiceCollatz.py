def collatz(number):
    if (number % 2) == 0:
        number = number // 2
        return number
    if (number % 2) == 1:
        number = (number * 3) + 1
        return number

while True: # sets up an infinite loop until a valid value is given
    try:
        value = int(input("What number would you like to start with? :> "))
        print(value)
        break

    except(ValueError):
        print("You have to enter a number.")

while value != 1:
    value = collatz(value)
    print(value)

print("Finished!")

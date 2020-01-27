print("Justifying!")
print("""
We use rjust() and ljust() to justify text.  They can be passed 2 parameters;
the first one gives the total length of the area to justify over, and the second
is a padding character.

Hence, 'Hello'.rjust(10) will put 5 blank spaces in front of hello.
'Hello'.rjust(10,'*') will fill those 5 blank spaces with *.""")
print("\nHence:\n")
print('hello'.rjust(10))
print('hello'.rjust(10,'*'))

print("\nThe same applies for center and ljust, using the syntax:")
print("""
print('hello'.ljust(20,'X'))
print('hello'.center(20,'*'))
When centered (sic) the filler characters are used on both sides.""")

print("Such as:\n")

print('hello'.ljust(20,'X'))
print('hello'.center(20,'*'))

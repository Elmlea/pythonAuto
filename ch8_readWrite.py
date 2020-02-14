# Call the open() function to create a file object; this is 'loading the disk'
# Call read() or write() to do stuff.  Read is like scanning for a DVD chapter
# Call close() to 'eject' the disk

import os

helloFile = open('hello.txt', 'r') # r for reading mode; it's the default
helloContent = helloFile.read()
print(helloContent)

# readlines method returns a list of lines
sonnetFile = open('sonnet29.txt', 'r')
print(sonnetFile.readlines())

# mode w overWrites, mode a Appends
baconFile = open('bacon.txt', 'w')
baconFile.write("Hello World!\n")
baconFile.close()

baconFile = open('bacon.txt', 'a')
baconFile.write("Bacon is not a vegetable.")
baconFile.close()

baconFile = open('bacon.txt', 'r')
content = baconFile.read()
baconFile.close()

print(content)

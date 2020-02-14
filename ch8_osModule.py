# os.path.join connects the elements in a way readable by the host OS, filling
# / or \ etc depending on what system is running.
import os

myFiles = ['agrius.txt', 'fish.xls']
for filename in myFiles:
        print(os.path.join('MacHD/users/mark/home', filename))

# the above should print the 2 files with the other 'MacHD' part correctly added

# to pull the current working directory use getcwd:
print(os.getcwd())

# you can change directories using chdir:
# / is the root directory in OSX, which seems to be the HD root (containing system,
# library, users etc)
os.chdir('/Users/markwharry/')
print(os.getcwd())
os.chdir('/Users/markwharry/Dropbox/Mark/Files/Python/pythonAuto/')
print(os.getcwd())

# mkdirs makes a new folder
# syntax is os.makdirs('path')
# this block shows how to use relative paths as well
os.makedirs('./testDir')
os.chdir('./testDir')
print("\nWe just made the directory " +os.getcwd() + " and moved to it.")
os.chdir('..')
print(os.getcwd())
os.rmdir('./testDir')

# path handling can isue os.path.abspath(path) and ispath(path)
# os.path.relpath(path, start) will return a string of a relative path from start
# . refers to the CWD
print("\nThe current absolute path is " + os.path.abspath('.'))
print("Making another test directory called 'testDirectory'")
os.makedirs('./testDirectory')
print("Without moving directories, its path is " + os.path.abspath('./testDirectory'))
os.rmdir('./testDirectory')

# practice with relpath; it should be how to get to first arg from the second
# last example shows '../pythonAuto as you'd go up one level, then in to pythonAuto
print(os.path.relpath('/Users/markwharry/Dropbox/Mark/Files', '/Users'))
print(os.path.relpath(os.getcwd(), '/Users'))
print(os.path.relpath(os.getcwd(), '/Users/markwharry/Dropbox/Mark/Files/Python/pythonFluent'))

# splitting paths uses 2 methods:
# basename returns the bit after the final /
# dirname returns the bits before
# os.path.split will do the opposite of join, and return a tuple of these 2 values
path = 'Users/markwharry/Dropbox/Mark/Files/Python/pythonAuto/ch8_osModule.py'
print(os.path.basename(path))
print(os.path.dirname(path))

# splitting to return a list with each value uses the string split methods
# the arguement fed is os.path.sep, which represents the path separator
# working on the path above:
print(path.split(os.path.sep))

# boolean results can be pulled from os.path.exists, os.path.isdir, and isfile

# first operators; os.listdir returns a list of files in a directory,
# and os.path.getsize finds the size of the files

print(os.path.getsize('ch8_osModule.py'))
print(os.listdir(os.getcwd()))

print("\nHow much work have you done on Python so far?")
print("")
totalSize = 0
for filename in os.listdir(os.getcwd()):
    totalSize = totalSize + os.path.getsize(filename)
print(totalSize)

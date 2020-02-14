# this module allows us to save variables to binary shelf Files

import shelve

# same as opening a text file; if the file doesn't exist it will be created
# syntax; call open on the module, pass the filename as a param
shelfFile = shelve.open('mydata')

cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cats'] = cats # assigns the list 'cats' to shelfFile with the key 'cats,' like a dictonary
shelfFile.close()

# running this will create a mydata.db file

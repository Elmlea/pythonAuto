# this is designed to be typed into the shell, but we'll do it here

import pprint

cats = [{'name': 'Zophie', 'desc': 'chubby'}, {'name': 'Pooka', 'desc': 'fluffy'}]
print(pprint.pformat(cats))

fileObj = open('ch8_myCats.py', 'w') # generates the file
fileObj.write('cats = ' + pprint.pformat(cats) + '\n') # pformat returns a string, which is saved in our text/py file
fileObj.close()

# we're effectively getting the program to write another program; so all the data has to be a string

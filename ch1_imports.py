import random
for i in range(5):
    print(random.randint(1, 10))
    # randint is in the random module, so has to be called on it.
    # we can avoid this by importing in the format 'from random import *'
    # then we can call randint without calling it on the random prefix

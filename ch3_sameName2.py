def spam():
    global eggs
    eggs = "spam" # sets the global variable eggs

eggs = "global"
spam()
print(eggs) # prints "spam;" line 6 sets the global variable

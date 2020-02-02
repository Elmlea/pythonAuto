# NOTE: Use of pipe | in regular expressions

# “The | character is called a pipe. You can use it anywhere you want
# to match one of many expressions. For example, the regular
# expression r'Batman|Tina Fey' will match either 'Batman' or
# 'Tina Fey'.

# When both Batman and Tina Fey occur in the searched string,
# the first occurrence of matching text will be returned as
# the Match object.
print("Regex Objects 3 - Matching Multiple Patterns\n")
print("The | character allows us to effectively place an 'or' term in a regex.")
print("heroRegex = re.compile(r'Batman|Tina Fey')")

import re
heroRegex = re.compile(r"Batman|Tina Fey")

print("mo1 = heroRegex.search(I like Batman and Tina Fey)")
mo1 = heroRegex.search(r"I like Batman and Tina Fey")
print("""This sets the match object var mo1 as the first instance of
Batman or Tina Fey.""")

print("mo1.(group()) should be Batman")
print(mo1.group())
print("\nNote we can't specify different groups as we haven't")
print("set up multiple groups in the original regex.")
print("\n We use the findall method to find all matches.")

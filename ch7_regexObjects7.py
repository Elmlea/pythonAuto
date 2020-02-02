print("Regex Objects 7 - Specific Repetitions\n")

print("""To match a specific number of repetitions, we use
curly brackets with the number of repetitions within them.

You can also specify a range within them.  For example:

(Ha){3} will only match HaHaHa
(Ha){3,5} will match HaHaHa, HaHaHaHa and HaHaHaHaHa

(Ha){3,} will match at least 3 repetitions, and
(Ha){,5} will match between 0 and 5.

The first use of this demonstrates greedy matching.
If we set up:

greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')

... then mo1.group() should return 'HaHaHaHaHa'.  Even though HaHaHa
and HaHaHaHa are valid options, it's 'greedy' so it goes for the largest.
""")

import re
greedyHaRegex = re.compile(r"(Ha){3,5}")
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())

print("""
Asking it to print mo1.group(1) will print "Ha," as that's the
group it's matched.  Remember, group() will show the whole matching
string.
""")

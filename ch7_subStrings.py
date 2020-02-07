print("""The sub method can be called on a regex object to
substitute any matches.  The first argument is the replacement text,
the second arg is the string to search.  Eg:

namesRegex = re.compile(r'Agent \w+')
namesRegex.sub('CENSORED', 'Agent Alice have the secret documents
to Agent Bob.')

Results in:
""")

import re
namesRegex = re.compile(r"Agent \w+")
mo = namesRegex.sub("CENSORED", "Agent Alice gave the secret documents to Agent Bob.")
print(mo)

print("""
In the first argument to sub, you can pass \\1 etc, which means '
enter the text of group 1 in the substitution.'

For example, say you want to censor the agent names but show the
first letters.  You could use the regex Agent (\\w)\\w*, and pass
r'\\1*****' as the first argument to sub.  The \\1 in the string
will be replacd by whatever text was matched by group 1; that is,
the (\w) group of the regex.

To test this:
agentNamesRegex = re.compile(r'Agent (\\w)w*')
mo1 = agentNamesRegex.sub(r'\\1***', 'Agent Alice told Agent Carol
that Agent Eve knew Agent Bob was a double agent.')
""")

agentNamesRegex = re.compile(r"Agent (\w)\w+")
mo1 = agentNamesRegex.sub(r"******","Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(mo1)

mo2 = agentNamesRegex.sub(r"Agent \1", "Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double agent.")
print(mo2)

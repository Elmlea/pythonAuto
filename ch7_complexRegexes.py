print("""
Verbose mode tells the re.compile function to ignore whitespace.
This allows us to spread out the format a lot more.
We pass the variable re.VERBOSE as the second argument to re.compile.

phoneRegex = re.compile(r'((\d{3}|\(\d{3}\))?(\s|-|\.)?\d{3}(\s|-“|\.)\d{4}
(\s*(ext|x|ext.)\s*\d{2,5})?)')

becomes:

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    \d{3}                         # first 3 digits
    (\s|-|\.)                     # separator
    \d{4}                         # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

Note we use triple quotes to spread the string over multiple lines,
Comments are ignored until the end of the line as normal.
Extra whitespace is ignored as well.

re.compile only takes a single second argument; if you want to combine
them, use the pipe, eg:

someRegexValue = re.compile('foo', re.IGNORECASE | re.DOTALL)

""")

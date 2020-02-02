# All about removing whitespace

print("""The strip command will return a new string when called on one,
stripping out all the whitespace.

Lstrip and rstrip are predictably the same, but will only
strip whitespace to the left and right.

Optionally, a string argument can be used to tell it what characters
to strip.  This doesn't have to be in order.

For example, if we set spam = 'SpamSpamSpamBaconSpamEggsSpamSpam,'
then call spam.strip('ampS'), we get:""")

spam = 'SpamSpamSpamBaconSpamEggsSpamSpam'
print(spam.strip(ampS))

print("""This should show BaconSpamEggs.  It's taken every instance
of S, a, m and p together and stripped them.""")

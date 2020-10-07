print("""
Write a short Python function that takes a string s, representing a sentence,
and returns a copy of the string with all punctuation removed.
For example, if given the string "Let's try, Mike.",
this function would return "Lets try Mike".
""")

s = input('Type your sentence here: ')

clean = ''.join([i for i in s if i.isalnum() or i.isspace()])

print('Sentence without punctuation: {0}'.format(clean))

        


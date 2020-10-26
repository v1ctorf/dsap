print("""
Write a Python program that inputs a list of words, separated by whitespace,
and outputs how many times each word appears in the list. You
need not worry about efficiency at this point, however, as this topic is
something that will be addressed later in this book.
""")

words = input('Type your list, son: ')

dict_words = {}

for i in words.split(' '):    
    dict_words[i] = dict_words[i] + 1 if i in dict_words else 1
    
print(dict_words)

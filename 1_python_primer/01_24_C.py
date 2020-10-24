print("""
Write a short Python function that counts the number of vowels in a given
character string
""")

string = input('Type your string here: ')
total_vowels = sum(1 for i in string.lower() if i in 'aeiou')
print('This string contains {0} vowels.'.format(total_vowels))

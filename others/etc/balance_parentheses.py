print("""
Given an expression string exp, write a program to examine whether the pairs
and the orders of “{“, “}”, “(“, “)”, “[“, “]” are correct in exp.

Input: exp = “[()]{}{[()()]()}” 
Output: Balanced

Input: exp = “[(])” 
Output: Not Balanced 
""")

words = input('Type your list, son: ')

dict_words = {}

for i in words.split(' '):
    dict_words[i] = dict_words[i] + 1 if i in dict_words else 1

print(dict_words)



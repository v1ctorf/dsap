print("""
Write a Python program that outputs all possible strings formed by using
the characters c , a , t , d , o , and g exactly once.
""")

import itertools

def all_possible_strings(keyword):
    all_p_str = set()

    for i in range(len(keyword)):        
        for combinations in list(itertools.permutations(keyword, i + 1)):
            for products in list(itertools.product(list(combinations), repeat = i + 1)):
                all_p_str.add(''.join(list(products)))

    return list(all_p_str)


keyword = input('Type "catdog" or other word you want: ')

all_strings = [i for i in all_possible_strings(keyword)]
print(all_strings)
      

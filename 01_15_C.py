print("""
Write a Python function that takes a sequence of numbers and determines
if all the numbers are different from each other (that is, they are distinct).
""")

from others.helpers import get_list_integers

def are_all_distincts(int_list):    
    return len(int_list) == len(set(int_list))

int_list = get_list_integers()

print(are_all_distincts(int_list))

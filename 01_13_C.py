print("""
Write a pseudo-code description of a function that reverses a list of n integers, so that
the numbers are listed in the opposite order than they were before, and compare this
method to an equivalent Python function for doing the same thing.
""")

from others.helpers import get_list_integers

def reverse_my_list(int_list):
    return [int_list[i] for i in range(len(int_list)-1,-1,-1)]

done = False
int_list = get_list_integers()

print('\nList of Integers:')
print(int_list)

print('\nList of Integers reversed:')
print(list(reversed(int_list)))

print('\nList of Integers reversed by me:')
print(reverse_my_list(int_list))

print('\nAnother way to reverse it:')
print(int_list[::-1])



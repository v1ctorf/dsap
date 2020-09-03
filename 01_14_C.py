"""
Write a short Python function that takes a sequence of integer values and
determines if there is a distinct pair of numbers in the sequence whose
product is odd.
"""

from others.helpers import get_list_integers


def get_odd_products(int_list):
    return len([i for i in set(int_list) if i & 1 == 1]) >= 2


int_list = get_list_integers()

print(get_odd_products(int_list))

"""
In order to have an odd product, both factors must be odd. The exercise also requires us
to "determine if there is a pair", not to list all pairs. So, we have to determine
if the list contains at least 2 distinct odd numbers.
"""


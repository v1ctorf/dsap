print("""
Write a short Python program that takes two arrays a and b of length n
storing int values, and returns the dot product of a and b. That is, it returns
an array c of length n such that c[i] = a[i] · b[i], for i = 0,...,n−1.
""")

import sys
sys.path.append("..")

from others.helpers import get_list_integers

print("Define the first array")
a_arr = get_list_integers()

print("Define the second array")
b_arr = get_list_integers()

prod = [a_arr[i] * b_arr[i] for i in range(len(a_arr))]

print("Dot Product (Vector) = {0}".format(prod))
print("Dot Product = {0}".format(sum(prod)))

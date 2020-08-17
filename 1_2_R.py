# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.

def is_even():
    k = int(input('Enter an integer value: '))
    return k % 2 == 0

print(is_even())
    

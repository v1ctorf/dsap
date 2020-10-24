"""
Write a short Python function that takes a positive integer n and returns
the sum of the squares of all the positive integers smaller than n.
"""


def sum_squares(n):
    total = 0    

    for num in range(n):
        square = num * num
        total += square        
        
    return total


data = int(input('Enter a positive integer: '))
print(sum_squares(data))

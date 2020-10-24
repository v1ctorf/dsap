"""
Give a single command that computes the sum from Exercise R-1.4,
relying on Python’s comprehension syntax and the built-in sum function.
"""

n = int(input('Enter a positive integer: '))

print(sum([k*k for k in range(n)]))

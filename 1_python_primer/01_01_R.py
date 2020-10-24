print("""
Write a short Python function, is multiple(n, m), that takes two integer
values and returns True if n is a multiple of m, that is, n = mi for some
integer i, and False otherwise.
""")

def is_multiple():
    n = int(input('Enter an integer value: '))
    m = int(input('Enter another integer value: '))
    return m % n == 0

print(is_multiple())



print("""
Write a short program that takes as input three integers, a, b, and c, from
the console and determines if they can be used in a correct arithmetic
formula (in the given order), like “a + b = c,” “a = b − c,” or “a * b = c.”
""")

import operator

operator_list = [operator.add, operator.sub, operator.mul, operator.truediv]

a = int(input('Integer A: '))
b = int(input('Integer B: '))
c = int(input('Integer C: '))

possible_ops = []

for op in operator_list:
    if a == op(b,c):
        possible_ops.append('{0} = {1} {2} {3}'.format(a,b,op.__name__,c))
    if op(a,b) == c:
        possible_ops.append('{0} {1} {2} = {3}'.format(a,op.__name__,b,c))        

print(possible_ops)


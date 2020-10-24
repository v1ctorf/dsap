print("""
Write a Python program that simulates a handheld calculator.
Your program should process input from the Python console representing buttons
that are “pushed”, and then output the contents of the screen after each operation is performed.
Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
""")

import operator, os, re

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}


os.system('cls')

print('Use your numeric pad.')

x = input('> ')


for i in x:
    if re.match("[0-9\-\*\/\+\.]", i) == None:
        raise Exception('Input contains invalid character')


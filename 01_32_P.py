print("""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
""")
import operator

operators = {
    '+':operator.add,
    '-':operator.sub,
    '*':operator.mul,
    '/':operator.truediv
}

a = float(input('A........: '))
op = input('[{0}]: '.format(' '.join(list(operators.keys()))))

if op not in operators.keys():
    raise Exception('"{0}" is not a valid operator'.format(op))

b = float(input('B........: '))

print('{0} {1} {2}'.format(a,op,b))



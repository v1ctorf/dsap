print("""
Write a Python program that can simulate a simple calculator, using the
console as the exclusive input and output device. That is, each input to the
calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
can be done on a separate line. After each such input, you should output
to the Python console what would be displayed on your calculator.
""")
import operator

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

end_of_exec = True

print(' Use {0}'.format(', '.join(list(operators.keys()))))

a = None
b = None
op = None

while end_of_exec:
    try:
        x = input(' ? ')

        if x.isnumeric() or x.replace('.','',1).isdigit():
            if a == None or op == None:
                a = x
            elif b == None:
                b = x
                a = operators[op](float(a),float(b))
                print(' > {0}'.format(a))                
                op = None
                b = None
        elif x in operators.keys():         
            op = x            
        else:            
            raise Exception('"{0}" is not a valid entry')
        
    except (EOFError, KeyboardInterrupt):
        end_of_exec = False            

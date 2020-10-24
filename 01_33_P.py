print("""
Write a Python program that simulates a handheld calculator.
Your program should process input from the Python console representing buttons
that are “pushed,” and then output the contents of the screen after each operation is performed.
Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
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

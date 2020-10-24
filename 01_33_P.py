print("""
Write a Python program that simulates a handheld calculator.
Your program should process input from the Python console representing buttons
that are “pushed”, and then output the contents of the screen after each operation is performed.
Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
""")

import os, re

os.system('cls')
end_of_exec = False

print('Use your numeric pad.')

while not end_of_exec:
    try:
        x = input('? ')
        
        if re.search("[^0-9\-\*\/\+\.]", x):
            print('Input contains invalid character')        

        print('> {0}'.format(eval(x)))
    except (EOFError, KeyboardInterrupt):
        end_of_exec = True 

    
    

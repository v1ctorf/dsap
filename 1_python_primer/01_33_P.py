print("""
Write a Python program that simulates a handheld calculator.
Your program should process input from the Python console representing buttons
that are “pushed”, and then output the contents of the screen after each operation is performed.
Minimally, your calculator should be able to process
the basic arithmetic operations and a reset/clear operation.
""")

import os, re

def reset_screen():
    os.system('cls')
    print('Use your numeric pad and press "c" to reset')

reset_screen()    

end_of_exec = False


while not end_of_exec:
    try:
        x = input('? ')

        if x == 'c':
            reset_screen()           
        elif re.search("[^0-9\-\*\/\+\.]", x):
            print('> Input contains invalid character')        
        else:
            print('> {0}'.format(eval(x)))
    except (EOFError, KeyboardInterrupt):
        end_of_exec = True 

    
    

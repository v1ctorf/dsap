print("""
Write a Python program that repeatedly reads lines from standard input
until an EOFError is raised, and then outputs those lines in reverse order
(a user can indicate end of input by typing ctrl-D).
""")

outputs = list()
not_eof = True

while not_eof:
    try:
        line = input('Type here: ')        
        outputs.append(line)
    except EOFError, KeyboardInterrupt:
        not_eof = False

for i in reversed(outputs):
    print('You typed: {0}'.format(i))    

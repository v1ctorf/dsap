print("""
Python’s random module includes a function shuffle(data) that accepts a list of elements and
randomly reorders the elements so that each possible order occurs with equal probability.

The random module includes a more basic function randint(a, b) that returns a uniformly
random integer from a to b (including both endpoints). Using only the randint function,
implement your own version of the shuffle function.
""")

from random import shuffle, randint

data = list('abcdefghijkl')
shuffle(data)
print(data)


def gen_shuffle(data):
    while len(data) > 0:
        el = randint(0, len(data) - 1)
        yield data.pop(el)
    
def my_shuffle(data):
    for i in list(gen_shuffle(data)):
        data.append(i)      
        

data = list('abcdefghijkl')
my_shuffle(data)    
print(data)



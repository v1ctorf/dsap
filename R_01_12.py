# Python’s random module includes a function choice(data) that returns a random element from a non-empty
# sequence. The random module includes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given range.
# Using only the randrange function, implement your own version of the choice function.

from random import randrange, choice

x = range(1,100)

print(choice(x))

def my_own_choice(s):
    return randrange(s.start, s.stop, s.step)

print(my_own_choice(x))

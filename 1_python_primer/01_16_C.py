print("""
In our implementation of the scale function (page 25), the body of the loop
executes the command data[j] *= factor. We have discussed that numeric
types are immutable, and that use of the *= operator in this context causes
the creation of a new instance (not the mutation of an existing instance).
How is it still possible, then, that our implementation of scale changes the
actual parameter sent by the caller?
""")

import sys
sys.path.append("..")


from others.helpers import get_list_integers

def scale(data, factor):
    for j in range(len(data)):
        data[j] *= factor

data = get_list_integers()

print(data)
scale(data, 3)
print(data)

print("""
In fact, numeric types are immutable, but scale function handles
a mutable parameter, which is a List, and this is why this parameter changes.
""")

def test(just_a_int, factor):
    just_a_int *= factor

int_data = int(input('Enter a integer: '))
print(int_data)
test(int_data, 3)
print(int_data)

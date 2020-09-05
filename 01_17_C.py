print("""
Had we implemented the scale function (page 25) as follows, does it work
properly?
""")

from others.helpers import get_list_integers

def scale(data, factor):
    for val in data:
        val *= factor

data = get_list_integers()

print(data)
scale(data, 3)
print(data)

print("""
If you mean to make this function work as it works on page 25 and exercise C-1.16, no, you hadn't.
You are trying to modify an immutable type, which is numeric (var val), and this can't be done
this way. This would require a mutable numeric class, which is doable, but not trivial.
""")


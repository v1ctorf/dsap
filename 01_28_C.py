print("""
The p-norm of a vector v = (v1,v2,...,vn) in n-dimensional space is defined
as [see book]

For the special case of p = 2, this results in the traditional Euclidean
norm, which represents the length of the vector. For example, the Euclidean norm of a two-dimensional vector with coordinates (4,3) has a
Euclidean norm of √
42 + 32 = √16+9 = √
25 = 5. Give an implementation of a function named norm such that norm(v, p) returns the p-norm
value of v and norm(v) returns the Euclidean norm of v. You may assume
that v is a list of numbers.
""")

from others.helpers import get_list_integers

def norm(v, p = None):
    if (p == None):
        print('Euclidean')
    else:
        print('p norm')
    

int_list = get_list_integers()

print(norm(int_list))

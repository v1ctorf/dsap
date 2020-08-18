# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.

def minmax(data):
    min_n, max_n = None, None
    
    for n in data:
        if min_n is None or n < min_n:
            min_n = n
            
        if max_n is None or n > max_n:
            max_n = n 
    
    return min_n, max_n


done = False
data = set()

while not done:
    n = input('Enter an integer number (blank if done): ')

    if n == '':
        done = True
    else:
        data.add(int(n))
        
print(minmax(data))



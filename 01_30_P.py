print("""
Write a Python program that can take a positive integer greater than 2 as
input and write out the number of times one must repeatedly divide this
number by 2 before getting a value less than 2.
""")

num = int(input('enter a positive integer greater than 2, please: '))

if num <= 2:
    raise Exception('You are a rebel!')

count = 1

while 2 ** count <= num:
    count += 1    

print('\n{0} time(s)'.format(count - 1))







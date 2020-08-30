# Write a pseudo-code description of a function that
# reverses a list of n integers, so that the numbers are listed in the opposite order than they
# were before,
# and compare this method to an equivalent Python function for doing the same thing.

done = False
data = []

while not done:
    n = input('Enter an integer number (blank if done): ')

    if n == '':
        done = True
    else:
        data.append(int(n))
        print('List = {0}'.format(data))

print(data)

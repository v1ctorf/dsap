print("""
Give an example of a Python code fragment that attempts to write an element to a list
based on an index that may be out of bounds. If that index
is out of bounds, the program should catch the exception that results, and
print the following error message: “Don’t try buffer overflow attacks in Python!”
""")


from random import randint

print('Generating list (random length, from 0 to 10)...')
rand_list = [i for i in range(randint(0, 10))]

guess = int(input('\nTry your luck - choose an index: '))

print('\nWriting {0} on index #{0}...'.format(guess))

try:
    rand_list[guess] = guess
    print("\nYOU DID IT!")
except (IndexError):
    print("\nDon’t try buffer overflow attacks in Python!")
finally:
    print("\nUnveiling the random list: {0} ".format(rand_list))



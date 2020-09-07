print("""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [ a , b , c , ..., z ], but without having to type all 26 such
characters literally.
""")

# To get the ASCII code of a character, use the ord() function.
# To get the character encoded by an ASCII code number, use the chr() function.

letters = [chr(i) for i in range(ord('a'), ord('z') + 1)]

print(letters)



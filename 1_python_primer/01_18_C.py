print("""
Demonstrate how to use Python’s list comprehension syntax to produce
the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].    
""")

print([i * x for i, x in enumerate(range(1,11))]) 

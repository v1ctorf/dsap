print("""
Write a Python program that can “make change.”
Your program should take two numbers as input,
one that is a monetary amount charged and the
other that is a monetary amount given. It should then return the number
of each kind of bill and coin to give back as change for the difference
between the amount given and the amount charged. The values assigned
to the bills and coins can be based on the monetary system of any current
or former government. Try to design your program so that it returns as
few bills and coins as possible.
""")


currency = {
    '1c':0.01,
    '2c':0.02,
    '5c':0.05,
    '10c':0.10,
    '20c':0.20,
    '50c':0.50,
    '1 EUR':1,
    '2 EUR':2,
    '5 EUR':5,    
    '10 EUR':10,
    '20 EUR':20,
    '50 EUR':50,
    '100 EUR':100,
    '200 EUR':200,
    '500 EUR':500
}

print('Our currency system is: {0}'.format(currency))

amount = float(input('\nMonetary amount charged: '))
given = float(input('Monetary amount given: '))

change = round(given - amount, 2)

# if (change < 0

print('Change = {0}; thus... '.format(format(change,'.2f')))      

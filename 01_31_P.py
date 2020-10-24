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
    '500 EUR':500,
    '200 EUR':200,
    '100 EUR':100,
    '50 EUR':50,
    '20 EUR':20,    
    '10 EUR':10,
    '5 EUR':5,
    '2 EUR':2,
    '1 EUR':1,
    '50c':0.50,
    '20c':0.20,
    '10c':0.10,
    '5c':0.05,
    '2c':0.02,
    '1c':0.01    
}

print('Our currency system is: {0}'.format(currency))

#amount = float(input('\nMonetary amount charged - in EUR: '))
#given = float(input('Monetary amount given - in EUR: '))
amount = float(55.89)
given = float(100)
due = round(given - amount, 2)

if (due < 0):
    raise Exception('Sorry, this is not enough money!')

print('\nDue = EUR {0}; thus...'.format(format(due,'.2f')))

change = []

for i in currency.items():
    if i[1] <= due:
        while i[1] <= due:
            change.append(i)
            due -= i[1]

dict_change = dict(change)
print(change)
print(sum(i for i in dict_change.values()))

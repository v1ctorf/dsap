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
    'EUR 500':500.00,
    'EUR 200':200.00,
    'EUR 100':100.00,
    'EUR 50':50.00,
    'EUR 20':20.00,    
    'EUR 10':10.00,
    'EUR 5':5.00,
    'EUR 2':2.00,
    'EUR 1':1.00,
    '50c':0.50,
    '20c':0.20,
    '10c':0.10,
    '5c':0.05,
    '2c':0.02,
    '1c':0.01    
}

print('Our currency system is: {0}'.format(currency))

amount = float(input('\nMonetary amount charged - in EUR: '))
given = float(input('Monetary amount given - in EUR: '))
due = round(given - amount, 2)

if (due < 0):
    raise Exception('Sorry, this is not enough money!')

print('\nDue = EUR {0}; thus'.format(format(due,'.2f')))

change = []

for i in currency.items():    
    if i[1] <= due:        
        while i[1] <= due:
            change.append(i)
            due -= i[1]
            due = round(due, 2)

dict_change = dict()

for i in change:
    if i[0] in dict_change:
        dict_change[i[0]] += 1
    else:
        dict_change[i[0]] = 1
    
print(dict_change)


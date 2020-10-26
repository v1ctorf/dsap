print("""
The birthday paradox says that the probability that two people in a room
will have the same birthday is more than half, provided n, the number of
people in the room, is more than 23. This property is not really a paradox,
but many people find it surprising. Design a Python program that can test
this paradox by a series of experiments on randomly generated birthdays,
which test this paradox for n = 5,10,15,20,...,100.
""")

print("""
The problem is to compute an approximate probability that in a group of n
people at least two have the same birthday. For simplicity, variations in
the distribution, such as leap years, twins, seasonal, or weekday variations
are disregarded, and it is assumed that all 365 possible birthdays are
equally likely.

Real-life birthday distributions are not uniform, since not all dates are
equally likely, but these irregularities have little effect on the analysis.
Actually, a uniform distribution of birth dates is the worst case.
""")

from random import choice

xp = [] 

for n in range(5,101,5):
    birthdays = [choice(range(1,365)) for i in range(0, n)]

    p = 1.0

    for i in range(1, n+1):
        p = p * (365 - i + 1) / 365
        
    xp.append((
        format(n, '3d'),
        format(100* (1 - p),'.10f'),
        len(birthdays) > len(set(birthdays))        
    ))

print('(N, P, Simulation)')
print(''.join((["\n{0}".format(i) for i in xp])))


    

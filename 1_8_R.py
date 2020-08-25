# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index −n ≤ k < 0,
# what is the equivalent index j ≥ 0 such that s[j] references the same element?

from random import randint

s = input('Enter a string with unique characters: ')

n = len(s)
print('length n = {0}'.format(n))

print('s = {0}'.format(s))

k = randint(1, n) * -1
print('selected index k = {0}'.format(k))
print('s[k] = {0}'.format(s[k]))

j = s.find(s[k])
print('equivalent index j = {0}'.format(j))
print('s[j] = {0}'.format(s[j]))

print('abs(j) + abs(k) = n; thus {0} + {1} = {2}'.format(j,k,n))


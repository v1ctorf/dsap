# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.

def sum_odd_squares(n):
    total = 0

    for num in range(n):        
        if num % 2 > 0:
            square = num * num
            total += square
            # print("{0} * {0} = {1} => subtotal is {2}".format(num, square, total))

    return total


data = int(input('Enter a positive integer: '))
print(sum_odd_squares(data))

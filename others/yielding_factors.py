def factors(n): # generator that computes factors
    for k in range(1,n+1):
        if n % k == 0: # divides evenly, thus k is a factor
            yield k # yield this factor as next result

def factorsx(n): # generator that computes factors
    k=1
    while k * k < n: # while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n: # special case if n is perfect square
        yield k

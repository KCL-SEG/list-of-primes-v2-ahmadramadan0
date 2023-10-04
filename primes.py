"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError

    list = []
    i = 2
    while len(list) < number_of_primes:
        for n in range(2, i):
            if i % n == 0:
                break
        else:
            list.append(i)
        i += 1
    return list

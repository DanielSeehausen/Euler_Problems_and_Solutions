#Simple solution to Hackerrank's Project Euler Problem #7 prompt. 
#https://www.hackerrank.com/contests/projecteuler/challenges/euler007/submissions/code/7083742

import sys

'''
As we are dealing with primes, I defaulted to snagging a Sieve of Eratosthenes implementation from one of the top links after googling it. This simply generates primes up to a limit, stores them in a list, and fetches them by index as the question is requesting the Nth prime.
'''

def primes_sieve2(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
                
test_cases = int(sys.stdin.readline())

prime_indexes = []
for case in range(test_cases):
    idx = int(sys.stdin.readline())
    prime_indexes.append(idx)

primes = []
for prime in primes_sieve2(200000):
    primes.append(prime)

for prime in prime_indexes:
    print primes[prime - 1]



    

from math import sqrt
import itertools
import sys

'''
Python 3 solution to Euler problem 3: finding the largest prime factor.
This was solved for HackerRank's input
'''

#This load the test cases list
burn_me = input()
test_cases = []
while True:
    try:
        case = int(input())
    except EOFError:
        break
    test_cases.append(case)

def lpf(val, factor_index=0):
    #if divisible by 2, keep dividing
    while True:
        if val % 2 == 0:
            val /= 2
        else:
            break
    #if the number boiled down to 1, 2 is the largest prime factor
    if val == 1: 
        return 2
    
    #starting at 3 (there are no even primes) increment by 2 while attempting to divide
    #the value
    divisor = 3
    while True:
        #if the square of the divisor is greater than the value we are trying to divide, 
        #then we will not find anything greater
        if divisor**2 == val:
            val = divisor
        if divisor**2 > val:
            break

        #if the number is evenly divisible, divide it and restart the divisor at 3
        if val % divisor == 0: 
            val = val/divisor
            divisor = 3
        else:
            divisor += 2

    #if what is left is greater than two, then it is the largest prime factor
    if val > 2:
        return val
    #otherwise, it was the last divisor we got up to
    return divisor
            

for case in test_cases:
    print(int(lpf(case)))
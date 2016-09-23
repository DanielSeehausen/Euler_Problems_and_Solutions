# Designed to answer the input from Hackerrank's prompt for Project Euler problem #9
#https://www.hackerrank.com/contests/projecteuler/challenges/euler009/submissions/code/7102148

import math
from sys import stdin


test_cases = int(stdin.readline())

#each test case provides a single integer (N) which is equal to a + b + c when a^2 + b^2 = c^2 is true

for case in range(test_cases):
    
    n = int(stdin.readline())
 
    #our method is derived from simplifying these equations to one unknown variable, which we loop over a set of all potential values.
    #in this case, N is a constant, a loop is created that increments a values and checks for validity of b/c values
    #a + b + c = n
    #a^2 + b^2 = c^2

    #c = n - a - b
    #now we can substitute this value in for c 
    #a^2 + b^2 = (n - a - b)^2
    #a^2 + b^2 = n^2 + a^2 + b^2 + 2ab - 2an - 2bn
    #a^2 - (a - n)^2 = b(2a - 2n)
    #b = (a^2 - (a - n)^2) / 2(a - n)
    
    n = float(n)
    a_final = None
    b_final = None
    c_final = None
    
    #for every possible value of a
    for a in range(1, int(n)/2):
        b = (a**2 - (a - n)**2) / (2*(a-n))
        c = n - a - b
        #if we have exceeded the given restrictions, end
        if a >= b or b >= c:
            break
        #if the values for a b and c satisfy our conditions, store them
        #as we increment a, we re-write the values as long as they satisfy the condition, as the highest found value for a will yield the highest product
        if a%1 == 0 and b%1 == 0 and c%1 == 0:
            a_final = a
            b_final = b
            c_final = c
    #if we never found a set of values that satisfy the condition, then they never overwrote the initial None value. Return -1
    if a_final == None:
        print -1
    else:
        print int(a_final*b_final*c_final)
        

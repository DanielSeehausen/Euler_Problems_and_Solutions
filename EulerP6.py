# Simple solution to Hackerrank's Project Euler problem 6 prompt
#Please see: https://www.hackerrank.com/contests/projecteuler/challenges/euler006

'''
While a clever method of calculating the square of sums may exist, only the equation for calculating the sum of squares was needed to satisfy the time constraints for this problem. 
'''

import sys

test_cases = int(sys.stdin.readline())

for case in range(test_cases):
    i = int(sys.stdin.readline())
    sum_of_squares = (i*(i+1)*(2*i + 1))/6

    square_of_sum = 0
    for n in range(1, i + 1):
        square_of_sum += n
    square_of_sum **= 2
    
    print square_of_sum - sum_of_squares

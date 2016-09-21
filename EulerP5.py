#Prompt from Hackerrank's Project Euler Problem #5
#please visit: https://www.hackerrank.com/contests/projecteuler/challenges/euler005

import fileinput
import sys

'''
This is a simple solution to Euler problem #5. As opposed to brute forcing every integer, this iterates over the largest interval possible, and checks each integer for divisibility by the larger set. 
'''

cases = sys.stdin.readline()

for case in range(int(cases)):
    n = int(sys.stdin.readline())
    cur_no = n
    
    #only if the solution is found does the loop break
    while True:
        found = True
        for i in range(1, int(n) + 1):
            #if one of the ints is not a entirely divisible, we skip up to the next integer
            if cur_no % i != 0:
                cur_no += n
                found = False
                break
        if found == True:
            print cur_no
            break
       
        
    

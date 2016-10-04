#Question prompt from Hackerrank's project Euler contest
#https://www.hackerrank.com/contests/projecteuler/challenges/euler011

'''
Follow is a simple solution to checking a grid for the largest product from a limited distance vert/horiz/diagonal
line within the grid
The code is short and ugly, using one iteration through the grid and checking all possible lines wherever they
have at least 4 integers available to make a product

There are quicker ways of doing this, but under the constraints provided for this problem (a grid 20x20)
this solution is plenty quick
'''

from sys import stdin

g = [[int(i) for i in stdin.readline().split()] for r in range(20)]


bf = float("-inf")
for r in range(20):
    for c in range(20):
        #h
        if c > 2:
            h = g[r][c] * g[r][c-1] * g[r][c-2] * g[r][c-3]
            if h > bf:
                bf = h
            #bs
            if r > 2:
                bs = g[r][c] * g[r-1][c-1] * g[r-2][c-2] * g[r-3][c-3]
                if bs > bf:
                    bf = bs
        #fs
        if c < 17 and r > 2:
            fs = g[r][c] * g[r-1][c+1] * g[r-2][c+2] * g[r-3][c+3]
            if fs > bf:
                bf = fs
        #v
        if r > 2:
            v = g[r][c] * g[r-1][c] * g[r-2][c] * g[r-3][c]
            if v > bf:
                bf = v

print bf

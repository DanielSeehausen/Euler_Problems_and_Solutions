# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
https://www.hackerrank.com/contests/projecteuler/challenges/euler008

The following is hackerrank's prompt to Project Euler problem #8:

Find the greatest product of  consecutive digits in the  digit number.

Input Format 
First line contains T that denotes the number of test cases. 
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer. 

Output Format 
Print the required answer for each test case.

Constraints 
 1 <= T <= 100
 1 <= K <= 7
 K <= N <= 1000
 

Sample Input

2
10 5
3675356291
10 5
2709360626

Sample Output

3150
0
'''
from sys import stdin

test_cases = int(stdin.readline())

for case in range(test_cases):
    '''
    Compared to the surrounding euler problems (and their time constraints provided by hackerrank) this one is deceptively simple. The method below essentially examines a subsequence of length K along the larger sequence of digits and calculates the new product with every step. Initially, I was expecting aggressive time constraints to fail this type of solution, which would make this problem more interesting.
    
    If I were to optimize this solution for more aggressive time constraints and/or larger possible values of K and N, three changes come to mind immediately: 
    a.) instead of recreating the list named 'curr_subsequence' with every iteration, I would kick off the oldest and append the newest integers OR simply sample the indexes from the larger sequence without creating a new list. 
    b.) I would seek to change the actual calculation of the product by implementing a method that used a working/changing product -- this product would update by dividing out the integer that is getting kicked off the end and multiplying in the new integer on the front every time the subsequence advanced
    c.) if N/K had larger bounds, there would likely come a point where it made sense to automatically stop iteration if we knew that even if the X remaining integers all have a value of 9, the final subsequence can not exceed the current best found product. This optimization is questionable, and only likely if we have extreme n/k limits set or if the problem was designed to fail solutions without this optimization
    
    '''
    #we burn the N, as the length of the sequence is not needed in our python implementation
    #length = K
    length = int(stdin.readline().split(' ')[1])
    sequence = stdin.readline()
    #here we are splitting off the '/n' that readline automatically snags and are left with a string of integers
    sequence = sequence[:len(sequence) - 1]
    
    best_found = float("-inf")
    #starting at the end of the first subset, we get the product of the previous K integers (our subset size)
    for idx in range(length - 1, len(sequence)):
        curr_subsequence = [int(sequence[digit]) for digit in range(idx - length + 1, idx + 1)]
        #reduce simply provides the product of a list of integers
        curr_product = reduce(lambda x, y: x*y, curr_subsequence)
        if curr_product > best_found:
            best_found = curr_product
    
    print best_found
    
    

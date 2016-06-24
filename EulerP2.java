import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {
    //Following prompt from HackerRank:
    //Make sure to check out their Project Euler domain 
    //if you are interested in a great format for 
    //completing Project Euler problems where strong sample inputs are provided 
    /*
    By considering the terms in the Fibonacci sequence whose values do not exceed N, find the sum of the even-valued terms.
    Input Format: First line contains T that denotes the number of test cases. 
                  This is followed by T lines, each containing an integer, N.
    (In my example, testCases reads in T and uBound (upper-bound) reads in each N.)
    https://www.hackerrank.com/contests/projecteuler/challenges/euler002
    */
    //In a nutshell, this solution iteratively sums every even number in the fib sequence, up to the uBound (and not beyond) while
    //ignoring the odd numbers. In examining the first few numbers in the fib sequence, we can see a pattern emerge for the even
    //numbers. The even numbers under 100 are: 2, 8, 34.
    //The pattern we recognize is: while on the current even number, the next even number is the current even number times 4 + the last even number.
    //This can be expressed as nextEvenNumber = 4*currEvenNumber + lastEvenNumber. 
    //It is surprising that this solution satisfies hackerranks time standards, as extremely large inputs are give. I have to imagine there is
    //a more clever way this can be done if one determines the largest even number present in the given uBound. 
    //(Long is used due to large hackerrank inputs)
    
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int testCases = in.nextInt();
        while (testCases > 0) {
            testCases--;
            long uBound = in.nextLong();
            if (1 < uBound && uBound < 8) {
                System.out.println(2);
                continue;
            }
            if (uBound < 2) {
                System.out.println(0);
                continue;
            }
            long workingSum = 0;
            long lastTerm = 0;
            long currTerm = 2;
            long nextTerm = 0;
            while (currTerm < uBound) {
                workingSum += currTerm;
                nextTerm = 4*currTerm + lastTerm;
                lastTerm = currTerm;
                currTerm = nextTerm;
            }
            System.out.println(workingSum);
        }
    }
}

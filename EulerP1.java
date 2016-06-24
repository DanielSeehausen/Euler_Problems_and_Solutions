import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

/*
***Euler P1***
If we list all the natural numbers BELOW 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below .
Input Format: First line contains T that denotes the number of test cases. 
              This is followed by T lines, each containing an integer, N.

***Solution***
Looking at this problem, we quickly see the brute force method of summing the multiples: iterate through every multiple and add it to a running total for 3 and 5. For the problem at hand, this is much more resource intensive than what is required. 

Luckily, we can see that the method of summing these multiples is almost identical to the method of summing from 1 to a larger integer(i.e. 1-10). For that, there is a straightforward polynomial function: x(x+1)/2 (where x is the largest integer in the range). We can adapt this to our needs by multiplying by the multiple we are counting (3 or 5), which yields: (x(x+1)/2)*multiple.
Here, x is the amount of times that the multiple appears in the integer provided. This is easily obtained by dividing the provided integer by the multiple. (i.e. N/3 or N/5)

Now all that remains is adding up the sums we have calculated with the method above for each multiple we are summing (3 and 5 in our case). This solution works for any and all numbers below 16, but fails thereafter. We have neglected to consider those multiples that we are double counting. Every multiple of 15 within our given integer is being double counted. To avoid this, we can use the same method as before and (sum the range of the count of multiples of 15)*15. Then we subtract this from our working sum and are left with the correct answer. 

Because this solution was provided for a set of unknown inputs up to very large sizes, the long and (even longer) BigInteger classes were used instead of int to avoid loss of data if the sums exceed the capacity of the int/long type. 

Uncomment out the lines below if you are running this and want to see the calculated steps. 
*/

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        for (int i = 0; i < n; i++) {
            //System.err.println("Case: " + i);
            //Our upper bound of the range
            long uBound = in.nextLong() - 1;
            //integer division floors/rounds down by default
            long mult3 = uBound / 3;
            long mult5 = uBound / 5;
            //must account for numbers that are double counting (i.e. 15, 30, etc.)
            //in every 15 we get 1 overlap, so we exclude them by summing multiples of 15
            //in the same manner we counted 3/5
            long overlapCount = uBound / 15;
            //System.err.println("3/5 count: " + mult3 + " " + mult5);
            //System.err.println("Excess: " + excess);
            //polynomial expression for summing over integers (0 - n] is 1/2*n(n + 1) 
            BigInteger sum3 = BigInteger.valueOf(mult3*(mult3 + 1)/2*3);
            BigInteger sum5 = BigInteger.valueOf(mult5*(mult5 + 1)/2*5);
            BigInteger excess = BigInteger.valueOf(overlapCount*(overlapCount + 1)/2*15);
            //System.err.println("3/5 sum: " + sum3 + " " + sum5);
            BigInteger answ = sum3.add(sum5);
            answ = answ.subtract(excess);
            System.out.println(answ);
        }
    }
}
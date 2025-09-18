/**
 * https://www.hackerrank.com/challenges/simple-array-sum
 *
 * 

Given an array of  integers, can you find the sum of its elements?

Input Format

The first line contains an integer, , denoting the size of the array. 
The second line contains  space-separated integers representing the array's elements.

Output Format

Print the sum of the array's elements as a single integer.

Sample Input:

6
1 2 3 4 10 11

Sample Output:

31

Explanation:

We print the sum of the array's elements, which is: 1 + 2 + 3 + 4 + 10 + 11 = 31.
 */

import java.io.*;

public class Problem_002_SimpleArraySum {

    public static void main(String[] args) throws Exception {
        BufferedReader bufferedReader = 
            new BufferedReader(new InputStreamReader(System.in));
        String countStr = bufferedReader.readLine();
        String elementsStr = bufferedReader.readLine();
        int count = Integer.parseInt(countStr);
        String[] elements = elementsStr.split(" ", -1);
        int elementsLength = elements.length;
        int sum = 0;
        for (int i=0; i<count && i<elementsLength; i++) {
          sum += Integer.parseInt(elements[i]);
        }
        System.out.println(sum);
    }
}
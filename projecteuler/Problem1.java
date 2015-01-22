/**
 * If we list all the natural numbers below 10 that are multiples of 3 or 5, 
 * we get 3, 5, 6 and 9. The sum of these multiples is 23.
 * Find the sum of all the multiples of 3 or 5 below 1000.
 */

package problem;

public class Problem1 {

    public static void main(String[] args) {
        int sum = 0;
        int[] flags = new int[1001];
        
        int current = 3;
        
        while (current < 1000) {
            if (flags[current] == 0) {
                sum += current;
                flags[current]++;
            }
            current += 3;
        }
        
        current = 5;
        while (current < 1000) {
            if (flags[current] == 0) {
                sum += current;
                flags[current]++;
            }
            current += 5;
        }
        
        System.out.println(sum);
    }

}

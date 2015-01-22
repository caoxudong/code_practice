/**
 * The prime factors of 13195 are 5, 7, 13 and 29.
 * What is the largest prime factor of the number 600851475143 ?
 */

package problem;

public class Problem3 {

    public static void main(String[] args) {
        long targetNumber = 600851475143L;
        int maxCapacity = (int)Math.ceil(Math.sqrt((double)targetNumber));
        long i = 2;
        long maxPrimeFactor = i;
        boolean[] flags = new boolean[maxCapacity + 1];
        while (true) {
            if ((int)i >= maxCapacity) {
                break;
            }
            if (flags[(int)i] == true) {
                i++;
                continue;
            }
            if ( targetNumber % i == 0 ) {
                maxPrimeFactor = i;
                targetNumber /= i;
            }
            long index = i;
            while ( index < flags.length ) {
                flags[(int) index] = true;
                index += i;
            }
            i++;
        }
        System.out.println(maxPrimeFactor);
    }

}


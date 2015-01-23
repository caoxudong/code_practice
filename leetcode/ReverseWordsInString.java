/**
 *  "this is a test" => "test a is this"
 *  https://oj.leetcode.com/problems/reverse-words-in-a-string/
 */
public class ReverseWordsInString {
    public static String reverseWords(char[] chars) {
        int count =  chars.length;
        for (int i=0; i<count/2; i++) {
            char c = chars[i];
            chars[i] = chars[count - 1 - i];
            chars[count - 1 - i] = c;
        }

        int begin = 0;
        for (int i=0; i<count; i++) {
            if (chars[i] == ' ') {
                for (int j=begin; j<(begin+(i-begin)/2); j++) {
                    char c = chars[j];
                    chars[j] = chars[i - 1 - (j - begin)];
                    chars[i - 1 - (j - begin)] = c;
                }
                begin = i + 1;
            }
        }

        for (int j=begin; j<(begin+(count-begin)/2); j++) {
            char c = chars[j];
            chars[j] = chars[count - 1 - (j - begin)];
            chars[count - 1 - (j - begin)] = c;
        }
        return new String(chars);
    }

    public static void main(String[] args) {
        String str = "111 22 333 444  555 6";
        char[] chars = new char[str.length()];
        str.getChars(0, str.length(), chars, 0);
        System.out.println(reverseWords(chars));
    }
}
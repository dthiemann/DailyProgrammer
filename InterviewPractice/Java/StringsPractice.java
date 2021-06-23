package InterviewPractice.Java;

import java.util.HashMap;

public class StringsPractice {

    // 1.1 - Implement an algorith mto determine if a string has
    // all unique characters. What if you cannot use additional DS?

    public boolean uniqueCharactersV1(String s) {
        // Assuming ASCII string (no more than 256 characters)
        boolean[] map = new boolean[256];

        for (int i = 0; i < s.length(); i++) {
            int value = s.charAt(i);
            if (map[value]) {
                return false;
            }
            map[value] = true;
        }

        return true;
    }

    /*
     * 
     * 1.3 Given two strings, write a method to decide if one is a permutation of
     * the other
     * 
     * ABCDE -- DABCE
     */

    public boolean isPalindrome(String string1, String string2) {
        if (string1.length() != string2.length()) {
            return false;
        }

        // Same assumption as above (ASCII string)
        int[] buffer = new int[256];

        // Populate buffer
        for (int i = 0; i < string1.length(); i++) {
            int charValue = string1.charAt(i);
            buffer[charValue]++;
        }

        // Subtract other string from buffer ---
        // If we hit < 0 return false
        for (int i = 0; i < string2.length(); i++) {
            int charValue = string2.charAt(i);
            if (--buffer[charValue] < 0) {
                return false;
            }
        }

        return true;
    }

    public static void main(String[] args) {
        StringsPractice sp = new StringsPractice();
        // System.out.println(sp.isPalindrome("ABCDEF", "ABCDFE"));
        // System.out.println(sp.isPalindrome("ABCDEF", "ABCDXE"));
    }
}

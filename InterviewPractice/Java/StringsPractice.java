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

    public static void main(String[] args) {

    }
}

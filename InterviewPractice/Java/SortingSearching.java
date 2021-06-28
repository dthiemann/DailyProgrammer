package InterviewPractice.Java;

import java.util.List;
import java.util.ArrayList;

public class SortingSearching {

    private void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + ", ");
        }
        System.out.println();
    }

    /**
     * You are given two sorted arrays, A and B, where A has a large enough buffer
     * at the end to hold B. Write a method to emrge B into A in sorted order
     */
    private void mergeTwoSortedArrays(int[] a, int[] b) {
        var endOfA = a.length - b.length - 1;
        var endOfB = b.length - 1;

        var startIndex = endOfA + b.length;
        while (endOfA >= 0 && endOfB >= 0) {
            if (a[endOfA] > b[endOfB]) {
                a[startIndex] = a[endOfA];
                endOfA--;
            }

            else if (a[endOfA] <= b[endOfB]) {
                a[startIndex] = b[endOfB];
                endOfB--;
            }

            startIndex--;
        }

        while (endOfB > 0) {
            a[startIndex--] = b[endOfB--];
        }

    }

    public void testMergeTwoSortedArrays() {
        int[] a1 = new int[10];
        a1[0] = 1;
        a1[1] = 3;
        a1[2] = 5;
        a1[3] = 7;
        int[] b1 = { 2, 4, 6, 8, 10, 12 };
        mergeTwoSortedArrays(a1, b1);
        printArray(a1);
    }

    public static void main(String[] args) {
        var testClass = new SortingSearching();
        testClass.testMergeTwoSortedArrays();
    }
}
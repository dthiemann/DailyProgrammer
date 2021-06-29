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

    /**
     * Given a sorted array of n integers that has been roated an unknown number of
     * times, write code to find an eleement in the array. You may assume that the
     * array was originally sorted in increasing order
     */
    private int findIndexOfValueInArray(int[] a, int target, int left, int right) {
        int middle = (a.length - 1) / 2;

        if (target == a[middle])  {
            return middle;
        }

        // Left side is normally sorted
        if (a[left] < a[middle]) {
            if (target < a[middle] && target >= a[left])
                return findIndexOfValueInArray(a, target, left, middle - 1);
            else {
                return findIndexOfValueInArray(a, target, middle + 1, right)
            }
        }

        // Right side is noramlly sorted
        else if (a[middle] < a[right]) {
            if (target > a[middle] && target <= a[middle]) {
                return findIndexOfValueInArray(a, target, middle + 1, right);
            } else {
                return findIndexOfValueInArray(a, target, left, middle - 1);
            }
        }

        // Left side is all duplicates
        else if (a[left] == a[middle]) {
            if (a[middle] != a[right]) {
                return findIndexOfValueInArray(a, target, middle + 1, right);
            } else {
                int result = findIndexOfValueInArray(a, target, left, middle - 1);
                if (result == -1) {
                    return findIndexOfValueInArray(a, target, middle + 1, right);
                }
                else {
                    return result;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        var testClass = new SortingSearching();
        testClass.testMergeTwoSortedArrays();
    }
}
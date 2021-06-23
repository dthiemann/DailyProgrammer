package InterviewPractice;

import java.util.List;
import java.util.ArrayList;

public class InterviewPrep {

    // ******************************** MERGE SORT ********************************
    /**
     * Returns a sorted list
     */
    private void mergeSort(int[] integerList) {
        this.mergeSortHelper(integerList, 0, integerList.length - 1);
    }

    private void mergeSortHelper(int[] integerList, int startIndex, int endIndex) {
        if (startIndex < endIndex) {
            int middleIndex = (startIndex + endIndex) / 2;

            mergeSortHelper(integerList, startIndex, middleIndex);
            mergeSortHelper(integerList, middleIndex + 1, endIndex);

            merge(integerList, startIndex, middleIndex, endIndex);
        }
    }

    private void merge(int[] integerList, int left, int middle, int right) {
        int leftListLength = middle - left + 1;
        int rightListLength = right - middle;

        int[] leftTempList = new int[leftListLength];
        int[] rightTempList = new int[rightListLength];

        // Copy data over
        for (int i = 0; i < leftListLength; i++) {
            leftTempList[i] = integerList[left + i];
        }
        for (int i = 0; i < rightListLength; i++) {
            rightTempList[i] = integerList[middle + i + 1];
        }

        //
        int i = 0;
        int j = 0;
        int k = left;

        // Compare two temp lists until one is empty - updating the
        while (i < leftListLength && j < rightListLength) {
            if (leftTempList[i] < rightTempList[j]) {
                integerList[k] = leftTempList[i];
                i++;
            } else {
                integerList[k] = rightTempList[j];
                j++;
            }
            k++;
        }

        // Pad rest of list if values are still present in any of the temp lists
        while (i < leftListLength) {
            integerList[k] = leftTempList[i++];
            k++;
        }

        while (j < rightListLength) {
            integerList[k] = rightTempList[j++];
            k++;
        }
    }

    public void testMergeSort() {
        int[] intList = new int[] { 1, 2, 3, 4, 5, 6, };
        int[] intList2 = new int[] { 6, 5, 4, 3, 2, 1, };
        int[] intList3 = new int[] { 4, 6, 1, 5, 2, 3, };

        this.mergeSort(intList);
        this.mergeSort(intList2);
        this.mergeSort(intList3);

        printList(intList);
        printList(intList2);
        printList(intList3);

    }

    // ******************************** MERGE SORT ********************************
    // ******************************** QUICK SORT ********************************

    private void quickSort(int[] intArray) {
        quickSortHelper(intArray, 0, intArray.length - 1);
    }

    private void quickSortHelper(int[] intArray, int start, int end) {
        if (start < end) {
            int pivot = partition(intArray, start, end);

            quickSortHelper(intArray, start, pivot - 1);
            quickSortHelper(intArray, pivot + 1, end);
        }
    }

    private int partition(int[] intArray, int start, int end) {
        int pivot = intArray[end];

        int i = start;
        for (int j = start; j < end; j++) {
            if (intArray[j] < pivot) {
                swap(intArray, i, j);
                i = i + 1;
            }
        }

        swap(intArray, i, end);

        return i;
    }

    public void testQuickSort() {
        int[] intList = new int[] { 1, 2, 3, 4, 5, 6, };
        int[] intList2 = new int[] { 6, 5, 4, 3, 2, 1, };
        int[] intList3 = new int[] { 4, 6, 1, 5, 2, 3, };

        this.quickSort(intList);
        this.quickSort(intList2);
        this.quickSort(intList3);

        printList(intList);
        printList(intList2);
        printList(intList3);
    }

    // ******************************** QUICK SORT ********************************

    /**
     * Helper methods
     */

    private void printList(int[] intList) {
        System.out.print("[");
        for (int i = 0; i < intList.length; i++) {
            System.out.print(intList[i] + ", ");
        }
        System.out.print("]\n");
    }

    private void swap(int[] intList, int a, int b) {
        int temp = intList[a];
        intList[a] = intList[b];
        intList[b] = temp;
    }

    public static void main(String args[]) {
        InterviewPrep test = new InterviewPrep();
        // test.testMergeSort();
        test.testQuickSort();
    }
}
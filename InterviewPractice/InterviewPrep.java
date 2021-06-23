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

    private void printList(int[] intList) {
        System.out.print("[");
        for (int i = 0; i < intList.length; i++) {
            System.out.print(intList[i] + ", ");
        }
        System.out.print("]\n");
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

    public static void main(String args[]) {
        InterviewPrep test = new InterviewPrep();
        test.testMergeSort();
    }
}
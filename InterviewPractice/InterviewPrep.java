package InterviewPractice;

import java.util.List;
import java.util.ArrayList;

public class InterviewPrep {

    /**
     * Returns a sorted list
     */
    private void mergeSort(List<Integer> integerList) {

    }

    public void testMergeSort() {
        ArrayList<Integer> intList = new ArrayList<Integer>() {
            {
                add(1);
                add(2);
                add(3);
                add(4);
                add(5);
                add(6);
            }
        };

        ArrayList<Integer> intList2 = new ArrayList<Integer>() {
            {
                add(6);
                add(5);
                add(4);
                add(3);
                add(2);
                add(1);
            }
        };

        ArrayList<Integer> intList3 = new ArrayList<Integer>() {
            {
                add(4);
                add(6);
                add(1);
                add(5);
                add(2);
                add(3);
            }
        };
        this.mergeSort(intList);
        this.mergeSort(intList2);
        this.mergeSort(intList3);
    }

    public static void main(String args[]) {
        InterviewPrep test = new InterviewPrep();
        test.testMergeSort();
    }
}
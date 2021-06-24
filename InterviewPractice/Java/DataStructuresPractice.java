package InterviewPractice.Java;

public class DataStructuresPractice {
    private class Node<T> {
        Node next = null;
        T data;

        public Node(T data) {
            this.data = data;
        }

        public void appendToTail(T data) {
            var end = new Node<T>(data);

            var current = this;
            while (current.getNext() != null) {
                current = current.getNext();
            }

            current.setNext(end);
        }

        public Node<T> getNext() {
            return this.next;
        }

        public void setNext(Node<T> next) {
            this.next = next;
        }
    }

    /**
     * Remove duplicates from a linked list
     */
    private void removeDuplicates1(Node<T> head) {
        if (head == null) {
            return;
        }

        var current = head;
        while (current != null) {
            var runner = current;
            while (runner.next != null) {
                if (runner.data == runner.getNext().data) {
                    runner.setNext(runner.getNext().getNext());
                } else {
                    runner = runner.next;
                }
            }
        }
    }

    /**
     * find the kth to last element of a singly linked list
     */

    private Node findTheKthElement(Node<T> head, int k) {
        var runner = head;
        for (int i = 0; i < k; i++) {
            if (runner == null) {
                return null;
            }
            runner = runner.getNext();
        }

        while (runner.getNext() != null) {
            runner = runner.getNext();
            head = head.getNext();
        }

        return head;
    }

    /**
     * Delete a node in the middle of a singly linked list
     * 
     * @param nodeToDelete
     */
    private void deleteNode(Node<T> nodeToDelete) {
        if (nodeToDelete.getNext() == null)
            nodeToDelete = null;

        else {
            nodeToDelete.data = nodeToDelete.getNext().data;
            nodeToDelete.setNext(nodeToDelete.getNext().getNext());
        }
    }

    public static void main(String args[]) {

    }
}
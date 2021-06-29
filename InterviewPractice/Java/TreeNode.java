package InterviewPractice.Java;

import org.graalvm.compiler.replacements.nodes.arithmetic.IntegerExactArithmeticNode;

public class TreeNode<T> {
    private T data;
    private TreeNode<T> leftChild;
    private TreeNode<T> rightChild;

    public TreeNode(T data) {
        this.data = data;
    }

    public TreeNode(T data, TreeNode<T> leftChild, TreeNode<T> rightChild) {
        this(data);
        this.leftChild = leftChild;
        this.rightChild = rightChild;
    }

    public void setData(T data) {
        this.data = data;
    }

    public void addLeftNode(TreeNode<T> leftNode) {
        this.leftChild = leftNode;
    }

    public void addRightNode(TreeNode<T> rightNode) {
        this.rightChild = rightNode;
    }

    public T getData() {
        return this.data;
    }

    public TreeNode<T> getLeftChild() {
        return this.leftChild;
    }

    public TreeNode<T> getRightChild() {
        return this.rightChild;
    }

    /**
     * Given a sorted array (increasing order) with unique integer elements, write
     * an algorithm to create a binary search tree with minimal height
     */

    public TreeNode<Integer> createTreeFromList(int[] intList) {
        if (intList.length <= 0) {
            return null;
        }

        var root = createTreeFromListHelper(null, intList, 0, intList.length - 1);

        return root;

    }

    private TreeNode<Integer> createTreeFromListHelper(int[] intList, int left, int right) {
        if (left > right) {
            return null;
        }

        var mid = (right - left) / 2;

        var node = new TreeNode<Integer>(intList[mid]);
        node.addLeftNode(createTreeFromListHelper(intList, left, mid - 1));
        node.addRightNode(createTreeFromListHelper(intList, mid + 1, right));

        return node;
    }

    public static void main(String[] args) {

    }

}

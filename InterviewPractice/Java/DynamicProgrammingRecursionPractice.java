package InterviewPractice.Java;

import java.util.HashMap;
import java.util.Map;

public class DynamicProgrammingRecursionPractice {

    /**
     * A child is running up a stair case with n steps, and can either hope 1 step,
     * 2 steps, or 3 steps at a time. Implement a method to count how many
     * possibilities the chil can run up the stairs
     * 
     * Base cases: if (n == 3): 1 (3)
     * 
     */

    private int oneStepTwoStepThreeSteps(int numSteps) {

        if (numSteps < 0) {
            return 0;
        }
        if (numSteps == 0) {
            return 1;
        }

        return oneStepTwoStepThreeSteps(numSteps - 3) + oneStepTwoStepThreeSteps(numSteps - 2)
                + oneStepTwoStepThreeSteps(numSteps - 1);
    }

    public void testOneStepTwoStepsThreeSteps() {
        System.out.println(oneStepTwoStepThreeSteps(3));
        System.out.println(oneStepTwoStepThreeSteps(4));

    }

    /**
     * Imagine a robot sitting on the upper left corner of an X by Y grid. The robot
     * can only move in two directions: right and down. How many possible paths are
     * there for the robot to go from (0,0) to (X,Y)?
     * 
     * (0,0) -> (1, 1) = 2 possible paths (0,0) -> (1, 2) = 3 possible paths
     */

    private int countRobotPathOptions(int destX, int destY) {
        return countRobotPathOptionsHelper(0, 0, destX, destY);
    }

    private int countRobotPathOptionsDynamic(int destX, int destY) {
        return countRobotPathOptionsHelperDynamic(0, 0, destX, destY, new HashMap<String, Integer>());
    }

    private int countRobotPathOptionsHelper(int startX, int startY, int destX, int destY) {

        if (startX == destX && startY == destY) {
            return 1;
        }
        if (startX > destX || startY > destY) {
            return 0;
        }

        return countRobotPathOptionsHelper(startX + 1, startY, destX, destY)
                + countRobotPathOptionsHelper(startX, startY + 1, destX, destY);
    }

    private int countRobotPathOptionsHelperDynamic(int startX, int startY, int destX, int destY,
            Map<String, Integer> pointMap) {

        var key = String.format("%d,%d", startX, startY);

        if (pointMap.containsKey(key)) {
            return pointMap.get(key);
        }

        if (startX == destX && startY == destY) {
            return 1;
        }
        if (startX > destX || startY > destY) {
            return 0;
        }

        var result = countRobotPathOptionsHelperDynamic(startX + 1, startY, destX, destY, pointMap)
                + countRobotPathOptionsHelperDynamic(startX, startY + 1, destX, destY, pointMap);
        pointMap.put(key, result);

        return result;
    }

    public void testRobotPathCounting() {
        System.out.println(countRobotPathOptions(12, 6));
        System.out.println(countRobotPathOptionsDynamic(12, 6));
    }

    public static void main(String args[]) {
        var x = new DynamicProgrammingRecursionPractice();
        // x.testOneStepTwoStepsThreeSteps();
        x.testRobotPathCounting();
    }
}

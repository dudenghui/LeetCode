import java.util.HashMap;

class Solution1 {
    public int[] twoSum(int[] nums, int target) {
        int n = nums.length;
        for (int i = 0; i < n; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (nums[i] + nums[j] == target) {
                    return new int[] { i, j };
                }
            }
        }
        return new int[0];
    }
}

class Solution2 {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashtable = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; ++i) {
            if (hashtable.containsKey(target - nums[i])) {
                return new int[] { hashtable.get(target - nums[i]), i };
            }
            hashtable.put(nums[i], i);
        }
        return new int[0];
    }
}

class Solution {
    public static void main(String[] args) {
        
        System.out.println("haha");
        int[] nums = { 2, 4, 5, 1, 2, 5 };
        int target = 7;
        for (int n : nums) {
            System.out.println(n);
        }
        System.out.println("target:" + target);

        // Solution1
        System.out.println("\nSolution1");
        Solution1 sol1 = new Solution1();
        int[] result = sol1.twoSum(nums, target);
        for (int r : result) {
            System.out.println(r);
        }
        // Solution2
        System.out.println("\nSolution2");
        Solution2 sol2 = new Solution2();
        result = sol2.twoSum(nums, target);
        for (int r : result) {
            System.out.println(r);
        }
    }
}
class Solution {
    public int maxSubArray(int[] nums) {
        int bestSum = nums[0];
        for (int i = 1; i < nums.length; i++){
            if (nums[i - 1] > 0) nums[i] += nums[i - 1];
            bestSum = Math.max(bestSum, nums[i]);
        }
        return bestSum;
    }
}
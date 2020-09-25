class Solution {
    public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        int minLength = Integer.MAX_VALUE;
        int start = 0, sum = 0;
        
        for (int i = 0; i < n; i++){
            sum += nums[i];
            while (sum >= s){
                minLength = Math.min(minLength, i - start + 1);
                sum -= nums[start++];
            }
        }
        return minLength != Integer.MAX_VALUE ? minLength : 0;
    }
}
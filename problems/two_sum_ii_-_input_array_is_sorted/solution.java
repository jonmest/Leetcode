class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int low = 0, high = numbers.length - 1;
        int[] toReturn = new int[2];
        
        while (low < high) {
            if (numbers[low] + numbers[high] > target) {
                high--;
            } else if (numbers[low] + numbers[high] < target) {
                low++;
            } else {
                toReturn[0] = low+1;
                toReturn[1] = high+1;
                break;
            }
        }
        return toReturn;
    }
}
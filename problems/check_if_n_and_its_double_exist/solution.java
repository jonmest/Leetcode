class Solution {
    public boolean checkIfExist(int[] arr) {
        HashMap<Integer, Boolean> seen = new HashMap<Integer, Boolean>();
        for (int i = 0; i < arr.length; i++) {
            if (
                seen.containsKey(arr[i] * 2) ||
                seen.containsKey((int) Math.floor(arr[i] / 2)) && arr[i] % 2 == 0
            ) return true;
            seen.put(arr[i], true);
        }
        return false;
    }
}
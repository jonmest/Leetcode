class Solution {
    public double average(int[] salary) {
        for (int i = 1; i < salary.length; i++) {
            int key = salary[i];
            int j = i - 1;
            while (j >= 0 && salary[j] > key) {
                salary[j+1] = salary[j];
                j = j-1;
            }
            salary[j+1] = key;
        }
        int sum = 0;
        for (int i = 1; i < salary.length-1; i++) {
            sum += salary[i];
        }
        return (double) sum / (salary.length - 2);
    }
}
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer_a = 0
        pointer_b = len(numbers)-1
        
        while (pointer_a <= pointer_b):
            if (numbers[pointer_a] + numbers[pointer_b]) < target:
                pointer_a += 1
            elif (numbers[pointer_a] + numbers[pointer_b]) > target:
                pointer_b -= 1
            else:
                return (pointer_a+1, pointer_b+1)
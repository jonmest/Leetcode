class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        number_indices = {}
        result = []
        for i in range(len(nums)):
            num = nums[i]
            difference = target - num
            if not number_indices.get(difference) == None:
                return [
                    i, number_indices[difference]
                ]
            
            number_indices[num] = i
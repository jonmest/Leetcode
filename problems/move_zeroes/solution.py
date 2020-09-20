class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        anchor = 0
        for explorer in range(len(nums)):
            if (nums[explorer] != 0):
                tmp = nums[anchor]
                nums[anchor] = nums[explorer]
                nums[explorer] = tmp
                anchor += 1

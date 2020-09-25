from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        max_count = 0
        majority = None
        for item in table:
            if table[item] > max_count:
                majority = item
                max_count = table[item]
        return majority
            
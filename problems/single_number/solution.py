from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = defaultdict(int)
        for n in nums:
            table[n] += 1
        for n in table:
            if table[n] == 1: return n
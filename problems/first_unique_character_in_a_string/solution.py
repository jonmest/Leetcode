from collections import defaultdict
class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = defaultdict(int)
        for char in s:
            table[char] += 1
        for item in table:
            if table[item] == 1: return s.index(item)
        return -1
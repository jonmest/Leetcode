from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = defaultdict(int)
        for c in s:
            table[c] += 1
        for c in t:
            table[c] -= 1
        for key in table:
            if table[key] != 0: return False
        return True
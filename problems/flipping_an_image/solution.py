import math
class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            M = len(row)
            for j in range(math.floor((M+1)/2)):
                row[j], row[~j] = row[~j] ^ 1, row[j] ^ 1
        return A
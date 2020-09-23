class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squared = sorted(
                    list(
                        map(lambda x: x**2, A)
                    )
        )
        return squared
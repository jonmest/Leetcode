class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack) is 0 and len(needle) is 0: return 0
        for i in range(len(haystack)-len(needle)+1):
                if haystack[i:i+len(needle)] == needle:
                    return i
        return -1
            
                
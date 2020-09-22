class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) == 0: return prefix
        for i in range(len(strs[0])):
            common = True
            for s in strs:
                print(i, s)
                if i >= len(s):
                    common = False
                    break
                if s[i] != strs[0][i]: common = False
            if not common: break
            prefix += strs[0][i]
        return prefix
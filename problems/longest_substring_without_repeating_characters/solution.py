class Solution(object):
    def lengthOfLongestSubstring(self, s):
        max_length = 0
        occured = []
        for i in range(len(s)):
            occured.append(s[i])
            right = i+1
            while right <= len(s)-1:
                if not s[right] in occured:
                    occured.append(s[right])
                    right += 1
                else: break
            if len(occured) > max_length:
                        max_length = len(occured)
            occured = []
                    
        return max_length
class Solution(object):
    def findTheDifference(self, s, t):
        t_sum = 0
        for i in t:
            t_sum += ord(i)
        s_sum = 0
        for i in s:
            s_sum += ord(i)
        return chr(t_sum - s_sum)
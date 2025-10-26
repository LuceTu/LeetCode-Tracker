# Last updated: 10/26/2025, 4:57:17 PM
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        window = set()
        right = 0
        maxLen = 0
        for right in range(len(s)):
            while s[right] in window:
                window.remove(s[left])
                left +=1
            window.add(s[right])
            maxLen = max(maxLen, right - left +1)
        return maxLen
# Last updated: 10/26/2025, 4:57:10 PM
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        count = [0] * 26  # 固定长度的array 
        
        for ch in s:
            count[ord(ch) - ord('a')] += 1
        for ch in t:
            count[ord(ch) - ord('a')] -= 1

        return all(c == 0 for c in count)